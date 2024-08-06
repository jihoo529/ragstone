import argparse
import os
import shutil
from langchain_community.document_loaders.pdf import PyMuPDFLoader
from langchain_community.document_loaders.directory import DirectoryLoader
from langchain_community.document_loaders import UnstructuredCSVLoader, TextLoader, UnstructuredMarkdownLoader, UnstructuredExcelLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
# from get_embedding import get_embedding_function
from langchain_community.vectorstores.chroma import Chroma
from .json_loader import JSONLoader
import pymongo
from pymongo.errors import PyMongoError
from langchain_huggingface import HuggingFaceEmbeddings
from app.db.mongo import MongoKeyValueDB
import asyncio
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
CHROMA_DIR = os.path.join(BASE_DIR, 'chroma')

# MongoDB configuration
MONGO_URI = "mongodb://mongodb:27017/"
DB_NAME = "ragstone"
FILES_COLLECTION_NAME = "populated_files"
SETTINGS_COLLECTION_NAME = "settings"
DEFAULT_CHUNK_SIZE = 1024
DEFAULT_CHUNK_OVERLAP = 300

loaders = {
    '.pdf': PyMuPDFLoader,
    '.csv': UnstructuredCSVLoader,
    '.txt': TextLoader,
    '.json': JSONLoader,
    '.md': UnstructuredMarkdownLoader,
    '.xlsx': UnstructuredExcelLoader,
    '.docx': Docx2txtLoader
}

def get_mongo_client():
    return pymongo.MongoClient(MONGO_URI)

def get_embedding_function():
    model_name = "BAAI/bge-small-en-v1.5"
    encode_kwargs = {'normalize_embeddings': False}
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        encode_kwargs=encode_kwargs
    )
    return embeddings

async def populate_database(category: str, progress_callback=None):
    # global DATA_PATH, CHROMA_PATH
    print("HELLo")
    data_path = os.path.join(DATA_DIR, category)
    chroma_path = os.path.join(CHROMA_DIR, category)

    if progress_callback:
        await progress_callback("Starting document loading...")
        time.sleep(0.5)
    documents = load_documents(data_path)
    
    if progress_callback:
        await progress_callback(f"Loaded {len(documents)} documents. Updating MongoDB...")
        time.sleep(0.5)
    update_mongodb(category, documents)
    
    if progress_callback:
        await progress_callback("Splitting documents...")
        time.sleep(0.5)
    chunks = split_documents(documents)
    
    if progress_callback:
        await progress_callback(f"Adding {len(chunks)} chunks to Chroma...")
        time.sleep(0.5)
    response = await add_to_chroma(chunks, chroma_path, progress_callback)
    
    if progress_callback:
        await progress_callback(f"Database population complete. Response: {response}")
        time.sleep(10)

def create_directory_loader(file_type, directory_path):
    return DirectoryLoader(
        path=directory_path,
        glob=f"**/*{file_type}",
        loader_cls=loaders[file_type],
        use_multithreading=True
    )

def load_documents(data_path):
    md_loader = create_directory_loader('.md', data_path)
    md_docs = md_loader.load()
    
    txt_loader = create_directory_loader('.txt', data_path)
    txt_docs = txt_loader.load()
    
    csv_loader = create_directory_loader('.csv', data_path)
    csv_docs = csv_loader.load()
    ####problematic line
    print(data_path)
    pdf_loader = create_directory_loader('.pdf', data_path)
    pdf_docs = pdf_loader.load()

    json_loader = create_directory_loader('.json', data_path)
    json_docs = json_loader.load()

    excel_loader = create_directory_loader('.xlsx', data_path)
    excel_docs = excel_loader.load()

    word_loader = create_directory_loader('.docx', data_path)
    word_docs = word_loader.load()

    docs = txt_docs + md_docs + csv_docs + json_docs + excel_docs + word_docs
    print(docs)
    return docs

def update_mongodb(category, documents):
    try:
        with MongoKeyValueDB(db_name=DB_NAME, collection_name=FILES_COLLECTION_NAME) as mkvdb:
            for doc in documents:
                if 'source' in doc.metadata:
                    mkvdb.set(doc.metadata['source'], category, True)
    except Exception as e:
        print(e)

# def split_documents(documents: list[Document]):
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1024,
#         chunk_overlap=300,
#         length_function=len,
#         is_separator_regex=False,
#     )
#     return text_splitter.split_documents(documents)

def split_documents(documents: list[Document]):
    with pymongo.MongoClient(MONGO_URI) as client:
        db = client[DB_NAME]
        settings = db[SETTINGS_COLLECTION_NAME].find_one()
    
    chunk_size = settings.get('chunk_size', DEFAULT_CHUNK_SIZE)
    chunk_overlap = settings.get('chunk_overlap', DEFAULT_CHUNK_OVERLAP)
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)

async def add_to_chroma(chunks: list[Document], chroma_path, progress_callback=None):
    db = Chroma(
        persist_directory=chroma_path,
        embedding_function=get_embedding_function()
    )
    chunks_with_ids = calculate_chunk_ids(chunks)

    existing_items = db.get(include=[])
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

    new_chunks = [chunk for chunk in chunks_with_ids if chunk.metadata["id"] not in existing_ids]

    if new_chunks:
        if progress_callback:
            await progress_callback(f"Adding {len(new_chunks)} new documents...")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
        db.persist()
        print("✅ Added successfully")
        return "success"
    else:
        print("✅ No new documents to add")
        return "no documents to add"

def calculate_chunk_ids(chunks):
    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        chunk.metadata["id"] = chunk_id

    return chunks

async def clear_database(category):
    print("Starting database clearing process")
    chroma_path = os.path.join(CHROMA_DIR, category)
    if os.path.exists(chroma_path):
        shutil.rmtree(chroma_path)
        print(f"Removed Chroma directory for category: {category}")

        with get_mongo_client() as client:
            db = client[DB_NAME]
            result = db[FILES_COLLECTION_NAME].delete_many({"category": category})
            print(f"Deleted {result.deleted_count} documents from {FILES_COLLECTION_NAME} where category = {category}")
    else:
        print(f"No Chroma directory found for category: {category}")

    print("Database clearing process completed")

if __name__ == "__main__":
    clear_database()