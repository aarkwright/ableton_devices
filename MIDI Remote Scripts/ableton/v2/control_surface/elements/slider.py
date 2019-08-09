# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\elements\slider.py
# Compiled at: 2019-05-15 03:17:58
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ..input_control_element import MIDI_NOTE_TYPE
from .encoder import EncoderElement

class SliderElement(EncoderElement):
    """ Class representing a slider on the controller """

    def __init__(self, msg_type, channel, identifier, *a, **k):
        assert msg_type is not MIDI_NOTE_TYPE
        super(SliderElement, self).__init__(msg_type, channel, identifier, map_mode=Live.MidiMap.MapMode.absolute, *a, **k)