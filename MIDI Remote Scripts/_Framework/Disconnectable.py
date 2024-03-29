# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\Disconnectable.py
# Compiled at: 2018-11-30 15:48:11
"""
Interface for items that adquire resources.
"""
from __future__ import absolute_import, print_function, unicode_literals
from .Util import find_if

class Disconnectable(object):
    """
    Represents an entity that holds connections to other objects that
    should be explicitly cleared to avoid object lifetime problems or
    leaking listeners.
    """

    def disconnect(self):
        pass


class CompoundDisconnectable(Disconnectable):
    """
    Compound disconnectable. Collects other disconnectables and
    disconnects them recursively.
    """

    def __init__(self, *a, **k):
        super(CompoundDisconnectable, self).__init__(*a, **k)
        self._registered_disconnectables = []

    def register_disconnectable(self, slot):
        if slot not in self._registered_disconnectables:
            self._registered_disconnectables.append(slot)
        return slot

    def unregister_disconnectable(self, slot):
        if slot in self._registered_disconnectables:
            self._registered_disconnectables.remove(slot)

    def disconnect_disconnectable(self, slot):
        if slot in self._registered_disconnectables:
            self._registered_disconnectables.remove(slot)
            slot.disconnect()

    def find_disconnectable(self, predicate):
        return find_if(predicate, self._registered_disconnectables)

    def has_disconnectable(self, slot):
        return slot in self._registered_disconnectables

    def disconnect(self):
        for slot in self._registered_disconnectables:
            slot.disconnect()

        self._registered_disconnectables = []
        super(CompoundDisconnectable, self).disconnect()


class disconnectable(object):
    """
    Context manager that will disconnect the given disconnectable when
    the context is exited.  It returns the original disconnectable.
    """

    def __init__(self, managed=None, *a, **k):
        super(disconnectable, self).__init__(*a, **k)
        self._managed = managed

    def __enter__(self):
        managed = self._managed
        return managed

    def __exit__(self, *a, **k):
        if self._managed is not None:
            self._managed.disconnect()
        return