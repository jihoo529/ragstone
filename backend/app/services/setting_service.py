from fastapi import HTTPException
import logging
import traceback
import pymongo
from pymongo.collection import Collection
from ..schemas.setting_schemas import PromptSettings

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

MONGO_CONNECTION_STRING = "mongodb://mongodb:27017"
DB_NAME = "ragstone"
COLLECTION_NAME = "settings"

client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

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