# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\master_track.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import listens
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.control import ToggleButtonControl

class MasterTrackComponent(Component):
    toggle_button = ToggleButtonControl()

    def __init__(self, tracks_provider=None, *a, **k):
        assert tracks_provider is not None
        super(MasterTrackComponent, self).__init__(*a, **k)
        self._tracks_provider = tracks_provider
        self.__on_selected_item_changed.subject = self._tracks_provider
        self._previous_selection = self._tracks_provider.selected_item
        self._update_button_state()
        return

    @listens(b'selected_item')
    def __on_selected_item_changed(self, *a):
        self._update_button_state()
        if not self._is_on_master():
            self._previous_selection = self._tracks_provider.selected_item

    def _update_button_state(self):
        self.toggle_button.is_toggled = self._is_on_master()

    @toggle_button.toggled
    def toggle_button(self, toggled, button):
        if toggled:
            self._previous_selection = self._tracks_provider.selected_item
            self._tracks_provider.selected_item = self.song.master_track
        else:
            self._tracks_provider.selected_item = self._previous_selection
        self._update_button_state()

    def _is_on_master(self):
        return self._tracks_provider.selected_item == self.song.master_track