# backend/app/schemas/chat_schemas.py
from typing import List
from pydantic import BaseModel

class ChatMessage(BaseModel):
    message: str
    category: str

class ChatResponse(BaseModel):
    response: str
    sources: List[str]