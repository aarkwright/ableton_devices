# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\note_editor.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
from pushbase.note_editor_component import NoteEditorComponent

class Push2NoteEditorComponent(NoteEditorComponent):
    __events__ = ('mute_solo_stop_cancel_action_performed', )

    def _on_pad_pressed(self, coordinate):
        super(Push2NoteEditorComponent, self)._on_pad_pressed(coordinate)
        self.notify_mute_solo_stop_cancel_action_performed()