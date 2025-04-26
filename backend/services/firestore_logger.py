from firebase_config import db
from datetime import datetime

def log_emotion(user_id: str, emotion_type: str, source: str, raw_input: str):
    try:
        entry = {
            "user_id": user_id,
            "emotion": emotion_type,
            "source": source,
            "timestamp": datetime.utcnow(),
            "raw_input": raw_input
        }
        db.collection("emotion_logs").add(entry)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
