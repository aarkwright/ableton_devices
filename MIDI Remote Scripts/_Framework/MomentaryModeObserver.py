# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\MomentaryModeObserver.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
from . import Defaults

class MomentaryModeObserver(object):
    """ Listens to the changes of a given set of controls and decides which mode to use """

    def __init__(self):
        object.__init__(self)
        self._controls = None
        self._mode_callback = None
        self._reset()
        return

    def disconnect(self):
        self._reset()

    def set_mode_details(self, base_mode, controls, mode_callback=None):
        assert isinstance(base_mode, int)
        assert isinstance(controls, (type(None), tuple))
        assert mode_callback == None or callable(mode_callback)
        self._reset()
        if controls != None:
            self._controls = controls
            for control in self._controls:
                control.add_value_listener(self._control_changed)

        self._base_mode = base_mode
        self._mode_callback = mode_callback
        return

    def is_mode_momentary(self):
        return self._controls_changed or self._timer_count >= Defaults.MOMENTARY_DELAY_TICKS

    def on_timer(self):
        self._timer_count += 1

    def _control_changed(self, value):
        if self._mode_callback == None or self._mode_callback() == self._base_mode:
            self._controls_changed = True
        return

    def _release_controls(self):
        if self._controls != None:
            for control in self._controls:
                control.remove_value_listener(self._control_changed)

            self._controls = None
        return

    def _reset(self):
        self._base_mode = -1
        self._controls_changed = False
        self._mode_callback = None
        self._timer_count = 0
        self._release_controls()
        return