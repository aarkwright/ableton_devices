# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\components\device_parameters.py
# Compiled at: 2019-05-15 03:17:58
from __future__ import absolute_import, print_function, unicode_literals
from itertools import chain, izip_longest, repeat
from ableton.v2.base import listens, listens_group
from ableton.v2.control_surface import Component, ParameterProvider
from ableton.v2.control_surface.control import ControlList, MappedSensitivitySettingControl
from ableton.v2.control_surface.elements import DisplayDataSource

class DeviceParameterComponent(Component):
    controls = ControlList(MappedSensitivitySettingControl, 8)

    def __init__(self, parameter_provider=None, *a, **k):
        super(DeviceParameterComponent, self).__init__(*a, **k)
        self.parameter_provider = parameter_provider

    def _get_parameter_provider(self):
        return self._parameter_provider

    def _set_parameter_provider(self, provider):
        self._parameter_provider = provider or ParameterProvider()
        self._on_parameters_changed.subject = self._parameter_provider
        self._update_parameters()
        self._on_parameter_provider_changed(provider)

    parameter_provider = property(_get_parameter_provider, _set_parameter_provider)

    def set_parameter_controls(self, encoders):
        self.controls.set_control_element(encoders)
        self._connect_parameters()

    def _connect_parameters(self):
        parameters = self._parameter_provider.parameters[:self.controls.control_count]
        for control, parameter_info in map(None, self.controls, parameters):
            parameter = parameter_info.parameter if parameter_info else None
            control.mapped_parameter = parameter
            if parameter:
                control.update_sensitivities(parameter_info.default_encoder_sensitivity, parameter_info.fine_grain_encoder_sensitivity)

        return

    def _update_parameters(self):
        if self.is_enabled():
            self._connect_parameters()

    @listens(b'parameters')
    def _on_parameters_changed(self):
        self._update_parameters()

    def _on_parameter_provider_changed(self, provider):
        pass

    def update(self):
        super(DeviceParameterComponent, self).update()
        self._update_parameters()


class DisplayingDeviceParameterComponent(DeviceParameterComponent):

    def __init__(self, *a, **k):
        self._parameter_name_data_sources = map(DisplayDataSource, ('', '', '', '',
                                                                    '', '', '', ''))
        self._parameter_value_data_sources = map(DisplayDataSource, ('', '', '', '',
                                                                     '', '', '',
                                                                     ''))
        super(DisplayingDeviceParameterComponent, self).__init__(*a, **k)

    @property
    def parameters(self):
        return map(lambda p: p and p.parameter, self._parameter_provider.parameters)

    @property
    def parameter_names(self):
        return map(lambda p: p and p.name or b'', self.parameters)

    def set_name_display_line(self, line):
        self._set_display_line(line, self._parameter_name_data_sources)

    def set_value_display_line(self, line):
        self._set_display_line(line, self._parameter_value_data_sources)

    def _set_display_line(self, line, sources):
        if line:
            line.set_num_segments(len(sources))
            for segment in xrange(len(sources)):
                line.segment(segment).set_data_source(sources[segment])

    def clear_display(self):
        for source in chain(self._parameter_name_data_sources, self._parameter_value_data_sources):
            source.set_display_string(b'')

    def _update_parameters(self):
        super(DisplayingDeviceParameterComponent, self)._update_parameters()
        if self.is_enabled():
            parameters = self.parameters
            self._on_parameter_name_changed.replace_subjects(parameters)
            self._on_parameter_value_changed.replace_subjects(parameters)
            self._update_parameter_names()
            self._update_parameter_values()

    @listens_group(b'name')
    def _on_parameter_name_changed(self, parameter):
        self._update_parameter_names()

    @listens_group(b'value')
    def _on_parameter_value_changed(self, parameter):
        self._update_parameter_values()

    def _update_parameter_names(self):
        if self.is_enabled():
            params = zip(chain(self.parameter_provider.parameters, repeat(None)), self._parameter_name_data_sources)
            for info, name_data_source in params:
                name = self.info_to_name(info)
                name_data_source.set_display_string(name or b'')

        return

    def _update_parameter_values(self):
        if self.is_enabled():
            for parameter, data_source in izip_longest(self.parameters, self._parameter_value_data_sources):
                value_string = self.parameter_to_string(parameter)
                if data_source:
                    data_source.set_display_string(value_string)

    def info_to_name(self, info):
        parameter = info and info.parameter
        return info and info.name or b''

    def parameter_to_string(self, parameter):
        if parameter == None:
            return b''
        else:
            return unicode(parameter)

    def parameter_to_value(self, parameter):
        return parameter.value