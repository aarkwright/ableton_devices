# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\LogicalDisplaySegment.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals

class LogicalDisplaySegment(object):
    """
    Class representing a specific segment of a display on the controller
    """
    separator = b''

    def __init__(self, width=None, update_callback=None, *a, **k):
        super(LogicalDisplaySegment, self).__init__(*a, **k)
        assert width is not None
        assert callable(update_callback)
        self._update_callback = update_callback
        self._width = width
        self._position_identifier = ()
        self._data_source = None
        self._display_string = None
        return

    def disconnect(self):
        self._update_callback = None
        self._position_identifier = None
        if self._data_source != None:
            self._data_source.set_update_callback(None)
            self._data_source = None
        return

    def set_data_source(self, data_source):
        if self._data_source != None:
            self._data_source.set_update_callback(None)
        self._data_source = data_source
        if self._data_source != None:
            self._data_source.set_update_callback(self.update)
        self._display_string = self._get_display_string()
        return

    def data_source(self):
        return self._data_source

    def set_position_identifier(self, position_identifier):
        """
        Sets position identifier as a tuple of HW related data.
        """
        self._position_identifier = position_identifier

    def position_identifier(self):
        return self._position_identifier

    def update(self):
        if self._update_callback:
            self._display_string = self._get_display_string()
            self._update_callback()

    def _get_display_string(self):
        if self._data_source != None:
            separator = self._data_source.separator + self.separator
            width = self._width - len(separator)
            assert width >= 0
            return self._data_source.adjust_string(width) + separator
        else:
            return b' ' * self._width
            return

    def display_string(self):
        if self._display_string is None:
            self._display_string = self._get_display_string()
        return self._display_string

    def __str__(self):
        return self.display_string()