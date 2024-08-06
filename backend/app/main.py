# backend/app/main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.api.endpoints import chat
from app.api.endpoints import upload_rfp
from app.api.endpoints import file_operations
from app.api.endpoints import update_database
from app.api.endpoints import settings
from app.api.endpoints import user
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_messages = []
    for error in exc.errors():
        error_messages.append({
            "loc": error.get("loc", []),
            "msg": error.get("msg", ""),
            "type": error.get("type", "")
        })
    
    return JSONResponse(
        status_code=422,
        content={
            "detail": "Validation Error",
            "errors": error_messages
        }
    )
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your Vue.js app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api")
app.include_router(upload_rfp.router, prefix="/api")
app.include_router(file_operations.router, prefix="/api")
app.include_router(update_database.router, prefix="/api")
app.include_router(settings.router, prefix='/api')
app.include_router(user.router, prefix='/api')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)