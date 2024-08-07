from pydantic import BaseModel
from typing import List

class UserSettings(BaseModel):
    category_settings: List[str]

class PromptSettings(BaseModel):
    model: str
    chunk_size: int
    chunk_overlap: int
    prompt_template: str