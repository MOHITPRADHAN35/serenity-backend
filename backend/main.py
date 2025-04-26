import os
import sys
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from services.facial_emotion_detection.face_emotion_detection import detect_emotions_in_frame
from routers import chatbot


# Add the root project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify your frontend URL instead of "*" in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for chatbot input
class ChatRequest(BaseModel):
    message: str

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Emotion Detection and Chatbot API"}

# Endpoint to start real-time emotion detection
@app.post("/detect_emotion/")
async def detect_emotion(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        result = detect_emotions_in_frame(contents)
        return result
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

# ✅ NEW: Chatbot with memory + context using LLaMA
app.include_router(chatbot.router, prefix="/api", tags=["chatbot"])
