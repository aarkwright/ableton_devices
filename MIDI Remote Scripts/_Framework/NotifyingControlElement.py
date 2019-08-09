# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\NotifyingControlElement.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
from .SubjectSlot import Subject, SubjectEvent
from .ControlElement import ControlElement

class NotifyingControlElement(Subject, ControlElement):
    """
    Class representing control elements that can send values
    """
    __subject_events__ = (
     SubjectEvent(name=b'value', doc=b' Called when the control element receives a MIDI value\n                             from the hardware '),)