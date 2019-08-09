# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\control\sysex.py
# Compiled at: 2019-05-15 03:17:58
from __future__ import absolute_import, print_function, unicode_literals
from .control import Control, control_color

class ColorSysexControl(Control):

    class State(Control.State):
        color = control_color(b'DefaultButton.Disabled')

        def set_control_element(self, control_element):
            super(ColorSysexControl.State, self).set_control_element(control_element)
            self._send_current_color()

        def update(self):
            super(ColorSysexControl.State, self).update()
            self._send_current_color()

        def _send_current_color(self):
            if self._control_element:
                self._control_element.set_light(self.color)