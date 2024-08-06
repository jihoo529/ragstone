# backend/app/routers/chat.py

from fastapi import APIRouter, Depends
from ...schemas.chat_schemas import ChatMessage, ChatResponse
from ...services.chat_service import ChatService
from typing import List

router = APIRouter()

chat_service = ChatService.get_instance(chroma_path="chroma")

def get_chat_service():
    return chat_service
    
@router.post("/chat", response_model=ChatResponse)
async def chat(message: ChatMessage, chat_service: ChatService = Depends(get_chat_service)):
    result = await chat_service.process_single_query(message)
    return result

@router.post("/chat/multiple", response_model=List[ChatResponse])
async def chat_multiple(messages: List[ChatMessage], chat_service: ChatService = Depends(get_chat_service)):
    return await chat_service.process_multiple_queries(messages)