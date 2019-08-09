# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\mixable_utilities.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.control_surface import find_instrument_meeting_requirement

def is_chain(track_or_chain):
    return isinstance(getattr(track_or_chain, b'proxied_object', track_or_chain), Live.Chain.Chain)


def is_midi_track(track):
    return getattr(track, b'has_midi_input', False) and not is_chain(track)


def is_audio_track(track):
    return getattr(track, b'has_audio_input', False) and not is_chain(track)


def can_play_clips(mixable):
    return hasattr(mixable, b'fired_slot_index')


def find_drum_rack_instrument(track):
    return find_instrument_meeting_requirement(lambda i: i.can_have_drum_pads, track)


def find_simpler(track_or_chain):
    return find_instrument_meeting_requirement(lambda i: hasattr(i, b'playback_mode'), track_or_chain)