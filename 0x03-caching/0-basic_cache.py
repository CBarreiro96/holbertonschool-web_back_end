#!/usr/bin/env python3

"""
Exercise:
Basic dictionary
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ class Base dictionary """

    def put(self, key, item):
        """ FUnction Puts itew in cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Function get item from cache"""
        return self.cache_data.get(key, None)
