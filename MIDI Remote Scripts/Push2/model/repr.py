# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\model\repr.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
import re
from functools import partial
from ableton.v2.base import EventObject, Slot, EventError, find_if, listenable_property, listens, liveobj_valid
from ..device_parameter_icons import get_image_filenames, get_image_filenames_from_ids
DEVICE_TYPES_WITH_PRESET_NAME = [
 b'InstrumentGroupDevice',
 b'DrumGroupDevice',
 b'AudioEffectGroupDevice',
 b'MidiEffectGroupDevice',
 b'ProxyInstrumentDevice',
 b'ProxyAudioEffectDevice',
 b'MxDeviceInstrument',
 b'MxDeviceAudioEffect',
 b'MxDeviceMidiEffect']
display_pattern = re.compile(b'\\d|°|/|\\%|\\.|\\:|\\-|\\+|inf')
unit_pattern = re.compile(b'inf\\s*[A-z]+$|\\d\\s*[A-z]+$')
string_pattern = re.compile(b'[A-z]+$')

def _get_parameter_by_name(device, name):
    parameters = device.parameters if liveobj_valid(device) else []
    return find_if(lambda x: x.name == name, parameters)


def _try_to_round_number(parameter_string):
    value_as_number = None
    try:
        value_as_number = int(parameter_string)
    except ValueError:
        pass

    if value_as_number is None:
        try:
            value_as_number = round(float(parameter_string), 2)
        except ValueError:
            pass

    return value_as_number


def get_parameter_display_value(parameter):
    parameter_string = unicode(parameter)
    found_string = (b'').join(display_pattern.findall(parameter_string))
    if found_string in ('inf', '-inf'):
        parameter_display = found_string
    else:
        value = _try_to_round_number(found_string)
        parameter_display = unicode(value) if value is not None else parameter_string
        if found_string.startswith(b'+'):
            parameter_display = b'+' + parameter_display
    return parameter_display


def get_parameter_unit(parameter):
    parameter_string = unicode(parameter)
    value = unit_pattern.findall(parameter_string)
    if value:
        return (b'').join(string_pattern.findall(value[0]))
    return b''


def strip_formatted_string(str):
    """
    Remove multiple whitespaces (including new lines) and whitespaces at the beginning
    and end of the given string.
    """
    return re.sub(b'\\s\\s+', b' ', str).strip()


def convert_color_index(color_index):
    from ..colors import UNCOLORED_INDEX
    if color_index is None:
        return UNCOLORED_INDEX
    else:
        return color_index


def determine_color_label_index(item):
    """
    Returns a number >= 0 if the given item is a color label (aka Collection),
    -1 otherwise. The number represents the index of the color label in the list of
    *all* color labels (i.e. including currently invisible/disabled labels)
    """
    match = re.search(b'^color:colors=(\\d+)$', item.uri)
    is_color_label = match is not None
    if is_color_label:
        return int(match.group(1)) - 1
    else:
        return -1


class ModelAdapter(EventObject):

    def __init__(self, adaptee=None, *a, **k):
        assert liveobj_valid(adaptee)
        super(ModelAdapter, self).__init__(*a, **k)
        self._adaptee = adaptee

    def is_valid(self):
        return liveobj_valid(self._adaptee)

    def __getattr__(self, name):
        if name in self.__dict__ or name in self.__class__.__dict__:
            return object.__getattribute__(self, name)
        return getattr(self._adaptee, name)

    @property
    def _live_ptr(self):
        if hasattr(self._adaptee, b'_live_ptr'):
            return self._adaptee._live_ptr
        return id(self._adaptee)

    def _alias_observable_property(self, prop_name, alias_name, getter=None):
        default_getter = lambda self_: getattr(self_._adaptee, prop_name)
        aliased_prop = property(getter or default_getter)
        setattr(self.__class__, alias_name, aliased_prop)
        notifier = getattr(self, b'notify_' + alias_name)
        self.register_slot(Slot(self._adaptee, notifier, prop_name))


class ClipAdapter(ModelAdapter):

    def __init__(self, *a, **k):
        super(ClipAdapter, self).__init__(*a, **k)
        self.register_slot(self._adaptee, self.notify_name, b'name')

    @listenable_property
    def name(self):
        name = self._adaptee.name
        if len(name.strip()) == 0:
            name = b'MIDI clip' if self._adaptee.is_midi_clip else b'Audio clip'
        return name

    @property
    def positions(self):
        return getattr(self._adaptee, b'positions', None)

    @property
    def warping(self):
        return self._adaptee.is_audio_clip and self._adaptee.warping


