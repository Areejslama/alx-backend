#!/usr/bin/env python3
"""this script define a class"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """define class"""
    def __init__(self):
        """initializ"""
        super().__init__()

    def put(self, key, item):
        """put values in dictionary"""
        self.cache_data[key] = item
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD: ", first_key)

    def get(self, key):
        """get the items"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
