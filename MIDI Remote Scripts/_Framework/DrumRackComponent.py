# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\DrumRackComponent.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
from itertools import ifilter
from .ControlSurfaceComponent import ControlSurfaceComponent
from .Dependency import depends
from .Util import product
NUM_PADS_X = 4
NUM_PADS_Y = 4

def _validate_matrix(matrix):
    if matrix.width() > NUM_PADS_X or matrix.height() > NUM_PADS_Y:
        raise RuntimeError(b'The provided button matrix should not be bigger than %dx%d' % (
         NUM_PADS_X, NUM_PADS_Y))


class DrumRackComponent(ControlSurfaceComponent):

    @depends(set_pad_translations=None, request_rebuild_midi_map=None)
    def __init__(self, set_pad_translations=None, request_rebuild_midi_map=None, *a, **k):
        super(DrumRackComponent, self).__init__(*a, **k)
        assert callable(set_pad_translations)
        assert callable(request_rebuild_midi_map)
        self._set_pad_translations = set_pad_translations
        self._request_rebuild_midi_map = request_rebuild_midi_map

    def _create_and_set_pad_translations(self, matrix):

        def create_translation_entry((y, x)):
            button = matrix.get_button(x, y)
            return (
             x, y + NUM_PADS_Y - matrix.height(),
             button.message_identifier() if button is not None else 0,
             button.message_channel() if button is not None else 0)

        translations = map(create_translation_entry, product(xrange(matrix.height()), xrange(matrix.width())))
        self._set_pad_translations(tuple(translations))

    def set_pads(self, matrix):
        if matrix is not None:
            _validate_matrix(matrix)
            self._create_and_set_pad_translations(matrix)
            for button in ifilter(None, matrix):
                button.suppress_script_forwarding = True

        else:
            self._set_pad_translations(None)
        self._request_rebuild_midi_map()
        return