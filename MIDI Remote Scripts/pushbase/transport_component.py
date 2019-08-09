# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\transport_component.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import components

class TransportComponent(components.TransportComponent):

    def __init__(self, *a, **k):
        super(TransportComponent, self).__init__(*a, **k)
        self._metronome_toggle.view_transform = lambda v: b'Metronome.On' if v else b'Metronome.Off'