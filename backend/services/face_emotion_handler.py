import cv2
import numpy as np
import tempfile
from serenity.services.facial_emotion_detection.face_emotion_detection import analyze_face_emotion
  # Replace with your model function

def analyze_face_emotion(image_bytes: bytes) -> str:
    try:
        # Save image to a temp file or read it directly from bytes
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        emotion = predict_emotion(img)  # your model's prediction function
        return {
        "emotion": emotion,  # Detected emotion
        }
    except Exception as e:
        print(f"[Face Emotion Error] {e}")
        return "error"
