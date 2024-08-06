# backend/app/services/chat_service.py

from fastapi import Depends
from ..schemas.chat_schemas import ChatMessage, ChatResponse
from langchain_community.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from .chromadb.get_embedding import get_embedding_function
from concurrent.futures import ProcessPoolExecutor
import os
import asyncio
from typing import List, Dict, Callable, Any
import logging
import traceback
import functools
import pymongo

# Consider moving these to a config file
MONGO_CONNECTION_STRING = "mongodb://mongodb:27017"
DB_NAME = "ragstone"
COLLECTION_NAME = "settings"

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
CHROMA_PATH = "chroma"
PROMPT_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "utils", "prompt.txt")
DEFAULT_PROMPT_TEMPLATE = """
    {You are an intelligent assistant called Ragstone helping Equinix Hong Kong office's potential & current customers to answer their queries. 
    Give simple and direct answers without additional statements. Do not append any According to the provided context, just give answer directly.
    DO NOT make up answers, answer the question based ONLY on the following context:}

    {context}

    ---

    Answer the question based on the above context: {question}
    """

class ChatService:
    _instance = None

    @classmethod
    def get_instance(cls, chroma_path: str):
        if cls._instance is None:
            cls._instance = cls(chroma_path)
        return cls._instance
    
    def __init__(self, chroma_path: str):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        
        # Create a file handler
        fh = logging.FileHandler('chat_service.log')
        fh.setLevel(logging.DEBUG)
        
        # Create a console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # Create a formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        # Add the handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        # self.chroma_path = chroma_path
        self.embedding_function = get_embedding_function()
        # self.db = Chroma(persist_directory=f'{CHROMA_PATH}/{self.chroma_path}', embedding_function=self.embedding_function)
        # self.model = Ollama(model="gemma2:2b", base_url=OLLAMA_BASE_URL)
        
        # print(self.chroma_path)

        self.client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
        self.db = self.client[DB_NAME]
        self.collection = self.db[COLLECTION_NAME]

        model_name = self.collection.find_one({"model": {"$exists": True}}, {"_id": 0, "model": 1})["model"]
        
        self.model = Ollama(model=model_name, base_url=OLLAMA_BASE_URL)
        self.prompt_template = self.load_prompt_template()

        self.chroma_connections = {}

    def load_prompt_template(self) -> ChatPromptTemplate:
        document = self.collection.find_one({
                "prompt_template": {"$exists": True}
            })
        self.logger.debug(document)
        try:
            document = self.collection.find_one({
                "prompt_template": {"$exists": True}
            })

            if document and "prompt_template" in document:
                prompt_content = document["prompt_template"].strip()
                
                full_template = f"""
                    {prompt_content}

                    {{context}}

                    ---

                    Answer the question based on the above context: {{question}}
                """
                return ChatPromptTemplate.from_template(full_template)
            else:
                self.logger.warning("Prompt template not found in MongoDB. Using default template.")
                return ChatPromptTemplate.from_template(DEFAULT_PROMPT_TEMPLATE)
        
        except Exception as e:
            self.logger.error(f"Failed to load prompt template: {str(e)}")
            # Fallback to a default template if file reading fails
            return ChatPromptTemplate.from_template(DEFAULT_PROMPT_TEMPLATE)
        
    def get_chroma(self, category: str):
        if category not in self.chroma_connections:
            chroma_path = f'{CHROMA_PATH}/{category}'
            self.chroma_connections[category] = Chroma(persist_directory=chroma_path, embedding_function=self.embedding_function)
        return self.chroma_connections[category]
    
    async def process_rag_query(self, query_text: str, category: str) -> Dict[str, any]:
        try:
            chroma_db = self.get_chroma(category)
            results = await asyncio.to_thread(chroma_db.similarity_search_with_score, query_text, k=4)

            context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
            prompt = self.prompt_template.format(context=context_text, question=query_text)

            response_text = await asyncio.to_thread(self.model.invoke, prompt)

            sources = [doc.metadata.get("id", None) for doc, _score in results]
            return {
                "response": response_text,
                "sources": sources
            }
        except Exception as e:
            print(f"Error processing query: {e}")
            return {"response": "An error occurred while processing your query.", "sources": []}

    async def process_single_query(self, message: ChatMessage) -> ChatResponse:
        # self.chroma_path = message.category
        result = await self.process_rag_query(message.message, message.category)
        
        return ChatResponse(response=result["response"], sources=result["sources"])

    
    
    
# Dependency
def get_chat_service():
    return ChatService(chroma_path="chroma")
