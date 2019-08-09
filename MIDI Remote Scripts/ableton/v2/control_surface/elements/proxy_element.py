# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\elements\proxy_element.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals
from ...base import Proxy
from ..control_element import ControlElement

class ProxyElement(Proxy, ControlElement):

    def reset(self):
        try:
            super(ProxyElement, self).__getattr__(b'reset')()
        except AttributeError:
            pass