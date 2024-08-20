#!/usr/bin/python3
"""this script define a class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """define class"""
    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        print("{}: {}".format(key, item))


    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
