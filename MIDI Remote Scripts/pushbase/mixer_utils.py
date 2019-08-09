# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\mixer_utils.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals
import Live

def is_set_to_split_stereo(mixer):
    modes = Live.MixerDevice.MixerDevice.panning_modes
    return modes.stereo_split == getattr(mixer, b'panning_mode', modes.stereo)


def has_pan_mode(mixer):
    return hasattr(mixer, b'panning_mode')