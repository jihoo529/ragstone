# app/api/endpoints/populate_db.py
from fastapi import APIRouter, WebSocket, HTTPException
from app.services.chromadb.populate_db import populate_database, clear_database as celar_db_service
from app.utils.to_markdown import process_directory
import asyncio
import logging
from pathlib import Path
import shutil

router = APIRouter()
logger = logging.getLogger(__name__)

@router.websocket("/ws/populate_db/{category}")
async def websocket_populate_db(websocket: WebSocket, category: str):
    await websocket.accept()
    logger.info(f"WebSocket connection accepted for category: {category}")

    async def progress_callback(message: str):
        await websocket.send_text(message)
        logger.info(f"Sent progress message for category {category}: {message}")

    try:
        await populate_database(category, progress_callback)
        await websocket.send_text("Database population completed successfully.")
    except Exception as e:
        error_message = f"Error: {str(e)}"
        logger.error(f"Error in WebSocket connection for category {category}: {error_message}")
        await websocket.send_text(error_message)
    finally:
        logger.info(f"WebSocket connection closed for category: {category}")
        await websocket.close()

@router.get("/clear-database/{category}")
async def clear_chroma_database(category: str):
    chroma_path = Path(f"chroma/{category}")
    
    if chroma_path.exists() and chroma_path.is_dir():
        try:
            await celar_db_service(category)
            return {"success": True, "message": f"Database for category '{category}' has been cleared."}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred while clearing the database: {str(e)}")
    else:
        return {"success": False, "message": f"Database for category '{category}' does not exist."}

@router.get("/convert-markdown/{category}")
async def convert_markdown(category: str):
    try:
        result = await process_directory(category)
        return {"success": True, "message": f"Markdown conversion for category '{category}' completed successfully.", "result": result}
    except Exception as e:
        logger.error(f"Error in markdown conversion for category {category}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An error occurred during markdown conversion: {str(e)}")
