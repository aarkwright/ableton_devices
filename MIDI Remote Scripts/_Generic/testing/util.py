# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Generic\testing\util.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.base import const, nop
from ableton.v2.testing import count_calls

class MockControlSurface(object):
    instance_identifier = const(0)
    request_rebuild_midi_map = count_calls()
    show_message = nop
    send_midi = nop

    def __init__(self, *a, **k):
        super(MockControlSurface, self).__init__(*a, **k)
        self._song = Live.Song.Song(num_tracks=4, num_returns=2)

    def song(self):
        return self._song