# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\note_editor_component.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals
from bisect import bisect
from contextlib import contextmanager
from functools import cmp_to_key, partial
from itertools import chain, imap, product
from ableton.v2.base import clamp, first, index_if, in_range, listens, listenable_property, liveobj_changed, liveobj_valid, sign, EventObject, task
from ableton.v2.control_surface import Component, defaults
from ableton.v2.control_surface.control import ButtonControl, control_matrix, PlayableControl
from .loop_selector_component import create_clip_in_selected_slot
from .matrix_maps import PLAYHEAD_FEEDBACK_CHANNELS
from .pad_control import PadControl
from .step_duplicator import NullStepDuplicator

def note_pitch(note):
    return note[0]


def note_start_time(note):
    return note[1]


def note_length(note):
    return note[2]


def note_velocity(note):
    return note[3]


def note_muted(note):
    return note[4]


ONE_YEAR_AT_120BPM_IN_BEATS = 63072000.0
DEFAULT_VELOCITY = 100
DEFAULT_START_NOTE = 36
DEFAULT_VELOCITY_RANGE_THRESHOLDS = [
 127, 100, 0]
VELOCITY_RANGE_INDEX_TO_COLOR = [b'Full', b'High', b'Low']
BEAT_TIME_EPSILON = 1e-05

def color_for_note(note, velocity_range_thresholds=None):
    thresholds = velocity_range_thresholds or DEFAULT_VELOCITY_RANGE_THRESHOLDS
    if not note_muted(note):
        velocity_range_index = index_if(lambda threshold: note_velocity(note) >= threshold, thresholds)
        return VELOCITY_RANGE_INDEX_TO_COLOR[velocity_range_index]
    else:
        return b'Muted'


def most_significant_note(notes):
    return max(notes, key=lambda n: n[3])


def is_triplet_quantization(triplet_factor):
    return triplet_factor == 0.75


MAX_CLIP_LENGTH = 100000000
RELATIVE_OFFSET = 0.24

class TimeStep(object):
    """
    A fixed step (time range) for the step sequencer
    """

    def __init__(self, start, length, *a, **k):
        super(TimeStep, self).__init__(*a, **k)
        self.start = start
        self.length = length

    @property
    def offset(self):
        return self.length * RELATIVE_OFFSET

    def left_boundary(self):
        return max(0, self.start - self.offset + BEAT_TIME_EPSILON)

    def right_boundary(self):
        return max(0, self.start - self.offset + self.length - BEAT_TIME_EPSILON)

    def includes_note(self, note):
        return self.includes_time(note_start_time(note))

    def overlaps_note(self, note):
        time = note_start_time(note)
        length = note_length(note)
        step_start = self.left_boundary()
        step_end = self.start + self.length - BEAT_TIME_EPSILON
        note_start = int((time + self.offset) / self.length) * self.length
        note_end = note_start + length
        if step_start < note_start:
            return step_end > note_start
        else:
            return step_end < note_end

    def filter_notes(self, notes):
        return filter(self.includes_note, notes)

    def clamp(self, time, extra_time=0.0):
        return clamp(time + extra_time, self.left_boundary(), self.right_boundary())

    def includes_time(self, time):
        return in_range(time - self.start + self.offset, 0, self.length)

    def connected_time_ranges(self):
        return [
         (
          self.start - self.offset, self.length)]


class NullVelocityProvider(EventObject):

    @listenable_property
    def velocity(self):
        return DEFAULT_VELOCITY

    def set_velocities_playable(self, playable):
        pass


def min_max_for_notes(notes, start_time, min_max_values=None):
    for note in notes:
        note_values = list(note[:4])
        note_values[1] -= start_time
        for index, value in enumerate(note_values):
            if not min_max_values:
                min_max_values = [
                 (99999, -99999)] * 4
            min_value, max_value = min_max_values[index]
            min_max_values[index] = (min(value, min_value), max(value, max_value))

    return min_max_values


def get_all_notes(clip, time, _, length):
    return clip.get_notes(time, 0, length, 128)


def remove_all_notes(clip, time, _, length):
    clip.remove_notes(time, 0, length, 128)


