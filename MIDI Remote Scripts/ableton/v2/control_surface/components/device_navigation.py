# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\components\device_navigation.py
# Compiled at: 2019-05-15 03:17:58
from __future__ import absolute_import, print_function, unicode_literals
from contextlib import contextmanager
from itertools import ifilter, imap, chain
from functools import partial
from multipledispatch import dispatch
import Live
from ...base import find_if, first, index_if, listenable_property, listens, listens_group, liveobj_changed, liveobj_valid, EventObject, SlotGroup, task
from ...control_surface import device_to_appoint
from ...control_surface.control import control_list, StepEncoderControl
from ...control_surface.mode import Component, ModesComponent
from .item_lister import ItemListerComponent, ItemProvider

def is_empty_rack(rack):
    return rack.can_have_chains and len(rack.chains) == 0


def nested_device_parent(device):
    if device.can_have_chains and device.view.is_showing_chain_devices and not device.view.is_collapsed:
        return device.view.selected_chain
    else:
        return


def collect_devices(track_or_chain, nesting_level=0):
    chain_devices = track_or_chain.devices if liveobj_valid(track_or_chain) else []
    devices = []
    for device in chain_devices:
        devices.append((device, nesting_level))
        devices.extend(collect_devices(nested_device_parent(device), nesting_level=nesting_level + 1))

    return devices


class FlattenedDeviceChain(ItemProvider):

    def __init__(self, collect_devices_fun=collect_devices, *a, **k):
        super(FlattenedDeviceChain, self).__init__(*a, **k)
        self._device_parent = None
        self._devices = []
        self._selected_item = None
        self._collect_devices = collect_devices_fun

        def make_slot_group(event):
            slot_group = SlotGroup(self._update_devices, event)
            return self.register_disconnectable(slot_group)

        self._devices_changed = make_slot_group(b'devices')
        self._selected_chain_changed = make_slot_group(b'selected_chain')
        self._selected_pad_changed = make_slot_group(b'selected_drum_pad')
        self._collapsed_state_changed = make_slot_group(b'is_collapsed')
        self._chain_devices_visibility_changed = make_slot_group(b'is_showing_chain_devices')
        return

    @property
    def items(self):
        return self._devices

    def _get_selected_item(self):
        return self._selected_item

    def _set_selected_item(self, device):
        if liveobj_changed(self._selected_item, device):
            self._selected_item = device
            self.notify_selected_item()

    selected_item = property(_get_selected_item, _set_selected_item)

    @property
    def has_invalid_selection(self):
        return not liveobj_valid(self._selected_item)

    def set_device_parent(self, parent):
        self._device_parent = parent
        self._update_devices()

    def _update_devices(self, *_):
        self._devices = self._collect_devices(self._device_parent)
        self._update_listeners()
        self.notify_items()

    def _update_listeners(self):

        def get_rack_views(racks):
            return map(lambda x: first(x).view, racks)

        racks = filter(lambda x: getattr(first(x), b'can_have_chains', False), self._devices)
        rack_views = get_rack_views(racks)
        device_parents = chain(imap(lambda x: x.selected_chain, rack_views), [
         self._device_parent])

        def is_empty_pad_drum_rack(item):
            rack = first(item)
            return rack.can_have_drum_pads and rack.view.selected_drum_pad and len(rack.view.selected_drum_pad.chains) == 0

        empty_pad_drum_rack_views = get_rack_views(ifilter(is_empty_pad_drum_rack, racks))
        self._devices_changed.replace_subjects(device_parents)
        self._selected_chain_changed.replace_subjects(rack_views)
        self._collapsed_state_changed.replace_subjects(rack_views)
        self._chain_devices_visibility_changed.replace_subjects(rack_views)
        self._selected_pad_changed.replace_subjects(empty_pad_drum_rack_views)


class DeviceNavigationComponent(ItemListerComponent):

    def __init__(self, device_component=None, item_provider=None, *a, **k):
        assert device_component is not None
        self._flattened_chain = item_provider or FlattenedDeviceChain()
        super(DeviceNavigationComponent, self).__init__(item_provider=self._flattened_chain, *a, **k)
        self._device_component = device_component
        self.__on_device_changed.subject = device_component
        self._last_pressed_button_index = -1
        self._selected_on_previous_press = None
        self.register_disconnectable(self._flattened_chain)
        self._on_selected_track_changed()
        self._on_selected_track_changed.subject = self.song.view
        self.__on_device_changed()
        self._update_button_colors()
        return

    @property
    def selected_item(self):
        return self.item_provider.selected_item

    def _on_select_button_pressed(self, button):
        device_or_pad = self.items[button.index].item
        self._select_item(self.items[button.index].item)

    def _show_selected_item(self):
        selected_item = self.item_provider.selected_item
        if selected_item is not None:
            items = self.item_provider.items
            if len(items) > self._num_visible_items:
                selected_index = index_if(lambda i: i[0] == selected_item, items)
                if selected_index >= self._num_visible_items + self.item_offset - 1 and selected_index < len(items) - 1:
                    self.item_offset = selected_index - self._num_visible_items + 2
                elif selected_index > 0 and selected_index <= self.item_offset:
                    self.item_offset = selected_index - 1
        return

    def _current_track(self):
        return self.song.view.selected_track

    @listens(b'selected_track')
    def _on_selected_track_changed(self):
        self._update_selected_track()

    def _update_selected_track(self):
        self._selected_track = self.song.view.selected_track
        selected_track = self._current_track()
        self.reset_offset()
        self._flattened_chain.set_device_parent(selected_track)
        self._device_selection_in_track_changed.subject = selected_track.view
        self._restore_selection(selected_track)

    def _restore_selection(self, selected_track):
        to_select = selected_track.view.selected_device
        self._select_item(to_select)

    def _select_item(self, device_or_pad):
        if device_or_pad:
            self._do_select_item(device_or_pad)
        self._update_item_provider(device_or_pad)

    def _do_select_item(self, device):
        appointed_device = device_to_appoint(device)
        self._appoint_device(appointed_device)
        self.song.view.select_device(device, False)
        self.song.appointed_device = appointed_device

    def _appoint_device(self, device):
        self._device_component.set_device(device)

    @listens(b'device')
    def __on_device_changed(self):
        self._update_device()

    def _update_device(self):
        self._update_item_provider(self._device_component.device())

    @listens(b'selected_device')
    def _device_selection_in_track_changed(self):
        new_selection = self.song.view.selected_track.view.selected_device
        self._update_item_provider(new_selection)

    def _update_item_provider(self, selection):
        self._flattened_chain.selected_item = selection