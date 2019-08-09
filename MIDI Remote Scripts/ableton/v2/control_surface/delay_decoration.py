# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\delay_decoration.py
# Compiled at: 2019-05-10 18:21:20
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import EventObject, listens, liveobj_valid
from ableton.v2.control_surface import LiveObjectDecorator, NotifyingList, get_parameter_by_name
from .internal_parameter import EnumWrappingParameter

class ChannelType(int):
    pass


ChannelType.left_right = ChannelType(0)
ChannelType.left = ChannelType(1)
ChannelType.right = ChannelType(2)

class LinkedState(int):
    pass


LinkedState.unlinked = LinkedState(0)
LinkedState.linked = LinkedState(1)

class DelayDeviceDecorator(LiveObjectDecorator, EventObject):
    sync_modes = ('Time', 'Sync')
    link_modes = ('Linked', 'Unlinked')

    def __init__(self, *a, **k):
        super(DelayDeviceDecorator, self).__init__(*a, **k)
        self._channel_type_provider = NotifyingList(available_values=[
         b'L+R', b'Left', b'Right'], default_value=ChannelType.left_right)
        self._additional_parameters = self._create_parameters()
        self.register_disconnectables(self._additional_parameters)

    @property
    def parameters(self):
        return tuple(self._live_object.parameters) + self._additional_parameters

    def _create_parameters(self):
        self._channel_switch = EnumWrappingParameter(name=b'Channel', parent=self, values_host=self._channel_type_provider, index_property_host=self._channel_type_provider, values_property=b'available_values', index_property=b'index', value_type=ChannelType)
        self._delay_line_link_parameter = get_parameter_by_name(self, b'Link')
        self.__on_channel_switch_changed.subject = self._channel_switch
        self.__on_linked_changed.subject = self._delay_line_link_parameter
        self.__on_linked_changed()
        return (
         self._channel_switch,
         EnumWrappingParameter(name=b'L Sync Enum', parent=self, values_host=self, values_property=b'sync_modes', index_property_host=get_parameter_by_name(self, b'L Sync'), index_property=b'value', to_index_conversion=lambda index: int(index), from_index_conversion=lambda index: int(index)),
         EnumWrappingParameter(name=b'R Sync Enum', parent=self, values_host=self, values_property=b'sync_modes', index_property_host=get_parameter_by_name(self, b'R Sync'), index_property=b'value', to_index_conversion=lambda index: int(index), from_index_conversion=lambda index: int(index)),
         EnumWrappingParameter(name=b'Link Switch', parent=self, values_host=self, values_property=b'link_modes', index_property_host=self._delay_line_link_parameter, index_property=b'value', to_index_conversion=lambda index: int(not index), from_index_conversion=lambda index: int(not index)))

    def _linked_state_needs_updating(self):
        if liveobj_valid(self._delay_line_link_parameter):
            is_delay_line_linked = self._delay_line_link_parameter.value == LinkedState.linked
            is_channel_switch_linked = self._channel_switch.value == ChannelType.left_right
            return is_delay_line_linked != is_channel_switch_linked

    @listens(b'value')
    def __on_channel_switch_changed(self):
        if self._linked_state_needs_updating():
            self._delay_line_link_parameter.value = LinkedState.linked if self._channel_switch.value == ChannelType.left_right else LinkedState.unlinked

    @listens(b'value')
    def __on_linked_changed(self):
        if self._linked_state_needs_updating():
            self._channel_switch.value = ChannelType.left_right if self._delay_line_link_parameter.value == LinkedState.linked else ChannelType.left