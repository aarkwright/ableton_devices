# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\components\auto_arm.py
# Compiled at: 2019-05-10 18:21:20
from __future__ import absolute_import, print_function, unicode_literals
from itertools import ifilter
from ...base import listens, listens_group, task
from ...control_surface import Component

class AutoArmComponent(Component):
    """
    Component that implictly arms (aka "pink arms") tracks to
    keep the selected track always armed while there is no
    compatible red-armed track.
    """
    active_instances = []

    def __init__(self, *a, **k):
        super(AutoArmComponent, self).__init__(*a, **k)
        AutoArmComponent.active_instances.append(self)
        self._on_tracks_changed.subject = self.song
        self._on_exclusive_arm_changed.subject = self.song
        self._on_tracks_changed()
        self._on_selected_track_changed.subject = self.song.view
        self._update_implicit_arm_task = self._tasks.add(task.run(self._update_implicit_arm))

    def disconnect(self):
        AutoArmComponent.active_instances.remove(self)
        super(AutoArmComponent, self).disconnect()

    @property
    def needs_restore_auto_arm(self):
        song = self.song
        exclusive_arm = song.exclusive_arm
        selected_track = song.view.selected_track
        return self.is_enabled() and self.can_auto_arm_track(selected_track) and not selected_track.arm and any(ifilter(lambda track: (exclusive_arm or self.can_auto_arm_track(track)) and track.can_be_armed and track.arm, song.tracks))

    def track_can_be_armed(self, track):
        return track.can_be_armed and track.has_midi_input

    def can_auto_arm(self):
        return any([ instance.is_enabled() for instance in AutoArmComponent.active_instances
                   ]) and not self.needs_restore_auto_arm

    def can_auto_arm_track(self, track):
        return self.track_can_be_armed(track)

    @listens(b'selected_track')
    def _on_selected_track_changed(self):
        self.update()

    def update(self):
        super(AutoArmComponent, self).update()
        self._update_implicit_arm()

    def _update_implicit_arm(self):
        self._update_implicit_arm_task.kill()
        song = self.song
        selected_track = song.view.selected_track
        can_auto_arm = self.can_auto_arm()
        for track in song.tracks:
            if self.track_can_be_armed(track):
                track.implicit_arm = can_auto_arm and selected_track == track and self.can_auto_arm_track(track)

    @listens(b'tracks')
    def _on_tracks_changed(self):
        tracks = filter(lambda t: t.can_be_armed, self.song.tracks)
        self._on_arm_changed.replace_subjects(tracks)
        self._on_input_routing_type_changed.replace_subjects(tracks)
        self._on_frozen_state_changed.replace_subjects(tracks)

    @listens(b'exclusive_arm')
    def _on_exclusive_arm_changed(self):
        self.update()

    @listens_group(b'arm')
    def _on_arm_changed(self, track):
        self._update_implicit_arm_task.restart()

    @listens_group(b'input_routing_type')
    def _on_input_routing_type_changed(self, track):
        self._update_implicit_arm_task.restart()

    @listens_group(b'is_frozen')
    def _on_frozen_state_changed(self, track):
        self._update_implicit_arm_task.restart()