from fastapi import APIRouter, HTTPException
import os
import shutil
from ...schemas.setting_schemas import UserSettings, PromptSettings
from ...services.setting_service import *

router = APIRouter()

DATA_FOLDER_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "data")

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
    

    
@router.get("/prompt", response_model=PromptSettings)
def get_prompt():
    return read_prompt_template()

@router.post("/prompt", response_model=PromptSettings)
def update_prompt(prompt: PromptSettings):
    write_prompt_template(collection, prompt)
    return prompt