class DeviceParameterAdapter(ModelAdapter):
    __events__ = ('hasAutomation', )

    def __init__(self, *a, **k):
        super(DeviceParameterAdapter, self).__init__(*a, **k)
        self._alias_observable_property(b'automation_state', b'hasAutomation', getter=lambda self_: self_._has_automation())
        self.register_slot(self._adaptee, self.notify_displayValue, b'value')
        self.register_slot(self._adaptee, self.notify_unit, b'value')
        self.register_slot(self._adaptee, self.notify_automationActive, b'automation_state')
        self.register_slot(self._adaptee, self.notify_isActive, b'state')
        try:
            self.register_slot(self._adaptee, self.notify_valueItems, b'value_items')
        except EventError:
            pass

    @listenable_property
    def valueItems(self):
        if self._adaptee.is_quantized:
            return self._adaptee.value_items
        return []

    def _get_image_filenames(self, small_images=False):
        device = self.canonical_parent
        if not hasattr(device, b'class_name'):
            return []
        else:
            custom_images = None
            if liveobj_valid(device):
                try:
                    custom_images = device.get_value_item_icons(getattr(self._adaptee, b'original_parameter', self._adaptee))
                except (AttributeError, RuntimeError):
                    pass

            if custom_images is not None:
                return get_image_filenames_from_ids(custom_images, small_images)
            return get_image_filenames(self.original_name, device.class_name, small_images)
            return

    @listenable_property
    def valueItemImages(self):
        return self._get_image_filenames(small_images=False)

    @listenable_property
    def valueItemSmallImages(self):
        result = self._get_image_filenames(small_images=True)
        return result

    @listenable_property
    def displayValue(self):
        return get_parameter_display_value(self._adaptee)

    @listenable_property
    def unit(self):
        return get_parameter_unit(self._adaptee)

    def _has_automation(self):
        no_automation = 0
        return self._adaptee.automation_state != no_automation

    @listenable_property
    def automationActive(self):
        active_automation = 1
        return self._adaptee.automation_state == active_automation

    @listenable_property
    def isActive(self):
        enabled_state = 0
        return self._adaptee.state == enabled_state


class EditModeOptionAdapter(ModelAdapter):
    __events__ = ('activeIndex', 'choices')

    def __init__(self, *a, **k):
        super(EditModeOptionAdapter, self).__init__(*a, **k)
        if hasattr(self._adaptee, b'active_index'):
            self._alias_observable_property(b'active_index', b'activeIndex', getter=lambda self_: getattr(self_._adaptee, b'active_index', 0))
        self._alias_observable_property(b'default_label', b'choices', getter=lambda self_: self_._choices)

    @property
    def activeIndex(self):
        return 0

    @property
    def _choices(self):
        return getattr(self._adaptee, b'labels', [self._adaptee.default_label])


class SimplerDeviceAdapter(ModelAdapter):

    def __init__(self, *a, **k):
        super(SimplerDeviceAdapter, self).__init__(*a, **k)
        self.register_slot(self._adaptee.view, self.notify_selected_slice, b'selected_slice')
        get_parameter = partial(_get_parameter_by_name, self._adaptee)
        self.sample_start = get_parameter(b'S Start')
        self.sample_length = get_parameter(b'S Length')
        self.loop_length = get_parameter(b'S Loop Length')
        self.loop_on = get_parameter(b'S Loop On')
        self.zoom = get_parameter(b'Zoom')
        self.__on_sample_changed.subject = self._adaptee
        self.__on_sample_changed()

    def _is_slicing(self):
        return self._adaptee.playback_mode == 2

    def _get_slice_times(self):
        slice_times = []
        if self._is_slicing() and liveobj_valid(self._adaptee.sample):
            try:
                slice_times = self._adaptee.sample.slices
            except RuntimeError:
                pass

        return slice_times

    @listens(b'sample')
    def __on_sample_changed(self):
        self.register_slot(self._adaptee.sample, self.notify_start_marker, b'start_marker')
        self.register_slot(self._adaptee.sample, self.notify_end_marker, b'end_marker')
        self.register_slot(self._adaptee.sample, self.notify_slices, b'slices')
        self.register_slot(self._adaptee.sample, self.notify_slicing_sensitivity, b'slicing_sensitivity')
        self.register_slot(self._adaptee.sample, self.notify_gain, b'gain')

    @listenable_property
    def slices(self):

        class SlicePoint(object):

            def __init__(self, __id__, time):
                self.__id__ = __id__
                self.time = time

        return [ SlicePoint(time, time) for time in self._get_slice_times() ]

    @listenable_property
    def selected_slice(self):
        return find_if(lambda s: s.time == self.view.selected_slice, self.slices)

    @listenable_property
    def start_marker(self):
        if liveobj_valid(self._adaptee) and liveobj_valid(self._adaptee.sample):
            return self._adaptee.sample.start_marker
        return 0

    @listenable_property
    def end_marker(self):
        if liveobj_valid(self._adaptee) and liveobj_valid(self._adaptee.sample):
            return self._adaptee.sample.end_marker
        return 0

    @listenable_property
    def slicing_sensitivity(self):
        if liveobj_valid(self._adaptee) and liveobj_valid(self._adaptee.sample):
            return self._adaptee.sample.slicing_sensitivity
        return 0.0

    @listenable_property
    def gain(self):
        if liveobj_valid(self._adaptee) and liveobj_valid(self._adaptee.sample):
            return self._adaptee.sample.gain
        return 0.0

    @listenable_property
    def warping(self):
        if liveobj_valid(self._adaptee) and liveobj_valid(self._adaptee.sample):
            return self._adaptee.sample.warping
        return False


