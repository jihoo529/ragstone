import pymupdf4llm
import pathlib
from pathlib import Path
import os
import pymupdf
import pytesseract
from PIL import Image
from io import BytesIO
from markdownify import markdownify as md

def is_scanned_pdf(doc):
    """Check if a PDF document is scanned (no extractable text)."""
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        if text.strip():
            return False
    return True

def ocr_pdf(doc):
    """Perform OCR on a scanned PDF."""
    text = ""
    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap()
        img = Image.open(BytesIO(pix.tobytes("png")))
        page_text = pytesseract.image_to_string(img, lang='eng', config='--psm 6')
        text += page_text + "\n"
    return text

def convert_to_markdown(pdf_path):
    doc = pymupdf.open(pdf_path)
    if is_scanned_pdf(doc):
        text = ocr_pdf(doc)
        markdown = md(text)

        # markdown = None
    else:
        markdown = pymupdf4llm.to_markdown(pdf_path)
    return markdown

def parse_and_save(pdf_path):
    markdown_path = pdf_path.replace('.pdf', '.md')
    if os.path.exists(markdown_path):
        return
    
    md_text = convert_to_markdown(pdf_path)
    if md_text is not None:
        pathlib.Path(markdown_path).write_bytes(md_text.encode())
        # if os.path.exists(pdf_path):
        #     os.remove(pdf_path)
        #     st.write(f"{pdf_path} has been deleted.")

async def process_directory(category: str):
    data_dir = Path(f'data/{category}')
    if not data_dir.exists():
        return f"Directory not found: {data_dir}"

    pdf_files = list(data_dir.glob('**/*.pdf')) + list(data_dir.glob('**/*.PDF'))
    processed_files = []

    for pdf_path in pdf_files:
        try:
            parse_and_save(str(pdf_path))
            processed_files.append(pdf_path.name)
        except Exception as e:
            processed_files.append(f"Error processing {pdf_path.name}: {str(e)}")

    return f"Processed files: {', '.join(processed_files)}"
