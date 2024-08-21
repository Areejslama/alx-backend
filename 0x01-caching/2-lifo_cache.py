#!/usr/bin/env python3
"""this script define a class"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ LIFO Cache"""
    def __init__(self):
        """intialize"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ Retrieve an item"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
