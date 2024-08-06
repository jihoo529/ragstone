from fastapi import APIRouter, File, UploadFile, Form, HTTPException, Depends
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse
import io
import os
import shutil
import pandas as pd
from typing import List
from pathlib import Path
from app.services.chat_service import ChatService, get_chat_service
from app.services.rfp_service import RFPService
import json
import asyncio

router = APIRouter()

# UPLOAD_DIR = "../../../tmp/"

# Ensure the upload directory exists


import logging

logger = logging.getLogger(__name__)


@router.post("/upload-rfp/{category}")
async def upload_rfp(category: str, files: List[UploadFile] = File(...), chat_service: ChatService = Depends(get_chat_service)):
    try:
        rfp_data = RFPService.process_rfp(files[0])
        total_queries = len(rfp_data["queries"]["Questions"])

        async def process_queries():
            processed_queries = {"Questions": {}, "Answers": {}, "Sources": {}}
            
            async def process_single_query(q_id, question):
                result = await chat_service.process_rag_query(question, category)
                return q_id, question, result

            tasks = [process_single_query(q_id, question) 
                     for q_id, question in rfp_data["queries"]["Questions"].items()]
            
            for i, completed_task in enumerate(asyncio.as_completed(tasks)):
                q_id, question, result = await completed_task
                processed_queries["Questions"][q_id] = question
                processed_queries["Answers"][q_id] = result["response"]
                processed_queries["Sources"][q_id] = result["sources"]
                
                progress = {
                    "current": i + 1,
                    "total": total_queries,
                    "percentage": round(((i + 1) / total_queries) * 100, 2)
                }
                yield f"data: {json.dumps({'progress': progress})}\n\n"

            output_rfp = RFPService.json_to_xl(processed_queries)
            filename = f"processed_rfp_{category}.xlsx"
            
            yield f"data: {json.dumps({'file_ready': True, 'filename': filename})}\n\n"

            with open(f"/tmp/{filename}", "wb") as f:
                f.write(output_rfp.getvalue())

        return StreamingResponse(process_queries(), media_type="text/event-stream")

    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get-processed-file/{category}/{filename}")
async def get_processed_file(category: str, filename: str):
    file_path = f"/tmp/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path, filename=filename, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    else:
        raise HTTPException(status_code=404, detail="File not found")