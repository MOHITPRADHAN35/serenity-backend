# routers/chatbot.py

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict,Optional
from core.emotion_detector import detect_emotion
from core.memory import MemoryManager
from core.context_manager import ContextManager
from core.groq_api import generate_chat_response

router = APIRouter()

# Global memory (optional: replace with per-user memory in prod)
memory = MemoryManager()
context = ContextManager(memory)

class ChatRequest(BaseModel):
    message: str
    user_id: Optional[str] = None  # 👈 Added this line

@router.post("/chat")
async def chat_handler(request: ChatRequest):
    user_input = request.message
    user_id = request.user_id or "default_user"  # fallback if user_id is not sent

    # Step 1: Update context with user id + message
    context.update_context(user_id, user_input)

    # Step 2: Prepare message history
    context_data = context.get_context(user_id)
    system_prompt = """
    You are Serenity, a warm and supportive mental wellness assistant.
    Try to remember what's important to the user. Be empathetic, never judgmental.
    Use helpful, kind, short messages. Context you know so far:
    """
    for k, v in context_data.items():
        system_prompt += f"\n- {k}: {v}"

    messages: List[Dict[str, str]] = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    # Step 3: Send to LLaMA API
    reply = generate_chat_response(messages)

    return {"reply": reply}
