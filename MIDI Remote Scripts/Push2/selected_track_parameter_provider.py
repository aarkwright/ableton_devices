# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\selected_track_parameter_provider.py
# Compiled at: 2019-04-23 16:19:13
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import ParameterInfo
from pushbase.selected_track_parameter_provider import SelectedTrackParameterProvider as SelectedTrackParameterProviderBase
from .parameter_mapping_sensitivities import parameter_mapping_sensitivity, fine_grain_parameter_mapping_sensitivity

class SelectedTrackParameterProvider(SelectedTrackParameterProviderBase):

    def _create_parameter_info(self, parameter, name):
        assert name is not None
        return ParameterInfo(name=name, parameter=parameter, default_encoder_sensitivity=parameter_mapping_sensitivity(parameter), fine_grain_encoder_sensitivity=fine_grain_parameter_mapping_sensitivity(parameter))