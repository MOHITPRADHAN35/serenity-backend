# core/groq_api.py

import os
import requests
from typing import List, Dict
from dotenv import load_dotenv  # 🆕

load_dotenv()  # 🆕 Load .env variables early

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_BASE_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = os.getenv("GROQ_TEXT_MODEL", "llama3-70b-819")

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def generate_chat_response(messages: List[Dict[str, str]]) -> str:
    """
    Calls the Groq API with a list of messages [{role: user/assistant, content: text}, ...]
    Returns the assistant's reply as a string.
    """
    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7,
        "top_p": 0.95,
        "stream": False
    }

    response = requests.post(GROQ_BASE_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        return reply.strip()
    else:
        print("Groq API Error:", response.text)
        return "Sorry, I had trouble thinking clearly just now. Can you try again?"


# Example usage (for dev testing)
if __name__ == "__main__":
    test_messages = [
        {"role": "system", "content": "You are Serenity, a supportive mental wellness assistant."},
        {"role": "user", "content": "Hi, I'm feeling kinda low today."}
    ]
    reply = generate_chat_response(test_messages)
    print("Bot:", reply)
