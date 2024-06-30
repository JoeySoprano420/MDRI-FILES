class MemoryManager:
    def __init__(self):
        self.cache = {}

    def get_cached_object(self, key):
        return self.cache.get(key)

    def cache_object(self, key, obj):
        self.cache[key] = obj

    def clear_cache(self):
        self.cache.clear()

memory_manager = MemoryManager()
