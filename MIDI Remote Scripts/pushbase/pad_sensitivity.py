# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\pad_sensitivity.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals
from itertools import repeat
from ableton.v2.base import find_if, second, nop, task
from ableton.v2.control_surface import Component

class PadUpdateComponent(Component):
    """
    Sets a set of parameters for different pads.  It keeps a set of
    profiles, and maps a profile to each pad.  It caches all
    modifications to the pad profiles, updating later optimally.

    The all_pads parameter contains the pads identifiers.

    The parameter_sender is a function that is used to update the
    pads. It takes the parameters as first value and a second optional
    value indicating the pad to update, or None to update all possible
    pads.
    """

    def __init__(self, all_pads=tuple(), parameter_sender=nop, default_profile=None, update_delay=0, *a, **k):
        assert find_if(lambda pad: pad < 0 or pad > 63, all_pads or []) == None
        super(PadUpdateComponent, self).__init__(*a, **k)
        self.parameter_sender = parameter_sender
        self._all_pads = set(all_pads)
        self._modified_pads = set(all_pads)
        self._profiles = {b'default': default_profile}
        self._profile_for = dict(zip(all_pads, repeat(b'default')))
        self._profile_count = {b'default': len(all_pads)}
        self._update_task = self._tasks.add(task.sequence(task.wait(update_delay), task.run(self._update_modified)))
        self._update_task.restart()
        return

    def set_profile(self, profile_id, parameters):
        self._profiles[profile_id] = parameters
        self._profile_count.setdefault(profile_id, 0)
        affected = [ k for k, v in self._profile_for.iteritems() if v == profile_id ]
        self._add_modified_pads(affected)

    def get_profile(self, profile_id):
        return self._profiles[profile_id]

    def set_pad(self, pad, new_profile):
        assert pad in self._all_pads
        assert new_profile in self._profile_count
        old_profile = self._profile_for[pad]
        if old_profile != new_profile:
            self._add_modified_pads([pad])
            self._profile_for[pad] = new_profile
            self._profile_count[old_profile] -= 1
            self._profile_count[new_profile] += 1

    def update(self):
        super(PadUpdateComponent, self).update()
        self._add_modified_pads(self._all_pads)
        self._update_modified()

    def _update_modified(self):
        if self.is_enabled() and self._modified_pads:
            assert sum(self._profile_count.itervalues()) == len(self._all_pads)
            largest_profile, largest_count = max(self._profile_count.iteritems(), key=second)
            if len(self._all_pads) - largest_count + 1 < len(self._modified_pads):
                self.parameter_sender(self._profiles[largest_profile])
                for pad in self._all_pads:
                    profile = self._profile_for[pad]
                    if profile != largest_profile:
                        self.parameter_sender(self._profiles[profile], pad)

            else:
                for pad in self._modified_pads:
                    self.parameter_sender(self._profiles[self._profile_for[pad]], pad)

            self._modified_pads.clear()
        self._update_task.kill()

    def _add_modified_pads(self, pads):
        self._modified_pads.update(pads)
        self._update_task.restart()