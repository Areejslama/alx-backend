#!/usr/bin/env python3
"""this script define a class"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ FIFO Cache"""
    def __init__(self):
        """intialize"""
        super().__init__()
        self.cache_data = OrderedDict()


    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return
        
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD: ", last_key)

    def get(self, key):
        """ Retrieve an item"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
