# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\consts.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals
import sys, Live
from ableton.v2.control_surface import DEFAULT_PRIORITY
DISPLAY_LENGTH = 72
SIDE_BUTTON_COLORS = dict(color=b'DefaultButton.On', disabled_color=b'DefaultButton.Disabled')
PROTO_FAST_DEVICE_NAVIGATION = False
PROTO_AUDIO_NOTE_MODE = False
PROTO_SONG_IS_ROOT = False
PROTO_TOUCH_ENCODER_TO_STRIP = False
SHARED_PRIORITY = DEFAULT_PRIORITY
M4L_PRIORITY = DEFAULT_PRIORITY + 7
USER_BUTTON_PRIORITY = DEFAULT_PRIORITY + 6
MESSAGE_BOX_PRIORITY = DEFAULT_PRIORITY + 5
MOMENTARY_DIALOG_PRIORITY = DEFAULT_PRIORITY + 4
SETUP_DIALOG_PRIORITY = DEFAULT_PRIORITY + 3
DIALOG_PRIORITY = DEFAULT_PRIORITY + 2
NOTIFICATION_PRIORITY = DEFAULT_PRIORITY + 1
BACKGROUND_PRIORITY = DEFAULT_PRIORITY - 3
GLOBAL_MAP_MODE = Live.MidiMap.MapMode.relative_smooth_two_compliment
CHAR_ARROW_UP = b'\x00'
CHAR_ARROW_DOWN = b'\x01'
CHAR_ARROW_RIGHT = b'\x1e'
CHAR_ARROW_LEFT = b'\x1f'
CHAR_RACK = b'\x02'
CHAR_BAR_LEFT = b'\x03'
CHAR_BAR_RIGHT = b'\x04'
CHAR_SPLIT_BLOCK = b'\x05'
CHAR_SPLIT_DASH = b'\x06'
CHAR_FOLDER = b'\x07'
CHAR_ELLIPSIS = b'\x1c'
CHAR_FLAT_SIGN = b'\x1b'
CHAR_ELLIPSIS = b'\x1c'
CHAR_FULL_BLOCK = b'\x1d'
CHAR_SELECT = b'\x7f'
GRAPH_VOL = ('\x03\x06\x06\x06\x06\x06\x06\x06', '\x05\x06\x06\x06\x06\x06\x06\x06',
             '\x05\x03\x06\x06\x06\x06\x06\x06', '\x05\x05\x06\x06\x06\x06\x06\x06',
             '\x05\x05\x03\x06\x06\x06\x06\x06', '\x05\x05\x05\x06\x06\x06\x06\x06',
             '\x05\x05\x05\x03\x06\x06\x06\x06', '\x05\x05\x05\x05\x06\x06\x06\x06',
             '\x05\x05\x05\x05\x03\x06\x06\x06', '\x05\x05\x05\x05\x05\x06\x06\x06',
             '\x05\x05\x05\x05\x05\x03\x06\x06', '\x05\x05\x05\x05\x05\x05\x06\x06',
             '\x05\x05\x05\x05\x05\x05\x03\x06', '\x05\x05\x05\x05\x05\x05\x05\x06',
             '\x05\x05\x05\x05\x05\x05\x05\x03', '\x05\x05\x05\x05\x05\x05\x05\x05')
GRAPH_PAN = ('\x05\x05\x05\x05\x06\x06\x06\x06', '\x04\x05\x05\x05\x06\x06\x06\x06',
             '\x06\x05\x05\x05\x06\x06\x06\x06', '\x06\x04\x05\x05\x06\x06\x06\x06',
             '\x06\x06\x05\x05\x06\x06\x06\x06', '\x06\x06\x04\x05\x06\x06\x06\x06',
             '\x06\x06\x06\x05\x06\x06\x06\x06', '\x06\x06\x06\x04\x06\x06\x06\x06',
             '\x06\x06\x06\x04\x03\x06\x06\x06', '\x06\x06\x06\x06\x03\x06\x06\x06',
             '\x06\x06\x06\x06\x05\x06\x06\x06', '\x06\x06\x06\x06\x05\x03\x06\x06',
             '\x06\x06\x06\x06\x05\x05\x06\x06', '\x06\x06\x06\x06\x05\x05\x03\x06',
             '\x06\x06\x06\x06\x05\x05\x05\x06', '\x06\x06\x06\x06\x05\x05\x05\x03',
             '\x06\x06\x06\x06\x05\x05\x05\x05')
