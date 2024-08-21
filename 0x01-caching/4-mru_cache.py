#!/usr/bin/env python3
"""this script define a class"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
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
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                m_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", m_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, False)

    def get(self, key):
        """get an item"""
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data[key]
        self.cache_data.move_to_end(key, False)
        return value
