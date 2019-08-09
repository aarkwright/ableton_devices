# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\base\live_api_utils.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals

def liveobj_changed(obj, other):
    """
    Check whether obj and other are not equal, properly handling lost weakrefs.

    Use this whenever you cache a Live API object in some variable, and want to check
    whether you need to update the cached object.
    """
    return obj != other or type(obj) != type(other)


def liveobj_valid(obj):
    """
    Check whether obj represents a valid Live API obj.

    This will return False both if obj represents a lost weakref or is None.
    It's important that Live API objects are not checked using "is None", since this
    would treat lost weakrefs as valid.
    """
    return obj != None