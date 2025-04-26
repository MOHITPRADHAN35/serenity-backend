from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class EmotionInput(BaseModel):
    emotion: str

@router.post("/")
async def respond_to_emotion(payload: EmotionInput):
    emotion = payload.emotion.lower()

    if emotion == "happy":
        reply = "I'm glad you're feeling great! Keep it up ☀️"
    elif emotion == "sad":
        reply = "I'm here for you. Want to talk about it?"
    elif emotion == "angry":
        reply = "Take a deep breath. I'm with you."
    else:
        reply = "I'm here to support you no matter how you feel."

    return {"response": reply}
