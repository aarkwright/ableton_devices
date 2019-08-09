# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\defaults.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals
TIMER_DELAY = 0.1
MOMENTARY_DELAY = 0.3
MOMENTARY_DELAY_TICKS = int(MOMENTARY_DELAY / TIMER_DELAY)
DOUBLE_CLICK_DELAY = 0.5