#!/usr/bin/python3
""" BaseCaching module
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
class BasicCache(BaseCaching):
    """define class"""
    def __init__(self):
        """Initiliaze"""
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Add an item in the cache"""
        self.cache_data[key] = item
        print("{}: {}".format(key,item))
        if key is None or item is None:
            pass

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None
        return self.cache_data.get(key)
