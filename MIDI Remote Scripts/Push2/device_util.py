# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\device_util.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.base import liveobj_valid

def is_drum_pad(item):
    return liveobj_valid(item) and isinstance(item, Live.DrumPad.DrumPad)


def find_chain_or_track(item):
    """
    Finds a chain for the given item.
    - If it's a device, returns the parent chain or track
    - If it's a drum pad, returns the first chain if it exists, otherwise also the parent
      chain or track
    """
    if is_drum_pad(item) and item.chains:
        chain = item.chains[0]
    else:
        chain = item
        while liveobj_valid(chain) and not isinstance(chain, (Live.Track.Track, Live.Chain.Chain)):
            chain = getattr(chain, b'canonical_parent', None)

    return chain


def find_rack(item):
    """
    Finds the parent rack of the given item or None, if it doesn't exist
    """
    rack = item
    while liveobj_valid(rack) and not isinstance(rack, Live.RackDevice.RackDevice):
        rack = getattr(rack, b'canonical_parent', None)

    return rack