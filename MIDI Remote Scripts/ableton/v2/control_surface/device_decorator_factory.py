# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\device_decorator_factory.py
# Compiled at: 2019-05-10 18:21:20
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import liveobj_valid
from ableton.v2.control_surface import DecoratorFactory
from .delay_decoration import DelayDeviceDecorator
from .simpler_decoration import SimplerDeviceDecorator
from .wavetable_decoration import WavetableDeviceDecorator

class DeviceDecoratorFactory(DecoratorFactory):
    DECORATOR_CLASSES = {b'Delay': DelayDeviceDecorator, 
       b'OriginalSimpler': SimplerDeviceDecorator, 
       b'InstrumentVector': WavetableDeviceDecorator}

    @classmethod
    def generate_decorated_device(cls, device, additional_properties={}, song=None, *a, **k):
        decorated = cls.DECORATOR_CLASSES[device.class_name](live_object=device, additional_properties=additional_properties, *a, **k)
        return decorated

    @classmethod
    def _should_be_decorated(cls, device):
        return liveobj_valid(device) and device.class_name in cls.DECORATOR_CLASSES

    def _get_decorated_object(self, device, additional_properties, song=None, *a, **k):
        return self.generate_decorated_device(device, additional_properties=additional_properties, *a, **k)