# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\delay.py
# Compiled at: 2019-05-10 18:21:20
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import DelayDeviceDecorator as DelayDeviceDecoratorBase, get_parameter_by_name
from .device_options import DeviceOnOffOption, DeviceSwitchOption
from .device_component import ButtonRange, DeviceComponentWithTrackColorViewData
from .visualisation_settings import VisualisationGuides

class DelayDeviceDecorator(DelayDeviceDecoratorBase):

    def __init__(self, *a, **k):
        super(DelayDeviceDecorator, self).__init__(*a, **k)
        self.sync_l_option = DeviceOnOffOption(name=b'L Delay Sync', property_host=get_parameter_by_name(self, b'L Sync'))
        self.sync_r_option = DeviceOnOffOption(name=b'R Delay Sync', property_host=get_parameter_by_name(self, b'R Sync'))
        self.filter_on_option = DeviceOnOffOption(name=b'Filter', property_host=get_parameter_by_name(self, b'Filter On'))
        self.freeze_on_option = DeviceOnOffOption(name=b'Freeze', property_host=get_parameter_by_name(self, b'Freeze'))
        self.smoothing_mode = DeviceSwitchOption(name=b'Delay Mode', parameter=get_parameter_by_name(self, b'Delay Mode'), labels=[
         b'Repitch', b'Fade', b'Jump'])
        self.register_disconnectables(self._additional_parameters)
        self.register_disconnectables(self.options)

    @property
    def options(self):
        return (
         self.sync_l_option,
         self.sync_r_option,
         self.filter_on_option,
         self.freeze_on_option,
         self.smoothing_mode)


class DelayDeviceComponent(DeviceComponentWithTrackColorViewData):
    VISUALISATION_POSITION_IN_BANKS = {0: ButtonRange(4, 5), 
       2: ButtonRange(0, 1)}

    def _parameter_touched(self, parameter):
        self._update_visualisation_view_data(self._adjustment_view_data)

    def _parameter_released(self, parameter):
        self._update_visualisation_view_data(self._adjustment_view_data)

    @property
    def _adjustment_view_data(self):
        adjusting_filter = False
        touched_parameters = [ self.parameters[button.index] for button in self.parameter_touch_buttons if button.is_pressed
                             ]
        for parameter in touched_parameters:
            if parameter.name.startswith(b'Filter'):
                adjusting_filter = True

        return {b'AdjustingFilter': adjusting_filter}

    @property
    def _visualisation_visible(self):
        return self._bank.index in self.VISUALISATION_POSITION_IN_BANKS

    @property
    def _shrink_parameters(self):
        if self.visualisation_visible:
            visualisation_position = self._get_current_visualisation_position()

            def is_shrunk(parameter_index):
                return visualisation_position.left_index <= parameter_index <= visualisation_position.right_index

            return [ is_shrunk(parameter_index) for parameter_index in range(8) ]
        return [
         False] * 8

    def _set_bank_index(self, bank):
        super(DelayDeviceComponent, self)._set_bank_index(bank)
        self._update_visualisation_view_data(self._get_current_view_data)
        self._update_visualisation_view_data(self._adjustment_view_data)
        self.notify_shrink_parameters()
        self.notify_visualisation_visible()

    def _get_current_visualisation_position(self):
        return self.VISUALISATION_POSITION_IN_BANKS.get(self._bank.index, ButtonRange(0, 0))

    @property
    def _get_current_view_data(self):
        position = self._get_current_visualisation_position()
        start_position_in_px = VisualisationGuides.light_left_x(position.left_index)
        end_position_in_px = VisualisationGuides.light_right_x(position.right_index)
        return {b'VisualisationStart': start_position_in_px, 
           b'VisualisationWidth': end_position_in_px - start_position_in_px, 
           b'IsVisualisationVisible': self._visualisation_visible}

    def _initial_visualisation_view_data(self):
        view_data = super(DelayDeviceComponent, self)._initial_visualisation_view_data()
        view_data.update(self._get_current_view_data)
        view_data.update(self._adjustment_view_data)
        return view_data