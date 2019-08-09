# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\auto_filter.py
# Compiled at: 2019-04-23 16:19:13
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import EventObject, listens, liveobj_valid
from ableton.v2.control_surface import LiveObjectDecorator, get_parameter_by_name
from .device_decoration import DeviceSwitchOption
from .device_component import DeviceComponentWithTrackColorViewData
from .visualisation_settings import VisualisationGuides

class AutoFilterDeviceDecorator(EventObject, LiveObjectDecorator):

    def __init__(self, *a, **k):
        super(AutoFilterDeviceDecorator, self).__init__(*a, **k)
        self.__on_parameters_changed.subject = self._live_object
        self.slope_option = DeviceSwitchOption(name=b'Slope', parameter=get_parameter_by_name(self, b'Slope'))
        self.register_disconnectables(self.options)

    @property
    def options(self):
        return (
         self.slope_option,)

    @listens(b'parameters')
    def __on_parameters_changed(self):
        self.slope_option.set_parameter(get_parameter_by_name(self, b'Slope'))


class AutoFilterDeviceComponent(DeviceComponentWithTrackColorViewData):

    def _parameter_touched(self, parameter):
        self._update_visualisation_view_data(self._filter_visualisation_data())

    def _parameter_released(self, parameter):
        self._update_visualisation_view_data(self._filter_visualisation_data())

    def parameters_changed(self):
        self._update_visualisation_view_data(self._filter_visualisation_data())

    def _set_bank_index(self, bank):
        super(AutoFilterDeviceComponent, self)._set_bank_index(bank)
        self._update_visualisation_view_data(self._filter_visualisation_data())
        self.notify_visualisation_visible()
        self.notify_shrink_parameters()

    def _initial_visualisation_view_data(self):
        view_data = super(AutoFilterDeviceComponent, self)._initial_visualisation_view_data()
        view_data.update(self._filter_visualisation_data())
        return view_data

    def _filter_visualisation_data(self):
        touched_parameters = [ self.parameters[button.index] for button in self.parameter_touch_buttons if button.is_pressed
                             ]
        parameter_names = [
         b'Filter Type',
         b'Filter Type (Legacy)',
         b'Frequency',
         b'Resonance',
         b'Resonance (Legacy)']
        filter_focus = any([ parameter.parameter.name in parameter_names for parameter in touched_parameters if liveobj_valid(parameter.parameter)
                           ])
        return {b'FilterLeft': VisualisationGuides.light_left_x(0), 
           b'FilterRight': VisualisationGuides.light_right_x(2), 
           b'FilterFocus': filter_focus}

    @listens(b'oscillator_index')
    def __on_selected_oscillator_changed(self):
        self._update_visualisation_view_data(self._filter_visualisation_data())

    @property
    def _visualisation_visible(self):
        return self._bank != None and self._bank.index in (0, 1)

    @property
    def _shrink_parameters(self):
        return [ self._visualisation_visible and index < 3 for index in xrange(8) ]