#!/usr/bin/env python3

"""
Exercise:
FIFO caching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queque_lists = []

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        if key not in self.queque_lists:
            self.queque_lists.append(key)
        else:
            self.mv_last_list(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.get_first_list(self.queque_lists)
            if first:
                self.queque_lists.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """ Gets item from cache """
        return self.cache_data.get(key, None)

    def mv_last_list(self, item):
        """ Moves element to last idx of list """
        length = len(self.queque_lists)
        if self.queque_lists[length - 1] != item:
            self.queque_lists.remove(item)
            self.queque_lists.append(item)

    @staticmethod
    def get_first_list(array):
        """ Get first element of list or None """
        return array[0] if array else None