GRAPH_SIN = ('\x03\x06\x06\x06\x06\x06\x06\x06', '\x04\x06\x06\x06\x06\x06\x06\x06',
             '\x06\x03\x06\x06\x06\x06\x06\x06', '\x06\x04\x06\x06\x06\x06\x06\x06',
             '\x06\x06\x03\x06\x06\x06\x06\x06', '\x06\x06\x04\x06\x06\x06\x06\x06',
             '\x06\x06\x06\x03\x06\x06\x06\x06', '\x06\x06\x06\x04\x06\x06\x06\x06',
             '\x06\x06\x06\x06\x03\x06\x06\x06', '\x06\x06\x06\x06\x04\x06\x06\x06',
             '\x06\x06\x06\x06\x06\x03\x06\x06', '\x06\x06\x06\x06\x06\x04\x06\x06',
             '\x06\x06\x06\x06\x06\x06\x03\x06', '\x06\x06\x06\x06\x06\x06\x04\x06',
             '\x06\x06\x06\x06\x06\x06\x06\x03', '\x06\x06\x06\x06\x06\x06\x06\x04')
DISTANT_FUTURE = 999999

class MessageBoxText:
    LIVE_DIALOG = b'\n                    Live is showing a dialog' + b'\n                    that needs your attention.'
    CLIP_DUPLICATION_FAILED = b'\n                     The clip could not be duplicated' + b'\n                      because it is recording'
    SCENE_LIMIT_REACHED = b'\n                  No more scene can be inserted' + b'\n                   for this version of Live'
    SCENE_DUPLICATION_FAILED = b'\n                  This scene cannot be duplicated' + b'\n                      because it is recording'
    TRACK_LIMIT_REACHED = b'\n                  No more track can be inserted' + b'\n                   for this version of Live'
    MAX_RETURN_TRACKS_REACHED = b'\n                  Maximum number of return tracks' + b'\n                  reached'
    TRACK_DUPLICATION_FAILED = b'\n                  This track cannot be duplicated' + b'\n                      because it is recording'
    TRACK_DELETE_FAILED = b'\n                  This track cannot be deleted' + b'\n                      because it is recording'
    DELETE_TRACK = b'                  Track deleted:    %s'
    DUPLICATE_TRACK = b'                  Track duplicated: %s'
    DELETE_CLIP = b'                  Clip deleted:     %s'
    DUPLICATE_CLIP = b'                  Clip duplicated:  %s'
    QUANTIZE_CLIP = b'                  Quantized to:     %(to)s, %(amount)s'
    QUANTIZE_CLIP_PITCH = b'                Quantized %(source)s to:   %(to)s, %(amount)s'
    DELETE_NOTES = b'                  Notes deleted:    %s'
    CAPTURE_AND_INSERT_SCENE = b'                      Duplicated to scene %s'
    DUPLICATE_LOOP = b'                   New loop length: %(length)s'
    DELETE_SCENE = b'                  Scene deleted:    %s'
    DUPLICATE_SCENE = b'                  Scene duplicated: %s'
    DELETE_ENVELOPE = b'                  Delete automation %(automation)s'
    DEFAULT_PARAMETER_VALUE = b'                  Reset to default: %(automation)s'
    DELETE_DRUM_RACK_PAD = b'                  Drum Pad deleted: %s'
    DELETE_SLICE = b'       Slice %s   deleted'
    FIXED_LENGTH = b'                      Fixed Length: %s'
    EMPTY_DEVICE_CHAIN = b'\n\n               No Devices.    Press [Browse] to add a device.'
    STUCK_PAD_WARNING = b'         Warning: Low threshold may cause stuck pads'
    UNDO = b'            Undo:     Reverted last action'
    REDO = b'            Redo: Re-performed last undone action'
    TRACK_FROZEN_INFO = b'                    ' + b'Cannot modify a frozen track'
    SELECTED_CLIP_BLINK = b' Press            to edit playing   clip'
    PLAYING_CLIP_ABOVE_SELECTED_CLIP = b' Press Up Arrow   to edit playing   clip'
    PLAYING_CLIP_BELOW_SELECTED_CLIP = b' Press Down Arrow to edit playing   clip'
    TOUCHSTRIP_PITCHBEND_MODE = b'                  Touchstrip Mode:  Pitchbend'
    TOUCHSTRIP_MODWHEEL_MODE = b'                  Touchstrip Mode:  Modwheel'
    COPIED_DRUM_PAD = b'     Pad %len=8,s copied.           Press destination pad to paste'
    PASTED_DRUM_PAD = b'     Pad %len=8,s duplicated to     %len=8,s'
    CANNOT_COPY_EMPTY_DRUM_PAD = b'                  Cannot copy empty drum pad'
    CANNOT_PASTE_TO_SOURCE_DRUM_PAD = b'                    Cannot paste to source drum pad'
    COPIED_STEP = b'     Note(s) copied.           Press destination step to paste'
    PASTED_STEP = b'     Note(s) duplicated.'
    COPIED_PAGE = b'     Page copied.           Press destination page to paste'
    PASTED_PAGE = b'     Page duplicated.'
    CANNOT_COPY_EMPTY_PAGE = b'                  Cannot copy empty page'
    CANNOT_PASTE_TO_SOURCE_PAGE = b'                    Cannot paste to source page'
    CANNOT_PASTE_FROM_STEP_TO_PAGE = b'                    Cannot paste from step to page'
    CANNOT_COPY_EMPTY_STEP = b'                  Cannot copy empty step'
    CANNOT_PASTE_TO_SOURCE_STEP = b'                    Cannot paste to source step'
    PAGE_CLEARED = b'                    Page cleared'
    CANNOT_CLEAR_EMPTY_PAGE = b'                    Cannot clear empty page'
    CANNOT_PASTE_FROM_PAGE_TO_STEP = b'                    Cannot paste from page to step'
    COPIED_CLIP = b'         %len=8,s copied.     Press destination clip  slot to paste'
    PASTED_CLIP = b'         %len=8,s duplicated to:    %len=17,s'
    CANNOT_COPY_EMPTY_CLIP = b' Cannot copy from empty clip slot'
    CANNOT_COPY_GROUP_SLOT = b'      Group clips cannot be copied'
    CANNOT_COPY_RECORDING_CLIP = b'      Cannot copy recording clip'
    CANNOT_COPY_AUDIO_CLIP_TO_MIDI_TRACK = b'     Please paste this audio clip       into an audio track'
    CANNOT_COPY_MIDI_CLIP_TO_AUDIO_TRACK = b'     Please paste this MIDI clip    into a MIDI track'
    CANNOT_PASTE_INTO_GROUP_SLOT = b'    A clip cannot be pasted into a  group track'
    LAYOUT_DRUMS_LOOP = b'          Drums:  Loop Selector'
    LAYOUT_DRUMS_LEVELS = b'          Drums:  16 Velocities'
    LAYOUT_DRUMS_64_PADS = b'          Drums:  64 Pads'
    LAYOUT_SLICING_LOOP = b'        Slicing:  Loop Selector'
    LAYOUT_SLICING_LEVELS = b'        Slicing:  16 Velocities'
    LAYOUT_SLICING_64_PADS = b'        Slicing:  64 Slices'
    ALTERNATE_LOOP_SELECTOR = b'          Loop Selector'
    ALTERNATE_16_VELOCITIES = b'          16 Velocities'
    ALTERNATE_56_PADS = b'          Loop Selector'
    ALTERNATE_PLAY_LOOP = b'          Loop Selector'
    ALTERNATE_SEQUENCE_LOOP = b'          Loop Selector'
    LAYOUT_MELODIC_PLAYING = b'        Melodic:  64 Notes'
    LAYOUT_MELODIC_SEQUENCER = b'        Melodic:  Sequencer'
    LAYOUT_MELODIC_32_PADS = b'        Melodic:  Sequencer  +  32  Notes'
    LAYOUT_MELODIC_32_PADS_LOOP_SELECTOR = b'        Loop Selector'
    LAYOUT_SESSION_VIEW = b' Session View'
    LAYOUT_SESSION_OVERVIEW = b' Session Overview'


_test_mode = __builtins__.get(b'TEST_MODE', False)
if not _test_mode:
    try:
        _this_module = sys.modules[__name__]
        _proto_list = filter(lambda a: a.startswith(b'PROTO_'), dir(_this_module))
        for attr in _proto_list:
            try:
                _local_consts = __import__(b'local_consts', globals(), locals(), [attr], -1)
                setattr(_this_module, attr, getattr(_local_consts, attr))
            except AttributeError:
                pass

    except ImportError:
        pass