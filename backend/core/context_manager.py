# core/context_manager.py

from typing import Dict

class ContextManager:
    """
    Dynamically manages conversation context based on user dialogue.
    """

    def __init__(self, memory_manager):
        self.memory_manager = memory_manager

    def update_context(self, user_id: str, user_message: str) -> None:
        keywords = ["my", "i am", "i'm", "i have", "i lost", "i love", "i hate", "i miss", "i feel"]
        lowered_message = user_message.lower()

        if any(kw in lowered_message for kw in keywords):
            key = self._generate_key_from_message(user_message)
            if key:
                self.memory_manager.update(user_id, key, user_message)

    def get_context(self, user_id: str) -> Dict[str, str]:
        return self.memory_manager.all_memory(user_id)

    def _generate_key_from_message(self, message: str) -> str:
        if "name" in message.lower():
            return "user_name"
        elif "ex" in message.lower():
            return "ex_relationship"
        elif "feel" in message.lower():
            return "feelings"
        elif "lost" in message.lower():
            return "loss"
        else:
            return "general_info"
