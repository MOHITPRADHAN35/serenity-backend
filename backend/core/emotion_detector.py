# core/emotion_detector.py

from typing import Optional

def detect_emotion(text: str) -> Optional[str]:
    """
    Very basic emotion detector based on keyword matching.
    You can later upgrade this with a ML model.
    """
    text = text.lower()

    if any(word in text for word in ["happy", "glad", "joy", "excited", "grateful"]):
        return "happy"
    elif any(word in text for word in ["sad", "down", "depressed", "cry", "upset"]):
        return "sad"
    elif any(word in text for word in ["angry", "mad", "furious", "annoyed"]):
        return "angry"
    elif any(word in text for word in ["anxious", "nervous", "worried", "scared"]):
        return "anxious"
    elif any(word in text for word in ["lonely", "alone", "isolated"]):
        return "lonely"
    elif any(word in text for word in ["hopeful", "optimistic", "looking forward"]):
        return "hopeful"
    else:
        return "neutral"