class VisibleAdapter(ModelAdapter):

    def __init__(self, adaptee=None, *a, **k):
        super(VisibleAdapter, self).__init__(adaptee=adaptee, *a, **k)
        self.__on_enabled_changed.subject = adaptee

    @listenable_property
    def visible(self):
        return self._adaptee.is_enabled()

    @listens(b'enabled')
    def __on_enabled_changed(self, enabled):
        self.notify_visible()


class TrackMixAdapter(VisibleAdapter):
    __events__ = ('scrollOffset', )

    def __init__(self, *a, **k):
        super(TrackMixAdapter, self).__init__(*a, **k)
        self._alias_observable_property(b'scroll_offset', b'scrollOffset')


class TrackControlAdapter(VisibleAdapter):
    __events__ = ('track_control_mode', )

    def __init__(self, *a, **k):
        super(TrackControlAdapter, self).__init__(*a, **k)
        self._alias_observable_property(b'selected_mode', b'track_control_mode')


class OptionsListAdapter(VisibleAdapter):
    __events__ = ('selectedItem', )

    def __init__(self, *a, **k):
        super(OptionsListAdapter, self).__init__(*a, **k)
        self._alias_observable_property(b'selected_item', b'selectedItem')


class ItemListAdapter(VisibleAdapter):
    __events__ = ('selectedItem', )

    def __init__(self, *a, **k):
        super(ItemListAdapter, self).__init__(*a, **k)
        self.__on_selected_item_changed.subject = self._adaptee.item_provider

    @listens(b'selected_item')
    def __on_selected_item_changed(self):
        self.notify_selectedItem()

    @property
    def selectedItem(self):
        return self._adaptee.item_provider.selected_item


class ItemSlotAdapter(ModelAdapter):

    @property
    def icon(self):
        return getattr(self._adaptee, b'icon', b'')


