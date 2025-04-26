# core/memory.py

from typing import Dict, Optional

class MemoryManager:
    """
    A simple multi-user memory manager.
    """

    def __init__(self):
        self.user_memories: Dict[str, Dict[str, str]] = {}

    def update(self, user_id: str, key: str, value: str) -> None:
        """Update or add a memory item for a specific user."""
        if user_id not in self.user_memories:
            self.user_memories[user_id] = {}
        self.user_memories[user_id][key.lower()] = value

    def get(self, user_id: str, key: str) -> Optional[str]:
        """Retrieve a memory item for a specific user."""
        return self.user_memories.get(user_id, {}).get(key.lower())

    def delete(self, user_id: str, key: str) -> None:
        """Delete a memory item for a specific user."""
        if user_id in self.user_memories and key.lower() in self.user_memories[user_id]:
            del self.user_memories[user_id][key.lower()]

    def clear(self, user_id: str) -> None:
        """Clear all memory for a specific user."""
        if user_id in self.user_memories:
            self.user_memories[user_id] = {}

    def all_memory(self, user_id: str) -> Dict[str, str]:
        """Return all stored memory for a specific user."""
        return self.user_memories.get(user_id, {})
