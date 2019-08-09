# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\control\radio_button.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals
from ...base import nop
from .control import control_event, control_color
from .button import ButtonControlBase

class RadioButtonControl(ButtonControlBase):
    checked = control_event(b'checked')

    class State(ButtonControlBase.State):
        unchecked_color = control_color(b'DefaultButton.Off')
        checked_color = control_color(b'DefaultButton.On')

        def __init__(self, unchecked_color=None, checked_color=None, *a, **k):
            super(RadioButtonControl.State, self).__init__(*a, **k)
            if unchecked_color is not None:
                self.unchecked_color = unchecked_color
            if checked_color is not None:
                self.checked_color = checked_color
            self._checked = False
            self._on_checked = nop
            return

        @property
        def is_checked(self):
            return self._checked

        @is_checked.setter
        def is_checked(self, value):
            if self._checked != value:
                self._checked = value
                if self._checked:
                    self._on_checked()
                self._send_current_color()

        def _send_button_color(self):
            self._control_element.set_light(self.checked_color if self._checked else self.unchecked_color)

        def _on_pressed(self):
            super(RadioButtonControl.State, self)._on_pressed()
            if not self._checked:
                self._checked = True
                self._notify_checked()

        def _notify_checked(self):
            if self._checked:
                self._call_listener(b'checked')
                self._on_checked()