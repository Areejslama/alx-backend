#!/usr/bin/env python3
"""this script define a class"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """define class"""
    def __init__(self):
        """intialize"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put an item"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                r_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", r_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """get an item"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