class DeviceAdapter(ModelAdapter):
    __events__ = ('is_active', )

    def __init__(self, *a, **k):
        from ..device_util import is_drum_pad, find_chain_or_track, find_rack
        super(DeviceAdapter, self).__init__(*a, **k)
        item = self._unwrapped_item()
        if hasattr(item, b'is_active'):
            self.__on_is_active_changed.subject = item
        elif is_drum_pad(item):
            self.__on_is_active_changed.subject = item.canonical_parent
            self.__on_mute_changed.subject = item
        if hasattr(item, b'name'):
            self.__on_name_changed.subject = item
        self._chain = find_chain_or_track(item)
        self._rack_chain = find_chain_or_track(find_rack(item))
        self.__on_chain_color_index_changed.subject = self._chain
        self.__on_rack_color_index_changed.subject = self._rack_chain

    def _unwrapped_item(self):
        return getattr(self._adaptee, b'item', self._adaptee)

    @listenable_property
    def navigation_name(self):
        item = self._unwrapped_item()
        name = getattr(item, b'name', b'')
        if hasattr(item, b'class_name') and item.class_name in DEVICE_TYPES_WITH_PRESET_NAME:
            return name
        else:
            return getattr(item, b'class_display_name', name)

    @property
    def class_name(self):
        import Live
        item = self._unwrapped_item()
        if isinstance(item, Live.DrumPad.DrumPad):
            return b'DrumPad'
        else:
            return getattr(item, b'class_name', b'')

    @property
    def nestingLevel(self):
        try:
            return self._adaptee.nesting_level
        except AttributeError:
            return 0

    @property
    def is_active(self):
        from ..device_navigation import is_active_element
        try:
            return is_active_element(self._unwrapped_item())
        except AttributeError:
            return True

    @listens(b'is_active')
    def __on_is_active_changed(self):
        self.notify_is_active()

    @listens(b'mute')
    def __on_mute_changed(self):
        self.notify_is_active()

    @listens(b'name')
    def __on_name_changed(self):
        self.notify_navigation_name()

    @property
    def icon(self):
        return getattr(self._adaptee, b'icon', b'')

    @listenable_property
    def chain_color_index(self):
        if liveobj_valid(self._chain):
            return convert_color_index(self._chain.color_index)
        return -1

    @listens(b'color_index')
    def __on_chain_color_index_changed(self):
        self.notify_chain_color_index()

    @listenable_property
    def rack_color_index(self):
        if liveobj_valid(self._rack_chain):
            return convert_color_index(self._rack_chain.color_index)
        return -1

    @listens(b'color_index')
    def __on_rack_color_index_changed(self):
        self.notify_rack_color_index()


class TrackAdapter(ModelAdapter):
    __events__ = ('activated', )

    def __init__(self, *a, **k):
        super(TrackAdapter, self).__init__(*a, **k)
        if hasattr(self._adaptee, b'mute'):
            self.__on_mute_changed.subject = self._adaptee
            self.__on_solo_changed.subject = self._adaptee
            self.__on_muted_via_solo_changed.subject = self._adaptee
        self.has_playing_clip = False
        self._update_has_playing_clip()
        if hasattr(self._adaptee, b'playing_slot_index'):
            self.__on_playing_slot_index_changed.subject = self._adaptee
        try:
            if hasattr(self._adaptee.parent_track, b'is_frozen'):
                self.__on_is_frozen_changed.subject = self._adaptee.parent_track
        except AttributeError:
            pass
        else:
            try:
                self.register_slot(self._adaptee, self.notify_colorIndex, b'color_index')
            except EventError:
                pass
            else:
                try:
                    self.register_slot(self._adaptee.parent_track, self.notify_parentColorIndex, b'color_index')
                except AttributeError:
                    pass
                else:
                    try:
                        self.register_slot(self._adaptee, self.notify_isFrozen, b'is_frozen')
                    except EventError:
                        pass

                try:
                    self.register_slot(self._adaptee, self.notify_arm, b'arm')
                except EventError:
                    pass

            try:
                self.register_slot(self._adaptee, self.notify_outputRouting, b'output_routing_type')
            except EventError:
                pass

    @property
    def isFoldable(self):
        return getattr(self._adaptee, b'is_foldable', False)

    @property
    def canShowChains(self):
        return getattr(self._adaptee, b'can_show_chains', False)

    @property
    def containsDrumRack(self):
        from ableton.v2.control_surface import find_instrument_meeting_requirement
        return find_instrument_meeting_requirement(lambda i: i.can_have_drum_pads, self._adaptee) is not None

    @property
    def nestingLevel(self):
        try:
            return self._adaptee.nesting_level
        except AttributeError:
            return 0

    @property
    def activated(self):
        try:
            return not (self._adaptee.muted_via_solo or self._adaptee.mute and not self._adaptee.solo)
        except RuntimeError:
            return True

    @listenable_property
    def isFrozen(self):
        try:
            return self._adaptee.is_frozen
        except AttributeError:
            return False

    @listenable_property
    def arm(self):
        try:
            if self._adaptee.can_be_armed:
                return self._adaptee.arm
            else:
                return False

        except AttributeError:
            return False

    @listenable_property
    def parent_track_frozen(self):
        try:
            return self._adaptee.parent_track.is_frozen
        except AttributeError:
            return False

    @listens(b'is_frozen')
    def __on_is_frozen_changed(self):
        self.notify_parent_track_frozen()

    @listens(b'mute')
    def __on_mute_changed(self):
        self.notify_activated()

    @listens(b'solo')
    def __on_solo_changed(self):
        self.notify_activated()

    @listens(b'muted_via_solo')
    def __on_muted_via_solo_changed(self):
        self.notify_activated()

    @listens(b'playing_slot_index')
    def __on_playing_slot_index_changed(self):
        self._update_has_playing_clip()
        self.notify_playingClip()

    def _update_has_playing_clip(self):
        has_playing_clip = self._adaptee.playing_slot_index >= 0 if hasattr(self._adaptee, b'playing_slot_index') else False
        if has_playing_clip != self.has_playing_clip:
            self.has_playing_clip = has_playing_clip
            self.notify_hasPlayingClip()

    def _playing_clip_slot(self):
        if hasattr(self._adaptee, b'playing_slot_index'):
            try:
                if self._adaptee.playing_slot_index >= 0:
                    return self._adaptee.clip_slots[self._adaptee.playing_slot_index]
            except RuntimeError:
                pass

        return

    def _playing_clip(self):
        playing_clip_slot = self._playing_clip_slot()
        if playing_clip_slot is not None:
            return playing_clip_slot.clip
        else:
            return

    @listenable_property
    def colorIndex(self):
        try:
            return convert_color_index(self._adaptee.color_index)
        except AttributeError:
            return self.parentColorIndex

    @listenable_property
    def parentColorIndex(self):
        try:
            return convert_color_index(self._adaptee.parent_track.color_index)
        except AttributeError:
            return -1

    @property
    def isMaster(self):
        try:
            return self._adaptee == self._adaptee.canonical_parent.master_track
        except AttributeError:
            return False

    @property
    def isAudio(self):
        try:
            return not self._adaptee.has_midi_input
        except AttributeError:
            return False

    @property
    def isReturn(self):
        try:
            return self._adaptee in list(self._adaptee.canonical_parent.return_tracks)
        except AttributeError:
            return False

    @listenable_property
    def outputRouting(self):
        routing_type = getattr(self._adaptee, b'output_routing_type', None)
        if routing_type is not None:
            return routing_type.display_name
        else:
            return b''

    @listenable_property
    def hasPlayingClip(self):
        return self.has_playing_clip

    @listenable_property
    def playingClip(self):
        return self._playing_clip()


