# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\melodic_component.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals
from itertools import izip_longest
from ableton.v2.base import find_if, forward_property, listenable_property, listens, listens_group, liveobj_valid
from ableton.v2.control_surface.components import AccentComponent
from ableton.v2.control_surface.elements import to_midi_value
from ableton.v2.control_surface.mode import LayerMode
from .consts import MessageBoxText
from .instrument_component import InstrumentComponent
from .loop_selector_component import LoopSelectorComponent
from .matrix_maps import PLAYHEAD_FEEDBACK_CHANNELS, NON_FEEDBACK_CHANNEL
from .melodic_pattern import pitch_index_to_string
from .messenger_mode_component import MessengerModesComponent
from .note_editor_component import NoteEditorComponent
from .note_editor_paginator import NoteEditorPaginator
from .playhead_component import PlayheadComponent
from .step_duplicator import StepDuplicatorComponent
from . import consts
NUM_NOTE_EDITORS = 8

class MelodicComponent(MessengerModesComponent):

    def __init__(self, clip_creator=None, parameter_provider=None, grid_resolution=None, note_layout=None, note_editor_settings=None, note_editor_class=NoteEditorComponent, velocity_range_thresholds=None, skin=None, instrument_play_layer=None, instrument_sequence_layer=None, pitch_mod_touch_strip_mode=None, play_loop_instrument_layer=None, layer=None, sequence_layer_with_loop=None, *a, **k):
        super(MelodicComponent, self).__init__(*a, **k)
        self._matrices = None
        self._grid_resolution = grid_resolution
        self.instrument = InstrumentComponent(parent=self, note_layout=note_layout)
        self._step_duplicator = StepDuplicatorComponent(parent=self)
        self._accent_component = AccentComponent(parent=self)
        self._note_editors = [ note_editor_class(parent=self, clip_creator=clip_creator, grid_resolution=self._grid_resolution, velocity_range_thresholds=velocity_range_thresholds, is_enabled=False) for _ in xrange(NUM_NOTE_EDITORS)
                             ]
        for editor in self._note_editors:
            note_editor_settings.add_editor(editor)
            editor.set_step_duplicator(self._step_duplicator)

        self.paginator = NoteEditorPaginator(self._note_editors, parent=self)
        self._loop_selector = LoopSelectorComponent(parent=self, clip_creator=clip_creator, paginator=self.paginator, is_enabled=False, default_size=8)
        self._playhead = None
        self._playhead_component = PlayheadComponent(parent=self, grid_resolution=grid_resolution, paginator=self.paginator, follower=self._loop_selector, feedback_channels=PLAYHEAD_FEEDBACK_CHANNELS, is_enabled=False)
        self._play_modes = MessengerModesComponent(muted=True, is_enabled=False, parent=self)
        self._play_modes.add_mode(b'play', [
         LayerMode(self.instrument, instrument_play_layer),
         pitch_mod_touch_strip_mode], default_mode=b'play', alternative_mode=b'play_loop')
        self._play_modes.add_mode(b'play_loop', [
         LayerMode(self.instrument, instrument_play_layer),
         self._loop_selector,
         LayerMode(self, play_loop_instrument_layer),
         self._playhead_component,
         self.paginator,
         pitch_mod_touch_strip_mode], message=consts.MessageBoxText.ALTERNATE_PLAY_LOOP, default_mode=b'play', alternative_mode=b'play_loop')
        self._play_modes.selected_mode = b'play'
        self.add_mode(b'play', self._play_modes, message=MessageBoxText.LAYOUT_MELODIC_PLAYING)
        self._sequence_modes = MessengerModesComponent(muted=True, is_enabled=False, parent=self)
        self._sequence_modes.add_mode(b'sequence', [
         LayerMode(self.instrument, instrument_sequence_layer),
         note_editor_settings,
         self._loop_selector,
         LayerMode(self, layer),
         self._playhead_component,
         self._update_note_editors,
         self.paginator,
         self._accent_component] + self._note_editors, message=MessageBoxText.LAYOUT_MELODIC_SEQUENCER, default_mode=b'sequence', alternative_mode=b'sequence_loop')
        self._sequence_modes.add_mode(b'sequence_loop', [
         LayerMode(self.instrument, instrument_sequence_layer),
         note_editor_settings,
         self._loop_selector,
         LayerMode(self, sequence_layer_with_loop),
         self._playhead_component,
         self._update_note_editors,
         self.paginator,
         self._accent_component] + self._note_editors, message=MessageBoxText.ALTERNATE_SEQUENCE_LOOP, default_mode=b'sequence', alternative_mode=b'sequence_loop')
        self._sequence_modes.selected_mode = b'sequence'
        self.add_mode(b'sequence', self._sequence_modes, message=MessageBoxText.LAYOUT_MELODIC_SEQUENCER)
        self.selected_mode = b'play'
        self._on_detail_clip_changed.subject = self.song.view
        self._on_pattern_changed.subject = self.instrument
        self._on_notes_changed.subject = self.instrument
        self.__on_grid_resolution_changed.subject = self._grid_resolution
        self._on_page_index_changed.subject = self.paginator
        self._on_page_length_changed.subject = self.paginator
        self._on_active_steps_changed.replace_subjects(self._note_editors)
        self._on_modify_all_notes_changed.replace_subjects(self._note_editors)
        self.__on_accent_activated_changed.subject = self._accent_component
        self._on_detail_clip_changed()
        self._update_note_editors()
        self._skin = skin
        self._playhead_color = b'Melodic.Playhead'
        self._update_playhead_color()
        self._loop_selector.set_step_duplicator(self._step_duplicator)
        self._show_notifications = True
        return

    @property
    def play_modes(self):
        return self._play_modes

    @property
    def sequence_modes(self):
        return self._sequence_modes

    def set_playhead(self, playhead):
        self._playhead = playhead
        self._playhead_component.set_playhead(playhead)
        self._update_playhead_color()

    set_loop_selector_matrix = forward_property(b'_loop_selector')(b'set_loop_selector_matrix')
    set_short_loop_selector_matrix = forward_property(b'_loop_selector')(b'set_short_loop_selector_matrix')
    next_loop_page_button = forward_property(b'_loop_selector')(b'next_page_button')
    prev_loop_page_button = forward_property(b'_loop_selector')(b'prev_page_button')
    delete_button = forward_property(b'_loop_selector')(b'delete_button')

    def set_duplicate_button(self, button):
        self._step_duplicator.button.set_control_element(button)

    def set_note_editor_matrices(self, matrices):
        assert not matrices or len(matrices) <= NUM_NOTE_EDITORS
        self._matrices = matrices
        for editor, matrix in izip_longest(self._note_editors, matrices or []):
            if editor:
                editor.set_matrix(matrix)

        self._update_matrix_channels_for_playhead()

    def _get_playhead_color(self):
        self._playhead_color

    def _set_playhead_color(self, value):
        self._playhead_color = b'Melodic.' + value
        self._update_playhead_color()

    playhead_color = property(_get_playhead_color, _set_playhead_color)

    @listens(b'detail_clip')
    def _on_detail_clip_changed(self):
        if self.is_enabled():
            clip = self.song.view.detail_clip
            clip = clip if liveobj_valid(clip) and clip.is_midi_clip else None
            for note_editor in self._note_editors:
                note_editor.set_detail_clip(clip)

            self._loop_selector.set_detail_clip(clip)
            self._playhead_component.set_clip(clip)
            self.instrument.set_detail_clip(clip)
        return

    @listens(b'activated')
    def __on_accent_activated_changed(self):
        self._update_full_velocity_for_editors()

    def _update_full_velocity_for_editors(self):
        enabled = self._accent_component.activated
        for note_editor in self._note_editors:
            note_editor.full_velocity = enabled

    def set_full_velocity(self, full_velocity):
        self._accent_component.set_full_velocity(full_velocity)
        self._update_full_velocity_for_editors()

    def set_accent_button(self, accent_button):
        self._accent_component.accent_button.set_control_element(accent_button)
        self._update_full_velocity_for_editors()

    def set_quantization_buttons(self, buttons):
        self._grid_resolution.quantization_buttons.set_control_element(buttons)

    def set_mute_button(self, button):
        for e in self._note_editors:
            e.mute_button.set_control_element(button)

    @property
    def show_notifications(self):
        return self._show_notifications

    @show_notifications.setter
    def show_notifications(self, value):
        self._show_notifications = value

    @listenable_property
    def editable_pitches(self):
        note_editor_range = self._note_editors if self.sequence_modes.selected_mode == b'sequence' else self._note_editors[0:7]
        return [ editor.editing_notes[0] for editor in note_editor_range if len(editor.editing_notes) > 0
               ]

    @listenable_property
    def step_length(self):
        return self._grid_resolution.step_length

    @listenable_property
    def editing_note_regions(self):
        return sum([ note_editor.editing_note_regions for note_editor in self._note_editors
                   ], [])

    @listenable_property
    def row_start_times(self):
        return self._note_editors[0].get_row_start_times()

    @listens(b'index')
    def __on_grid_resolution_changed(self, *a):
        if self.is_enabled():
            self.notify_row_start_times()
            self.notify_step_length()

    @listens(b'page_index')
    def _on_page_index_changed(self):
        if self.is_enabled():
            self.notify_row_start_times()

    @listens(b'page_length')
    def _on_page_length_changed(self):
        if self.is_enabled():
            self.notify_row_start_times()

    @listens_group(b'active_steps')
    def _on_active_steps_changed(self, _):
        if self.is_enabled():
            self.notify_editing_note_regions()

    @listens_group(b'modify_all_notes')
    def _on_modify_all_notes_changed(self, _):
        if self.is_enabled():
            self.notify_editing_note_regions()

    @listens(b'position')
    def _on_notes_changed(self, *args):
        self._update_note_editors()
        self._show_notes_information()

    @listens(b'pattern')
    def _on_pattern_changed(self):
        self._update_note_editors()

    def _update_note_editors(self, *a):
        for row, note_editor in enumerate(self._note_editors):
            note_info = self.instrument.pattern[row]
            note_editor.background_color = b'NoteEditor.' + note_info.color
            note_editor.editing_notes = [note_info.index] if note_info.index != None else []

        self._update_matrix_channels_for_playhead()
        self.notify_editable_pitches()
        self.notify_row_start_times()
        self.notify_step_length()
        return

    def _update_matrix_channels_for_playhead(self):
        if self.is_enabled() and self._matrices is not None:
            pattern = self.instrument.pattern
            for matrix, (y, _) in self._matrices.iterbuttons():
                if matrix:
                    for x, button in enumerate(matrix):
                        if button:
                            if pattern[y].index is not None:
                                button.set_identifier(x)
                                button.set_channel(PLAYHEAD_FEEDBACK_CHANNELS[y])
                            else:
                                button.set_identifier(button._original_identifier)
                                button.set_channel(NON_FEEDBACK_CHANNEL)

        return

    def _update_playhead_color(self):
        if self.is_enabled() and self._skin and self._playhead:
            self._playhead.velocity = to_midi_value(self._skin[self._playhead_color])

    def update(self):
        super(MelodicComponent, self).update()
        if self.is_enabled():
            self._on_detail_clip_changed()
            self._update_playhead_color()
            self._update_note_editors()

    def _show_notes_information(self, mode=None):
        if self.is_enabled() and self.show_notifications:
            if mode is None:
                mode = self.selected_mode
            if mode == b'sequence':
                message = b'Sequence %s to %s'
                start_note = self._note_editors[0].editing_notes[0]
                end_editor = find_if(lambda editor: len(editor.editing_notes) > 0, reversed(self._note_editors))
                end_note = end_editor.editing_notes[0]
                self.show_notification(message % (pitch_index_to_string(start_note),
                 pitch_index_to_string(end_note)))
            else:
                self.instrument.show_pitch_range_notification()
        return