# core/groq_api.py

import os
import requests
from typing import List, Dict
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_BASE_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = os.getenv("GROQ_TEXT_MODEL", "llama3-70b-8192")

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def generate_chat_response(messages: List[Dict[str, str]]) -> str:
    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7,
        "top_p": 0.95,
        "stream": False
    }

    try:
        response = requests.post(GROQ_BASE_URL, headers=HEADERS, json=payload)

        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            return reply.strip()
        else:
            print("Groq API Error:", response.status_code, response.text)
            return f"Groq API Error {response.status_code}: {response.text}"

    except Exception as e:
        print("Exception during Groq API call:", str(e))
        return f"Exception: {str(e)}"


# Example usage (optional)
if __name__ == "__main__":
    test_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
    print("Bot reply:", generate_chat_response(test_messages))
