from pydantic import BaseModel
from typing import List, Dict

class ChatRequest(BaseModel):
    messages: List[Dict[str, str]]  # [{"role": "user", "content": "Hi"}, ...]

class EmotionRequest(BaseModel):
    text: str

class EmotionResponse(BaseModel):
    emotion: str
    confidence: float
