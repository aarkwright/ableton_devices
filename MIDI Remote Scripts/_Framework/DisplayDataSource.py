# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\DisplayDataSource.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial

def adjust_string_crop(original, length):
    return original[:length].ljust(length)


def adjust_string(original, length):
    """
    Brings the string to the given length by either removing
    characters or adding spaces. The algorithm is adopted from ede's
    old implementation for the Mackie.
    """
    assert length > 0
    resulting_string = original
    if len(resulting_string) > length:
        unit_db = resulting_string.endswith(b'dB') and resulting_string.find(b'.') != -1
        if len(resulting_string.strip()) > length and unit_db:
            resulting_string = resulting_string[:-2]
        if len(resulting_string) > length:
            for char in (' ', '_', 'i', 'o', 'u', 'e', 'a'):
                offset = 0 if char == b' ' else 1
                while len(resulting_string) > length and resulting_string.rfind(char, offset) > 0:
                    char_pos = resulting_string.rfind(char, offset)
                    resulting_string = resulting_string[:char_pos] + resulting_string[char_pos + 1:]

            resulting_string = resulting_string[:length]
    if len(resulting_string) < length:
        resulting_string = resulting_string.ljust(length)
    return resulting_string


class DisplayDataSource(object):
    """
    Data object that is fed with a specific string and notifies a
    observer via its update_callback.
    """
    _separator = b''
    _adjust_string_fn = partial(adjust_string)

    def __init__(self, display_string=b'', separator=None, adjust_string_fn=adjust_string, *a, **k):
        super(DisplayDataSource, self).__init__(*a, **k)
        if adjust_string_fn is not None:
            self._adjust_string_fn = partial(adjust_string_fn)
        if separator is not None:
            self._separator = separator
        self._display_string = display_string
        self._update_callback = None
        self._in_update = False
        return

    def _get_separator(self):
        return self._separator

    def _set_separator(self, separator):
        if separator != self._separator:
            self._separator = separator
            self.update()

    separator = property(_get_separator, _set_separator)

    def set_update_callback(self, update_callback):
        assert not update_callback or callable(update_callback)
        self._update_callback = update_callback
        if update_callback:
            self.update()

    def set_display_string(self, new_string):
        if self._display_string != new_string:
            self._display_string = new_string
            self.update()

    def clear(self):
        self.set_display_string(b'')
        self.separator = b''

    def update(self):
        assert not self._in_update
        self._in_update = True
        if self._update_callback != None:
            self._update_callback()
        self._in_update = False
        return

    def display_string(self):
        return self._display_string

    def adjust_string(self, width):
        return self._adjust_string_fn(self.display_string(), width)