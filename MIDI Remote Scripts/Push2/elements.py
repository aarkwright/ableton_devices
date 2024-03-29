# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\elements.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.elements import SysexElement
from pushbase.control_element_factory import create_button, create_note_button
from pushbase.elements import Elements as ElementsBase
from pushbase.touch_strip_element import TouchStripElement
from .parameter_mapping_sensitivities import CONTINUOUS_MAPPING_SENSITIVITY, FINE_GRAINED_CONTINUOUS_MAPPING_SENSITIVITY
from . import sysex

class Elements(ElementsBase):

    def __init__(self, model=None, *a, **k):
        assert model is not None
        self._model = model
        super(Elements, self).__init__(continuous_mapping_sensitivity=CONTINUOUS_MAPPING_SENSITIVITY, fine_grained_continuous_mapping_sensitivity=FINE_GRAINED_CONTINUOUS_MAPPING_SENSITIVITY, *a, **k)
        for button in self.select_buttons_raw:
            button.is_rgb = True

        self.mix_button = self.single_track_mix_mode_button
        self.page_left_button = self.in_button
        self.page_left_button.name = b'Page_Left_Button'
        self.page_right_button = self.out_button
        self.page_right_button.name = b'Page_Right_Button'
        self.global_mute_button.is_rgb = True
        self.global_solo_button.is_rgb = True
        self.global_track_stop_button.is_rgb = True
        self.play_button.is_rgb = True
        self.record_button.is_rgb = True
        self.automation_button.is_rgb = True
        for button in self.side_buttons_raw:
            button.is_rgb = True

        self.convert_button = create_button(35, b'Convert')
        self.setup_button = create_button(30, b'Setup_Button')
        self.layout_button = create_button(31, b'Layout')
        self._create_touch_strip()
        self.aftertouch_control = SysexElement(send_message_generator=sysex.make_aftertouch_mode_message, default_value=b'polyphonic')
        return

    def _create_touch_strip(self):
        touch_strip_mode_element = SysexElement(send_message_generator=sysex.make_touch_strip_mode_message)
        touch_strip_light_element = SysexElement(send_message_generator=sysex.make_touch_strip_light_message)
        self.touch_strip_tap = create_note_button(12, b'Touch_Strip_Tap')
        self.touch_strip_control = TouchStripElement(name=b'Touch_Strip_Control', touch_button=self.touch_strip_tap, mode_element=touch_strip_mode_element, light_element=touch_strip_light_element)
        self.touch_strip_control.state_count = 31
        self.touch_strip_control.set_feedback_delay(-1)
        self.touch_strip_control.set_needs_takeover(False)