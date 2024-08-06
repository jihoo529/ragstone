# backend/app/routers/update_db.py

from fastapi import APIRouter, File, UploadFile, HTTPException, Form
from fastapi.responses import JSONResponse, FileResponse
from typing import List
import os
import shutil
import asyncio
from ...services.chromadb.populate_db import populate_database
from app.db.mongo import MongoKeyValueDB
router = APIRouter()

UPLOAD_DIR = "data"

@router.post("/upload")
async def upload_files(files: List[UploadFile] = File(...), category: str = Form(...)):
    saved_files = []

    try:
        # Create a directory for the category if it doesn't exist
        category_dir = os.path.join(UPLOAD_DIR, category)
        os.makedirs(category_dir, exist_ok=True)
        
        for file in files:
            file_path = os.path.join(category_dir, file.filename)
            
            # Check if file already exists
            if os.path.exists(file_path):
                return HTTPException(status_code=400, detail=f"File {file.filename} already exists")
            
            # Save the file
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            saved_files.append(file.filename)
        
        return JSONResponse(content={
            "message": f"Successfully uploaded {len(saved_files)} files",
            "files": saved_files
        })

    except HTTPException as he:
        # If it's an HTTPException (like file already exists), re-raise it
        raise he
    except Exception as e:
        # If an error occurs, attempt to delete any files that were saved
        for filename in saved_files:
            file_path = os.path.join(category_dir, filename)
            if os.path.exists(file_path):
                os.remove(file_path)
        
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/download/{category}/{file_name}")
async def download_file(category: str, file_name: str):
    file_path = os.path.join(UPLOAD_DIR, category, file_name)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, filename=file_name, media_type='application/octet-stream')

@router.delete("/delete/{category}/{file_name}")
async def delete_file(category: str, file_name: str):
    file_path = os.path.join(UPLOAD_DIR, category, file_name)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    try:
        os.remove(file_path)
        return {"message": f"File {file_name} has been deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while deleting the file: {str(e)}")
    
@router.get("/files/{category}")
async def list_files(category: str):
    category_dir = os.path.join("./data", category)

    if not os.path.exists(category_dir):
        return JSONResponse(content=[])
    
    files = os.listdir(category_dir)
    print(files)

    with MongoKeyValueDB() as db:
        file_statuses = []
        
        for file in files:
            key = f'/app/data/{category}/{file}'
            result = db.get(key)
            is_populated = result.get('is_populated', False) if result else False

            file_statuses.append({
                "name": file,
                "category": category,
                "inChroma": is_populated
            })
    print(f"FILE STATUS: {file_statuses}")
    return JSONResponse(content=file_statuses)
