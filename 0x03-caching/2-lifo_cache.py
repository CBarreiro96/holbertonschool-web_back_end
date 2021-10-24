#!/usr/bin/env python3
"""
Exercise:
LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue_lists = []

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.queue_lists:
                last = self.queue_lists.pop()
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

        if key not in self.queue_lists:
            self.queue_lists.append(key)
        else:
            self.mv_last_list(key)

    def get(self, key):
        """ Gets item from cache """
        return self.cache_data.get(key, None)

    def mv_last_list(self, item):
        """ Moves element to last idx of list """
        length = len(self.queue_lists)
        if self.queue_lists[length - 1] != item:
            self.queue_lists.remove(item)
            self.queue_lists.append(item)
