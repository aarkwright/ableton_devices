# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\device_parameter_component.py
# Compiled at: 2019-04-23 16:19:13
from __future__ import absolute_import, print_function, unicode_literals
from itertools import chain, repeat, izip_longest
import Live
from ableton.v2.base import listens_group, listens
from ableton.v2.control_surface import Component, ParameterProvider
from ableton.v2.control_surface.components import DisplayingDeviceParameterComponent as DeviceParameterComponentBase
from ableton.v2.control_surface.control import ControlList, MappedSensitivitySettingControl
from ableton.v2.control_surface.elements import DisplayDataSource
from . import consts
AutomationState = Live.DeviceParameter.AutomationState

def graphic_bar_for_parameter(parameter):
    if parameter.min == -1 * parameter.max:
        return consts.GRAPH_PAN
    if parameter.is_quantized:
        return consts.GRAPH_SIN
    return consts.GRAPH_VOL


def convert_parameter_value_to_graphic(param, param_to_value=lambda p: p.value):
    if param != None:
        param_range = param.max - param.min
        param_bar = graphic_bar_for_parameter(param)
        graph_range = len(param_bar) - 1
        value = int(float(param_to_value(param) - param.min) / param_range * graph_range)
        graphic_display_string = param_bar[value]
    else:
        graphic_display_string = b' '
    return graphic_display_string


class DeviceParameterComponent(DeviceParameterComponentBase):
    """
    Maps the display and encoders to the parameters provided by a
    ParameterProvider.
    """

    def __init__(self, *a, **k):
        self._parameter_graphic_data_sources = map(DisplayDataSource, ('', '', '',
                                                                       '', '', '',
                                                                       '', ''))
        super(DeviceParameterComponent, self).__init__(*a, **k)

    def set_graphic_display_line(self, line):
        self._set_display_line(line, self._parameter_graphic_data_sources)

    def clear_display(self):
        super(DeviceParameterComponent, self).clear_display()
        for source in self._parameter_graphic_data_sources:
            source.set_display_string(b'')

    def _update_parameters(self):
        super(DeviceParameterComponent, self)._update_parameters()
        if self.is_enabled():
            self._on_parameter_automation_state_changed.replace_subjects(self.parameters)

    @listens_group(b'automation_state')
    def _on_parameter_automation_state_changed(self, parameter):
        self._update_parameter_names()
        self._update_parameter_values()

    def _update_parameter_values(self):
        super(DeviceParameterComponent, self)._update_parameter_values()
        if self.is_enabled():
            for param, data_source in izip_longest(self.parameters, self._parameter_graphic_data_sources):
                graph = convert_parameter_value_to_graphic(param, self.parameter_to_value)
                if data_source:
                    data_source.set_display_string(graph)

    def info_to_name(self, info):
        parameter = info and info.parameter
        name = info and info.name or b''
        if parameter and parameter.automation_state != AutomationState.none:
            name = consts.CHAR_FULL_BLOCK + name
        return name

    def parameter_to_string(self, parameter):
        s = b'' if parameter == None else unicode(parameter)
        if parameter and parameter.automation_state == AutomationState.overridden:
            s = b'[%s]' % s
        return s