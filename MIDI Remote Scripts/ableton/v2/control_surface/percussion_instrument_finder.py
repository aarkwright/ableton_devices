# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\percussion_instrument_finder.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals
import Live
from itertools import chain
from ..base import EventObject, listens_group, liveobj_changed, liveobj_valid
from .device_chain_utils import find_instrument_devices, find_instrument_meeting_requirement
from .mode import Mode

class PercussionInstrumentFinder(Mode, EventObject):
    """
    Looks in the hierarchy of devices of the selected track, looking
    for the first available drum-rack or sliced simpler (depth-first),
    updating as the device list changes.
    """
    __events__ = ('instrument', )
    _drum_group = None
    _simpler = None

    def __init__(self, device_parent=None, is_enabled=True, *a, **k):
        assert liveobj_valid(device_parent)
        super(PercussionInstrumentFinder, self).__init__(*a, **k)
        self._is_enabled = is_enabled
        self._device_parent = None
        self.device_parent = device_parent
        return

    @property
    def is_enabled(self):
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, enabled):
        self._is_enabled = enabled
        self.update()

    def enter_mode(self):
        self.is_enabled = True

    def leave_mode(self):
        self.is_enabled = False

    @property
    def drum_group(self):
        """
        The latest found drum rack.
        """
        return self._drum_group

    @property
    def sliced_simpler(self):
        """
        The latest found simpler in slicing mode.
        """
        return self._simpler

    def _get_device_parent(self):
        """
        The currently observed track.
        """
        return self._device_parent

    def _set_device_parent(self, device_parent):
        if liveobj_changed(self._device_parent, device_parent):
            self._device_parent = device_parent
            self.update()

    device_parent = property(_get_device_parent, _set_device_parent)

    @listens_group(b'devices')
    def __on_devices_changed(self, chain):
        self._get_device_parent().set_data(b'alternative_mode_locked', False)
        self.update()

    @listens_group(b'chains')
    def __on_chains_changed(self, chain):
        self.update()

    @listens_group(b'playback_mode')
    def __on_slicing_changed(self, _simpler):
        self.update()

    def update(self):
        if self.is_enabled:
            self._update_listeners()
            self._update_instruments()

    def _update_listeners(self):
        device_parent = self.device_parent
        devices = list(find_instrument_devices(device_parent))
        racks = filter(lambda d: d.can_have_chains, devices)
        simplers = filter(lambda d: hasattr(d, b'playback_mode'), devices)
        chains = list(chain([device_parent], *[ d.chains for d in racks ]))
        self.__on_chains_changed.replace_subjects(racks)
        self.__on_devices_changed.replace_subjects(chains)
        self.__on_slicing_changed.replace_subjects(simplers)

    def _update_instruments(self):
        drum_group = find_drum_group_device(self.device_parent)
        simpler = find_sliced_simpler(self.device_parent)
        do_notify = liveobj_changed(drum_group, self._drum_group) or liveobj_changed(simpler, self._simpler)
        self._drum_group = drum_group
        self._simpler = simpler
        if do_notify:
            self.notify_instrument()


def find_drum_group_device(track_or_chain):
    """
    Looks up recursively for a drum_group device in the track.
    """
    requirement = lambda i: i.can_have_drum_pads
    return find_instrument_meeting_requirement(requirement, track_or_chain)


def find_sliced_simpler(track_or_chain):
    """
    Looks up recursively for a sliced simpler device in the track.
    """
    requirement = lambda i: getattr(i, b'playback_mode', None) == Live.SimplerDevice.PlaybackMode.slicing
    return find_instrument_meeting_requirement(requirement, track_or_chain)