class TrackListAdapter(VisibleAdapter):
    __events__ = ('selectedTrack', )

    def __init__(self, *a, **k):
        super(TrackListAdapter, self).__init__(*a, **k)
        self._alias_observable_property(b'selected_track', b'selectedTrack')


class BrowserItemAdapter(ModelAdapter):

    @property
    def icon(self):
        return getattr(self._adaptee, b'icon', b'')

    @property
    def color_label_index(self):
        return determine_color_label_index(self._adaptee)


class BrowserListWrapper(EventObject):
    """
    Custom object wrapper that takes care of binding a browser list and serializing it.
    This is necessary to greatly improve performance and avoid unnecessary wrapping of
    each browser item.
    """

    def __init__(self, browser_list, notifier=None, *a, **k):
        super(BrowserListWrapper, self).__init__(*a, **k)
        self._browser_list = browser_list
        self._notifier = notifier
        slot = Slot(browser_list, self.notify, b'items')
        slot.connect()
        self.register_slot(slot)

    @staticmethod
    def _serialize_browser_item(item):
        return {b'id': item.uri, 
           b'name': item.name, 
           b'is_loadable': item.is_loadable, 
           b'is_device': item.is_device, 
           b'icon': getattr(item, b'icon', b''), 
           b'color_label_index': determine_color_label_index(item)}

    def to_json(self):
        return map(self._serialize_browser_item, self._browser_list.items)

    def notify(self):
        self._notifier.structural_change()

    def disconnect(self):
        super(BrowserListWrapper, self).disconnect()
        self._browser_list = None
        return


class LiveDialogAdapter(VisibleAdapter):

    @property
    def text(self):
        text = self._adaptee.text
        if text is not None:
            return strip_formatted_string(text)
        else:
            return b''


class RoutingAdapter(VisibleAdapter):
    __events__ = ('routingTypeList', 'routingChannelList', 'routingChannelPositionList')

    def __init__(self, *a, **k):
        super(RoutingAdapter, self).__init__(*a, **k)
        self._alias_observable_property(b'routing_type_list', b'routingTypeList', lambda self_: [
         self_._adaptee.routing_type_list])
        self._alias_observable_property(b'routing_channel_list', b'routingChannelList', lambda self_: [
         self_._adaptee.routing_channel_list])
        self._alias_observable_property(b'routing_channel_position_list', b'routingChannelPositionList', lambda self_: [
         self_._adaptee.routing_channel_position_list])