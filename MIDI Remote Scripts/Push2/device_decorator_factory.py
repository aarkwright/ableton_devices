# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\device_decorator_factory.py
# Compiled at: 2019-05-10 18:21:20
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import DeviceDecoratorFactory as DeviceDecoratorFactoryBase
from .auto_filter import AutoFilterDeviceDecorator
from .compressor import CompressorDeviceDecorator
from .device_decoration import SamplerDeviceDecorator, PedalDeviceDecorator, DrumBussDeviceDecorator, UtilityDeviceDecorator
from .delay import DelayDeviceDecorator
from .echo import EchoDeviceDecorator
from .eq8 import Eq8DeviceDecorator
from .operator import OperatorDeviceDecorator
from .simpler import SimplerDeviceDecorator
from .wavetable import WavetableDeviceDecorator

class DeviceDecoratorFactory(DeviceDecoratorFactoryBase):
    DECORATOR_CLASSES = {b'OriginalSimpler': SimplerDeviceDecorator, 
       b'Operator': OperatorDeviceDecorator, 
       b'MultiSampler': SamplerDeviceDecorator, 
       b'AutoFilter': AutoFilterDeviceDecorator, 
       b'Eq8': Eq8DeviceDecorator, 
       b'Compressor2': CompressorDeviceDecorator, 
       b'Pedal': PedalDeviceDecorator, 
       b'DrumBuss': DrumBussDeviceDecorator, 
       b'Echo': EchoDeviceDecorator, 
       b'InstrumentVector': WavetableDeviceDecorator, 
       b'StereoGain': UtilityDeviceDecorator, 
       b'Delay': DelayDeviceDecorator}