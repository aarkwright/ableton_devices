# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\components\background.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from ..component import Component

class BackgroundComponent(Component):
    """
    This component resets and adds a no-op listener to every control
    that it receives via arbitrary set_* methods.  It is specially
    useful to give it a layer with every control and low priority such
    that it prevents leaking LED lights or midi notes slipping into
    the midi track.
    """

    def __init__(self, *a, **k):
        super(BackgroundComponent, self).__init__(*a, **k)
        self._control_slots = {}
        self._control_map = {}

    def __getattr__(self, name):
        if len(name) > 4 and name[:4] == b'set_':
            return partial(self._clear_control, name[4:])
        raise AttributeError(name)

    def _clear_control(self, name, control):
        slot = self._control_slots.get(name, None)
        if slot:
            del self._control_slots[name]
            self.disconnect_disconnectable(slot)
        if control:
            self._reset_control(control)
            self._control_map[name] = control
        elif name in self._control_map:
            del self._control_map[name]
        return

    def _reset_control(self, control):
        control.reset()

    def update(self):
        super(BackgroundComponent, self).update()
        if self.is_enabled():
            for control in self._control_map.itervalues():
                self._reset_control(control)


class ModifierBackgroundComponent(BackgroundComponent):
    """
    This component lights up modifiers IFF they have other owners as
    well.  Only give configurable buttons with prioritized resources
    to this component.
    """

    def __init__(self, *a, **k):
        super(ModifierBackgroundComponent, self).__init__(*a, **k)

    def _reset_control(self, control):
        if len(control.resource.owners) > 1:
            control.set_light(True)
        else:
            control.reset()