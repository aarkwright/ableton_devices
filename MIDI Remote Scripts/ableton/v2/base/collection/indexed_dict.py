# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\base\collection\indexed_dict.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals
from collections import OrderedDict

class IndexedDict(OrderedDict):
    """ Dictionary whose values are accessible by indices """

    def __init__(self, *args, **kwds):
        self.__keys = []
        super(IndexedDict, self).__init__(*args, **kwds)

    def __setitem__(self, key, value, *args, **kwds):
        super(IndexedDict, self).__setitem__(key, value, *args, **kwds)
        self.__keys.append(key)

    def __delitem__(self, key, *args, **kwds):
        super(IndexedDict, self).__delitem__(key, *args, **kwds)
        self.__keys.remove(key)

    def clear(self):
        super(IndexedDict, self).clear()
        self.__keys = []

    def popitem(self, last=True):
        item = super(IndexedDict, self).popitem(last)
        self.__keys.pop(-1 if last else 0)
        return item

    def keys(self):
        return self.__keys

    def item_by_index(self, ix):
        """ Returns (key, value) pair for given index """
        key = self.__keys[ix]
        return (
         key, self[key])

    def key_by_index(self, ix):
        """ Returns key for given index """
        return self.__keys[ix]

    def value_by_index(self, ix):
        """ Returns value for given index """
        return self[self.__keys[ix]]

    def index_by_key(self, key):
        """ Returns index of the given key """
        return self.__keys.index(key)