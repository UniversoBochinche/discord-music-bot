from typing import Dict, List, Any

class QueueManager:
    def __init__(self):
        self.queue: Dict[int, List[str]] = dict()

    def add_to_queue(self, guild_id: int, url: str):
        guild_queue = self.ensure_guild_queue(guild_id)
        guild_queue.append(url)

    def remove_from_queue(self, guild_id: int, url: str):
        guild_queue = self.ensure_guild_queue(guild_id)
        if url in guild_queue:
            guild_queue.remove(url)

    def get_next_item(self, guild_id: int) -> str | None:
        guild_queue = self.ensure_guild_queue(guild_id)
        if guild_queue:
            return guild_queue.pop(0)
        return None

    def get_queue(self, guild_id: int) -> List[str]:
        return self.ensure_guild_queue(guild_id)

    def clear_queue(self, guild_id: int):
        if self.queue[guild_id]:
            self.queue[guild_id].clear()

    def ensure_guild_queue(self, guild_id: int) -> List[str]:
        if guild_id not in self.queue:
            self.queue[guild_id] = []
        return self.queue[guild_id]