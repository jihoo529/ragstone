from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List
import aiofiles
import os
import shutil
import pymongo
import logging
import traceback
from pymongo.collection import Collection
from typing import Dict, Any

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

router = APIRouter()

MONGO_CONNECTION_STRING = "mongodb://mongodb:27017"
DB_NAME = "ragstone"
COLLECTION_NAME = "settings"


client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

PROMPT_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "utils", "prompt.txt")
DATA_FOLDER_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "data")

class UserSettings(BaseModel):
    category_settings: List[str]

class PromptSettings(BaseModel):
    model: str
    chunk_size: int
    chunk_overlap: int
    prompt_template: str

@router.get("/settings", response_model=UserSettings)
def get_user_settings():
    try:
        # Get all subdirectories in the DATA_FOLDER_PATH
        category_list = [d for d in os.listdir(DATA_FOLDER_PATH) if os.path.isdir(os.path.join(DATA_FOLDER_PATH, d))]
        
        # Sort the list alphabetically
        category_list.sort()
        
        return UserSettings(category_settings=category_list)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading data folder: {str(e)}")

@router.put("/settings", response_model=UserSettings)
def update_user_settings(settings: UserSettings):
    try:
        # Get the current settings (folders)
        current_category_settings = set(d for d in os.listdir(DATA_FOLDER_PATH) if os.path.isdir(os.path.join(DATA_FOLDER_PATH, d)))
        new_category_settings = set(settings.category_settings)

        # Identify added and removed category settings
        added_category = new_category_settings - current_category_settings
        removed_category = current_category_settings - new_category_settings

        # Create folders for new category settings
        for category in added_category:
            folder_path = os.path.join(DATA_FOLDER_PATH, category)
            os.makedirs(folder_path, exist_ok=True)

        # Remove folders for deleted category settings
        for category in removed_category:
            folder_path = os.path.join(DATA_FOLDER_PATH, category)
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)

        return settings
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating settings: {str(e)}")
    
def read_prompt_template():
    try:
        logger.debug("Attempting to read prompt template from database")
        document = collection.find_one({
            "model": {"$exists": True},
            "chunk_size": {"$exists": True},
            "chunk_overlap": {"$exists": True},
            "prompt_template": {"$exists": True}
        })
        logger.debug(f"Query result: {document}")
        
        if document:
            logger.info("Document found in database")
            return PromptSettings(
                model = document["model"],
                chunk_size=document["chunk_size"],
                chunk_overlap=document["chunk_overlap"],
                prompt_template=document["prompt_template"]
            )
        else:
            logger.warning("No document found matching the query")
            return {"error": "No document found"}
    except Exception as e:
        logger.error(f"Error reading prompt template from database: {str(e)}")
        logger.error(traceback.format_exc())
        return {"error": str(e), "traceback": traceback.format_exc()}
    
def write_prompt_template(collection: Collection, data: PromptSettings):
    try:
        result = collection.update_one(
            {
                "model": {"$exists": True},
                "chunk_size": {"$exists": True},
                "chunk_overlap": {"$exists": True},
                "prompt_template": {"$exists": True}
            },
            {"$set": data.dict()},
            upsert=True
        )
        if result.modified_count == 0:
            raise HTTPException(status_code=400, detail="No changes made to the prompt template")
        return {"message": "Prompt template updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error writing prompt template to database: {str(e)}")
    
@router.get("/prompt", response_model=PromptSettings)
def get_prompt():
    return read_prompt_template()

@router.post("/prompt", response_model=PromptSettings)
def update_prompt(prompt: PromptSettings):
    write_prompt_template(collection, prompt)
    return prompt