# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\hardware_settings_component.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.base import clamp, listens, task
from ableton.v2.control_surface import Component
LED_FADE_IN_DELAY = 0.3
LED_FADE_IN_TIME = 200
LED_FADE_IN_FREQUENCY = 16
MIN_BRIGHTNESS_FOR_FADE_IN = 0

class HardwareSettingsComponent(Component):

    def __init__(self, led_brightness_element=None, display_brightness_element=None, settings=None, *a, **k):
        assert led_brightness_element is not None
        assert display_brightness_element is not None
        assert settings is not None
        super(HardwareSettingsComponent, self).__init__(*a, **k)
        self._settings = settings
        self._led_brightness_element = led_brightness_element
        self._display_brightness_element = display_brightness_element
        self._led_brightness_timer = Live.Base.Timer(callback=self._on_fade_in_led_brightness_timer, interval=LED_FADE_IN_FREQUENCY, repeat=True)
        self._target_led_brightness = 0
        self._led_brightness = 0
        self._fade_in_delay_task = self._tasks.add(task.sequence(task.wait(LED_FADE_IN_DELAY), task.run(self._led_brightness_timer.restart))).kill()
        self.__on_led_brightness_changed.subject = settings
        self.__on_display_brightness_changed.subject = settings
        return

    def disconnect(self):
        super(HardwareSettingsComponent, self).disconnect()
        self._led_brightness_timer.stop()
        self._led_brightness_timer = None
        return

    def hardware_initialized(self):
        self.fade_in_led_brightness(self._settings.led_brightness)
        self._display_brightness_element.send_value(self._settings.display_brightness)

    def fade_in_led_brightness(self, target_brightness):
        assert MIN_BRIGHTNESS_FOR_FADE_IN <= target_brightness <= self._settings.max_led_brightness
        self._led_brightness = MIN_BRIGHTNESS_FOR_FADE_IN
        self._target_led_brightness = target_brightness
        self._led_brightness_element.send_value(MIN_BRIGHTNESS_FOR_FADE_IN)
        self._fade_in_delay_task.restart()

    def stop_fade_in_led_brightness(self):
        self._led_brightness_timer.stop()
        self._led_brightness = self._target_led_brightness = MIN_BRIGHTNESS_FOR_FADE_IN
        self._fade_in_delay_task.kill()

    def _on_fade_in_led_brightness_timer(self):
        if self._led_brightness < self._target_led_brightness:
            distance = float(self._target_led_brightness - MIN_BRIGHTNESS_FOR_FADE_IN)
            increment = distance / LED_FADE_IN_TIME * LED_FADE_IN_FREQUENCY
            self._led_brightness = clamp(self._led_brightness + increment, MIN_BRIGHTNESS_FOR_FADE_IN, self._target_led_brightness)
            self._led_brightness_element.send_value(int(round(self._led_brightness)))
        else:
            self._led_brightness_timer.stop()

    @listens(b'led_brightness')
    def __on_led_brightness_changed(self, value):
        self.stop_fade_in_led_brightness()
        self._led_brightness_element.send_value(value)

    @listens(b'display_brightness')
    def __on_display_brightness_changed(self, value):
        self._display_brightness_element.send_value(value)

    def send(self):
        self.stop_fade_in_led_brightness()
        self._led_brightness_element.send_value(self._settings.led_brightness)
        self._display_brightness_element.send_value(self._settings.display_brightness)