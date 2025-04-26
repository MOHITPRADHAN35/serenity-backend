# models/memory_model.py

from pydantic import BaseModel
from typing import Optional

class MemoryItem(BaseModel):
    key: str
    value: str
    user_id: Optional[str] = None  # Optional, for multi-user support
