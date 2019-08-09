# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\elements\playhead_element.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals
from ...base import nop
from .proxy_element import ProxyElement

class NullPlayhead(object):
    notes = []
    start_time = 0.0
    step_length = 1.0
    velocity = 0.0
    wrap_around = False
    track = None
    clip = None
    set_feedback_channels = nop


class PlayheadElement(ProxyElement):

    def __init__(self, playhead=None, *a, **k):
        super(PlayheadElement, self).__init__(proxied_object=playhead, proxied_interface=NullPlayhead())

    def reset(self):
        self.track = None
        return