def get_single_note(clip, time, notes, length):
    return clip.get_notes(time, notes[0], length, 1)


def remove_single_note(clip, time, notes, length):
    clip.remove_notes(time, notes[0], length, 1)


class NoteEditorComponent(Component):
    __events__ = ('page_length', 'active_note_regions', 'active_steps', 'notes_changed',
                  'modify_all_notes')
    matrix = control_matrix(PadControl, channel=PLAYHEAD_FEEDBACK_CHANNELS[0], sensitivity_profile=b'loop', mode=PlayableControl.Mode.listenable)
    mute_button = ButtonControl(color=b'DefaultButton.Transparent')

    def __init__(self, clip_creator=None, grid_resolution=None, skin_base_key=b'NoteEditor', velocity_range_thresholds=None, velocity_provider=None, get_notes_handler=get_single_note, remove_notes_handler=remove_single_note, duplicate_all_notes=False, *a, **k):
        assert skin_base_key is not None
        super(NoteEditorComponent, self).__init__(*a, **k)
        self._duplicate_all_notes = duplicate_all_notes
        self._get_notes_handler = get_notes_handler
        self._remove_notes_handler = remove_notes_handler
        self._skin_base_key = skin_base_key
        self.full_velocity = False
        self._provided_velocity = None
        self._selected_page_point = 0
        self._page_index = 0
        self._clip_creator = clip_creator
        self._sequencer_clip = None
        self._step_colors = []
        self._pressed_steps = []
        self._modified_steps = []
        self._pressed_step_callback = None
        self._modify_task = self._tasks.add(task.run(self._do_modification))
        self._modify_task.kill()
        self._modify_all_notes_enabled = False
        self._step_tap_tasks = {}
        self._clip_notes = []
        self._pitches = [
         DEFAULT_START_NOTE]
        self._grid_resolution = grid_resolution
        self.__on_resolution_changed.subject = self._grid_resolution
        self.set_step_duplicator(None)
        self._nudge_offset = 0
        self._length_offset = 0
        self._velocity_offset = 0
        self._triplet_factor = 1.0
        self._update_from_grid()
        self.background_color = self._skin_base_key + b'.StepEmpty'
        self._velocity_range_thresholds = velocity_range_thresholds or DEFAULT_VELOCITY_RANGE_THRESHOLDS
        self._velocity_provider = velocity_provider or NullVelocityProvider()
        self.__on_provided_velocity_changed.subject = self._velocity_provider
        return

    @property
    def page_index(self):
        return self._page_index

    @property
    def page_length(self):
        return self._get_step_count() * self._get_step_length() * self._triplet_factor

    @property
    def can_change_page(self):
        return not self._pressed_steps and not self._modified_steps

    @property
    def notes_in_selected_step(self):
        time_steps = []
        if self._modify_all_notes_enabled:
            time_steps = [
             TimeStep(0.0, ONE_YEAR_AT_120BPM_IN_BEATS)]
        else:
            time_steps = [ self._time_step(self.get_step_start_time(start_time)) for start_time in chain(self._pressed_steps, self._modified_steps) ]
        time_steps_with_notes = [ time_step.filter_notes(self._clip_notes) for time_step in time_steps ]
        notes_in_step = []
        for time_step in time_steps_with_notes:
            for note in time_step:
                notes_in_step.append(note_pitch(note))

        return notes_in_step

    def set_selected_page_point(self, point):
        assert self.can_change_page
        self._selected_page_point = point
        index = int(point / self.page_length) if self.page_length != 0 else 0
        if index != self._page_index:
            self._page_index = index
            self._on_clip_notes_changed()

    def _get_modify_all_notes_enabled(self):
        return self._modify_all_notes_enabled

    def _set_modify_all_notes_enabled(self, enabled):
        if enabled != self._modify_all_notes_enabled:
            self._modify_all_notes_enabled = enabled
            self._on_clip_notes_changed()
            self.notify_modify_all_notes()

    modify_all_notes_enabled = property(_get_modify_all_notes_enabled, _set_modify_all_notes_enabled)

    def set_detail_clip(self, clip):
        if liveobj_changed(clip, self._sequencer_clip):
            self._sequencer_clip = clip
            self._step_duplicator.set_clip(clip)
            if self.can_change_page:
                self.set_selected_page_point(0)
            self._on_clip_notes_changed.subject = clip
            self._on_clip_notes_changed()

    def _can_edit(self):
        return len(self._pitches) != 0

    def _get_editing_notes(self):
        return self._pitches

    def _set_editing_notes(self, pitches):
        self._pitches = pitches
        enabled = self._can_edit()
        for button in self.matrix:
            button.enabled = enabled

        if enabled:
            self._on_clip_notes_changed()

    editing_notes = property(_get_editing_notes, _set_editing_notes)

    def _get_width(self):
        if self.matrix.width:
            return self.matrix.width
        return 4

    def _get_height(self):
        if self.matrix.height:
            return self.matrix.height
        return 4

    def set_matrix(self, matrix):
        last_page_length = self.page_length
        self.matrix.set_control_element(matrix)
        for t in self._step_tap_tasks.itervalues():
            t.kill()

        def trigger_modification_task(x, y):
            trigger = partial(self._trigger_modification, (x, y), done=True)
            return self._tasks.add(task.sequence(task.wait(defaults.MOMENTARY_DELAY), task.run(trigger))).kill()

        self._step_tap_tasks = dict([ ((x, y), trigger_modification_task(x, y)) for x, y in product(xrange(self._get_width()), xrange(self._get_height()))
                                    ])
        if matrix and last_page_length != self.page_length:
            self._on_clip_notes_changed()
            self.notify_page_length()
        else:
            self._update_editor_matrix()

    def set_step_duplicator(self, duplicator):
        self._step_duplicator = duplicator or NullStepDuplicator()
        self._step_duplicator.set_clip(self._sequencer_clip)

    def update(self):
        super(NoteEditorComponent, self).update()
        self._update_editor_matrix_leds()

    def _get_clip_notes_time_range(self):
        if self._modify_all_notes_enabled:
            time_length = self._get_step_count() * 4.0
            time_start = 0
        else:
            time_length = self.page_length
            time_start = self._page_index * time_length
        return (time_start - self._time_step(0).offset, time_length)

    @listens(b'notes')
    def _on_clip_notes_changed(self):
        """ get notes from clip for offline array """
        if liveobj_valid(self._sequencer_clip) and self._can_edit():
            time_start, time_length = self._get_clip_notes_time_range()
            self._clip_notes = self._get_notes_handler(self._sequencer_clip, time_start, self._pitches, time_length)
        else:
            self._clip_notes = []
        self._update_editor_matrix()
        self.notify_notes_changed()

    def _update_editor_matrix(self):
        """
        update offline array of button LED values, based on note
        velocity and mute states
        """
        step_colors = [
         self._skin_base_key + b'.StepDisabled'] * self._get_step_count()

        def coords_to_index(coord):
            return coord[0] + coord[1] * self._get_width()

        editing_indices = set(map(coords_to_index, self._modified_steps))
        selected_indices = set(map(coords_to_index, self._pressed_steps))
        last_editing_notes = []
        for time_step, index in self._visible_steps():
            notes = time_step.filter_notes(self._clip_notes)
            if len(notes) > 0:
                last_editing_notes = []
                if index in selected_indices:
                    color = self._skin_base_key + b'.StepSelected'
                elif index in editing_indices:
                    note_color = self._determine_color(notes)
                    color = self._skin_base_key + b'.StepEditing.' + note_color
                    last_editing_notes = notes
                else:
                    note_color = self._determine_color(notes)
                    color = self._skin_base_key + b'.Step.' + note_color
            elif any(imap(time_step.overlaps_note, last_editing_notes)):
                color = self._skin_base_key + b'.StepEditing.' + note_color
            elif index in editing_indices or index in selected_indices:
                color = self._skin_base_key + b'.StepSelected'
                last_editing_notes = []
            else:
                color = self.background_color
                last_editing_notes = []
            step_colors[index] = color

        self._step_colors = step_colors
        self._update_editor_matrix_leds()

    def _determine_color(self, notes):
        return color_for_note(most_significant_note(notes), velocity_range_thresholds=self._velocity_range_thresholds)

    def _visible_steps(self):
        first_time = self.page_length * self._page_index
        steps_per_page = self._get_step_count()
        step_length = self._get_step_length()
        indices = range(steps_per_page)
        if is_triplet_quantization(self._triplet_factor):
            indices = filter(lambda k: k % 8 not in (6, 7), indices)
        return [ (self._time_step(first_time + k * step_length), index) for k, index in enumerate(indices)
               ]

    def _update_editor_matrix_leds(self):
        if self.is_enabled():
            for control in self.matrix:
                control.color = self._step_colors[control.index]

    def _get_step_count(self):
        return self._get_width() * self._get_height()

    def get_step_start_time(self, step):
        x, y = step
        assert in_range(x, 0, self._get_width())
        assert in_range(y, 0, self._get_height())
        page_time = self._page_index * self._get_step_count() * self._triplet_factor
        step_time = x + y * self._get_width() * self._triplet_factor
        return (page_time + step_time) * self._get_step_length()

    def _get_step_length(self):
        return self._grid_resolution.step_length

    def get_row_start_times(self):
        return [ self.get_step_start_time((0, row)) for row in xrange(self._get_height())
               ]

    def _update_from_grid(self):
        quantization, is_triplet = self._grid_resolution.clip_grid
        self._triplet_factor = 1.0 if not is_triplet else 0.75
        if self._clip_creator:
            self._clip_creator.grid_quantization = quantization
            self._clip_creator.is_grid_triplet = is_triplet
        if liveobj_valid(self._sequencer_clip):
            self._sequencer_clip.view.grid_quantization = quantization
            self._sequencer_clip.view.grid_is_triplet = is_triplet

    @mute_button.pressed
    def mute_button(self, button):
        self._trigger_modification(immediate=True)

    @listens(b'index')
    def __on_resolution_changed(self, *a):
        self._release_active_steps()
        self._update_from_grid()
        self.set_selected_page_point(self._selected_page_point)
        self.notify_page_length()
        self._on_clip_notes_changed()

    @matrix.pressed
    def matrix(self, button):
        self._on_pad_pressed(button.coordinate)

    @matrix.released
    def matrix(self, button):
        self._on_pad_released(button.coordinate)

    def _on_pad_pressed(self, coordinate):
        y, x = coordinate
        if self.is_enabled():
            if not liveobj_valid(self._sequencer_clip):
                self.set_detail_clip(create_clip_in_selected_slot(self._clip_creator, self.song))
            if self._can_press_or_release_step(x, y):
                self._on_press_step((x, y))
                self._update_editor_matrix()

    def _on_pad_released(self, coordinate):
        y, x = coordinate
        if self.is_enabled() and self._can_press_or_release_step(x, y):
            self._on_release_step((x, y))
            self._update_editor_matrix()

    def _can_press_or_release_step(self, x, y):
        width = self._get_width() * self._triplet_factor if is_triplet_quantization(self._triplet_factor) else self._get_width()
        return x < width and y < self._get_height()

    @listens(b'velocity')
    def __on_provided_velocity_changed(self):
        if len(self._pressed_steps) + len(self._modified_steps) > 0:
            self._provided_velocity = self._velocity_provider.velocity
            self._trigger_modification(immediate=True)
            self._provided_velocity = None
        return

    def _get_step_time_range(self, step):
        time = self.get_step_start_time(step)
        return (
         time, time + self._get_step_length())

    @property
    def editing_note_regions(self):
        active_time_spans = self.active_time_spans
        editing_notes = set(self.notes_in_selected_step)
        if len(editing_notes) > 1:
            editing_notes = [
             -1]
        return list(product(editing_notes, list(active_time_spans)))

    @property
    def active_time_spans(self):
        if self._modify_all_notes_enabled:
            return [(0.0, ONE_YEAR_AT_120BPM_IN_BEATS)]
        else:

            def time_span(step):
                time_step = self._time_step(self.get_step_start_time(step))
                return (
                 time_step.left_boundary(), time_step.right_boundary())

            return imap(time_span, chain(self._pressed_steps, self._modified_steps))

    @property
    def active_steps(self):
        return imap(self._get_step_time_range, chain(self._pressed_steps, self._modified_steps))

    @property
    def active_note_regions(self):
        return imap(self._get_time_range, chain(self._pressed_steps, self._modified_steps))

    def _get_time_range(self, step):

        def note_compare(left, right):
            return note_start_time(left) - note_start_time(right)

        time = self.get_step_start_time(step)
        notes = self._time_step(time).filter_notes(self._clip_notes)
        if notes:
            beginning_note = first(sorted(notes, key=cmp_to_key(note_compare)))
            start = note_start_time(beginning_note)
            end = start + note_length(beginning_note)
            if len(notes) > 1:
                end_note = notes[(-1)]
                end = note_start_time(end_note) + note_length(end_note)
            return (start, end)
        else:
            return (
             time, time + self._get_step_length())

    def _release_active_steps(self):
        for step in self._pressed_steps + self._modified_steps:
            self._on_release_step(step, do_delete_notes=False)

    def _on_release_step(self, step, do_delete_notes=True):
        self._step_tap_tasks[step].kill()
        if step in self._pressed_steps:
            if do_delete_notes:
                self._delete_notes_in_step(step)
            self._pressed_steps.remove(step)
            for pitch in self._pitches:
                self._add_or_modify_note_in_step(step, pitch)

        if step in self._modified_steps:
            self._modified_steps.remove(step)
        if len(self._modified_steps) + len(self._pressed_steps) == 0:
            self._velocity_provider.set_velocities_playable(True)
        self.notify_active_steps()
        self.notify_active_note_regions()

    def _find_continued_step(self, step):

        def steps_to_note_start(steps):
            return map(lambda step: self.get_step_start_time(step), steps)

        time = self.get_step_start_time(step)
        all_steps_with_notes = [ time_step for time_step, index in self._visible_steps() if time_step.filter_notes(self._clip_notes)
                               ]
        all_time_step_starts = map(lambda ts: ts.start, all_steps_with_notes)
        if all_time_step_starts:
            insert_point = bisect(all_time_step_starts, time)
            if insert_point > 0:
                prev_filled_step = all_steps_with_notes[(insert_point - 1)]
                notes_in_modified_steps = steps_to_note_start(self._modified_steps)
                if prev_filled_step.start in notes_in_modified_steps:
                    return prev_filled_step
        return

    def _add_step_to_duplicator(self, step):
        nudge_offset = 0
        time = self.get_step_start_time(step)
        notes = self._time_step(time).filter_notes(self._clip_notes)
        step_start, step_end = self._get_time_range(step)
        if notes:
            nudge_offset = min(imap(note_start_time, notes)) - time
        if self._duplicate_all_notes:
            self._step_duplicator.add_step(step_start, step_end, nudge_offset)
        else:
            self._step_duplicator.add_step_with_pitch(self.editing_notes[0], step_start, step_end, nudge_offset)

    def _on_press_step(self, step):
        if liveobj_valid(self._sequencer_clip) and step not in self._pressed_steps and step not in self._modified_steps:
            if self._step_duplicator.is_duplicating:
                self._add_step_to_duplicator(step)
            else:
                self._step_tap_tasks[step].restart()
                continued_step = self._find_continued_step(step)
                if continued_step:
                    self._modify_length_of_notes_within_existing_step(continued_step, step)
                else:
                    self._pressed_steps.append(step)
                self._velocity_provider.set_velocities_playable(False)
        self.notify_active_steps()
        self.notify_active_note_regions()

    def _modify_length_of_notes_within_existing_step(self, existing_time_step, new_step):
        notes_in_step = existing_time_step.filter_notes(self._clip_notes)
        new_end = float(self.get_step_start_time(new_step) + self._get_step_length())
        step_mute = all(map(lambda note: note_muted(note), notes_in_step))
        new_notes = []
        for note in self._clip_notes:
            length_offset = new_end - (note_length(note) + note_start_time(note)) if note in notes_in_step else 0
            new_notes.append(self._modify_single_note(step_mute, existing_time_step, length_offset, note))

        self._replace_notes(tuple(new_notes))

    def _time_step(self, time):
        return TimeStep(time, self._get_step_length())

    def _get_notes_info_from_step(self, step):
        time = self.get_step_start_time(step)
        notes = self._time_step(time).filter_notes(self._clip_notes)
        pitches = [ note_pitch(note) for note in notes ]
        return (
         time, notes, pitches)

    def toggle_pitch_for_all_modified_steps(self, pitch):
        assert liveobj_valid(self._sequencer_clip)
        for step in set(chain(self._pressed_steps, self._modified_steps)):
            time, notes, pitches = self._get_notes_info_from_step(step)
            if pitch not in pitches:
                self._add_new_note_in_step(step, pitch, time)
            else:
                time_step = self._time_step(self.get_step_start_time(step))
                for time, length in time_step.connected_time_ranges():
                    remove_single_note(self._sequencer_clip, time, (pitch,), length)

    def _add_new_note_in_step(self, step, pitch, time):
        mute = self.mute_button.is_pressed
        velocity = 127 if self.full_velocity else self._velocity_provider.velocity
        note = (pitch, time, self._get_step_length(), velocity, mute)
        self._sequencer_clip.set_notes((note,))
        self._sequencer_clip.deselect_all_notes()
        self._trigger_modification(step, done=True)

    def _add_or_modify_note_in_step(self, step, pitch, modify_existing=True):
        """
        Add note in given step if there are none in there, otherwise
        select the step for potential deletion or modification
        """
        if liveobj_valid(self._sequencer_clip):
            time, notes, pitches = self._get_notes_info_from_step(step)
            if notes:
                if pitch in pitches and modify_existing:
                    most_significant_velocity = most_significant_note(notes)[3]
                    if self.mute_button.is_pressed or most_significant_velocity != 127 and self.full_velocity:
                        self._trigger_modification(step, immediate=True)
            else:
                self._add_new_note_in_step(step, pitch, time)
                return True
        return False

    def _delete_notes_in_step(self, step):
        """ Delete all notes in the given step """
        if liveobj_valid(self._sequencer_clip) and self._can_edit():
            time_step = self._time_step(self.get_step_start_time(step))
            for time, length in time_step.connected_time_ranges():
                self._remove_notes_handler(self._sequencer_clip, time, self._pitches, length)

    def set_nudge_offset(self, value):
        self._modify_note_property(b'_nudge_offset', value)

    def set_length_offset(self, value):
        self._modify_note_property(b'_length_offset', value)

    def set_velocity_offset(self, value):
        self._modify_note_property(b'_velocity_offset', value)

    def _modify_note_property(self, note_property, value):
        if self.is_enabled():
            with self._full_velocity_context(False):
                setattr(self, note_property, getattr(self, note_property) + value)
                self._trigger_modification(immediate=True)

    @contextmanager
    def _full_velocity_context(self, desired_full_velocity_state):
        saved_velocity = self.full_velocity
        self.full_velocity = desired_full_velocity_state
        yield
        self.full_velocity = saved_velocity

    def set_full_velocity(self):
        if self.is_enabled():
            with self._full_velocity_context(True):
                self._trigger_modification()

    def notify_modification(self):
        """
        Tell the note editor about changes to pressed steps, so further modifications
        by the note editor are ignored.
        """
        self._trigger_modification(done=True)

    def _trigger_modification(self, step=None, done=False, immediate=False):
        """
        Because the modification of notes is slow, we
        accumulate modification events and perform all of them
        alltogether in a task. Call this function whenever a given set
        of steps (or potentially all steps) are to be modified.

        If done=True, we just notify that the given steps have been
        modified without actually executing the task.
        """
        needs_update = False
        if step is None:
            needs_update = bool(self._pressed_steps)
            self._modified_steps += self._pressed_steps
            self._pressed_steps = []
        elif step not in self._modified_steps:
            self._modified_steps.append(step)
        else:
            if step in self._pressed_steps:
                self._pressed_steps.remove(step)
            needs_update = True

        if not done:
            if immediate:
                self._do_modification()
                self._modify_task.kill()
            elif self._modify_task.is_killed:
                self._do_modification()
                self._modify_task.restart()
        if needs_update:
            self._update_editor_matrix()
        return

    def _reset_modifications(self):
        self._velocity_offset = 0
        self._length_offset = 0
        self._nudge_offset = 0

    def _do_modification(self):
        if self._modify_all_notes_enabled:
            new_notes = self._modify_all_notes()
            self._replace_notes(new_notes)
        elif self._modified_steps:
            notes_added = map(lambda step_and_pitch: self._add_or_modify_note_in_step(modify_existing=False, *step_and_pitch), product(self._modified_steps, self._pitches))
            if any(notes_added):
                self._modify_task.restart()
            else:
                new_notes = self._modify_step_notes(self._modified_steps)
                self._replace_notes(new_notes)
        self._reset_modifications()

    def _replace_notes(self, new_notes):
        if new_notes != self._clip_notes and self._can_edit():
            time_start, time_length = self._get_clip_notes_time_range()
            self._remove_notes_handler(self._sequencer_clip, time_start, self._pitches, time_length)
            self._sequencer_clip.set_notes(tuple(new_notes))
            self._sequencer_clip.deselect_all_notes()

    def _modify_all_notes(self):
        """ modify all notes in the current pitch """
        return self._modify_notes_in_time(TimeStep(0.0, MAX_CLIP_LENGTH), self._clip_notes, self._length_offset)

    def _limited_nudge_offset(self, steps, notes, nudge_offset):
        limited_nudge_offset = MAX_CLIP_LENGTH
        for step in steps:
            time_step = self._time_step(self.get_step_start_time(step))
            for note in time_step.filter_notes(notes):
                start_time = note_start_time(note)
                time_after_nudge = time_step.clamp(start_time, nudge_offset)
                limited_nudge_offset = min(limited_nudge_offset, abs(start_time - time_after_nudge))

        return sign(nudge_offset) * limited_nudge_offset

    def _modify_step_notes(self, steps):
        """ Return a new list with all notes within steps modified. """
        notes = self._clip_notes
        self._nudge_offset = self._limited_nudge_offset(steps, notes, self._nudge_offset)
        for step in steps:
            time_step = self._time_step(self.get_step_start_time(step))
            notes = self._modify_notes_in_time(time_step, notes, self._length_offset)

        return notes

    def _modify_notes_in_time(self, time_step, notes, length_offset):
        step_notes = time_step.filter_notes(self._clip_notes)
        step_mute = all(map(lambda note: note_muted(note), step_notes))
        return map(partial(self._modify_single_note, step_mute, time_step, length_offset), notes)

    def _modify_single_note(self, step_mute, time_step, length_offset, note):
        """
        Return a modified version of the passed in note taking into
        account current modifiers. If the note is not within
        the given step, returns the note as-is.

        If the time_step is inside a loop, the last part of the loop
        is considered as being the same as the part just before the
        loop, so the resulting note may, in this case, jump between
        the beginning and the end.
        """
        pitch, time, length, velocity, mute = note
        if time_step.includes_time(time):
            time = time_step.clamp(time, self._nudge_offset)
            if length_offset <= -time_step.length and length + length_offset < time_step.length:
                if length > time_step.length:
                    length = time_step.length
            else:
                length = max(0, length + length_offset)
            if self._provided_velocity:
                velocity = self._provided_velocity
            elif self.full_velocity:
                velocity = 127
            else:
                velocity = clamp(velocity + self._velocity_offset, 1, 127)
            mute = not step_mute if self.mute_button.is_pressed else mute
        return (
         pitch, time, length, velocity, mute)

    def get_min_max_note_values(self):
        if self._modify_all_notes_enabled and len(self._clip_notes) > 0:
            return min_max_for_notes(self._clip_notes, 0.0)
        else:
            if len(self._pressed_steps) + len(self._modified_steps) > 0:
                min_max_values = None
                for step in chain(self._modified_steps, self._pressed_steps):
                    start_time = self.get_step_start_time(step)
                    min_max_values = min_max_for_notes(self._time_step(start_time).filter_notes(self._clip_notes), start_time, min_max_values)

                return min_max_values
            return