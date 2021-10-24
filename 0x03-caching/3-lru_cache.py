#!/usr/bin/env python3
"""
Exercise:
LIFO Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching """

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
            first = self.get_first_list(self.queue_lists)
            if first:
                self.queue_lists.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

        if key not in self.queue_lists:
            self.queue_lists.append(key)
        else:
            self.mv_last_list(key)

    def get(self, key):
        """ Gets item from cache """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.mv_last_list(key)
        return item

    def mv_last_list(self, item):
        """ Moves element to last idx of list """
        length = len(self.queue_lists)
        if self.queue_lists[length - 1] != item:
            self.queue_lists.remove(item)
            self.queue_lists.append(item)

    @staticmethod
    def get_first_list(array):
        "Get first element of list or none"
        return array[0] if array else None
