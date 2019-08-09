# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Generic\util.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.SubjectSlot import SlotManager, subject_slot
from _Framework.Util import nop

class DeviceAppointer(SlotManager):

    def __init__(self, song=None, appointed_device_setter=nop, *a, **k):
        super(DeviceAppointer, self).__init__(*a, **k)
        self._set_appointed_device = appointed_device_setter
        self._appointed_device = None
        self._song = song
        self.__on_appointed_device_changed.subject = self._song
        self.__on_selected_track_changed.subject = self._song.view
        self.__on_selected_track_changed()
        return

    @subject_slot(b'appointed_device')
    def __on_appointed_device_changed(self):
        if self._appointed_device != self._song.appointed_device:
            self._update_appointed_device(self._song.appointed_device)

    @subject_slot(b'selected_device')
    def __on_selected_device_changed(self):
        song = self._song
        device = song.view.selected_track.view.selected_device
        if device != None:
            self._update_appointed_device(device)
        return

    @subject_slot(b'selected_track')
    def __on_selected_track_changed(self):
        track_view = self._song.view.selected_track.view
        self.__on_selected_device_changed.subject = track_view
        self._update_appointed_device(track_view.selected_device)

    def _update_appointed_device(self, device):
        if device != None:
            self._appointed_device = device
            self._set_appointed_device(device)
            self._song.appointed_device = device
        return