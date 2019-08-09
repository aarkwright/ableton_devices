# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\elements\velocity_levels_element.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals
from ...base import EventObject, listenable_property
from .proxy_element import ProxyElement

class NullVelocityLevels(EventObject):
    enabled = False
    target_note = -1
    target_channel = -1
    source_channel = -1
    notes = []

    @property
    def levels(self):
        return []

    @listenable_property
    def last_played_level(self):
        return -1.0


class VelocityLevelsElement(ProxyElement):

    def __init__(self, velocity_levels=None, *a, **k):
        super(VelocityLevelsElement, self).__init__(proxied_object=velocity_levels, proxied_interface=NullVelocityLevels())

    def reset(self):
        self.notes = []
        self.source_channel = -1