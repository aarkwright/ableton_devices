# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\browser_util.py
# Compiled at: 2018-11-30 15:48:12
from __future__ import absolute_import, print_function, unicode_literals
import Live
FilterType = Live.Browser.FilterType
DeviceType = Live.Device.DeviceType

def filter_type_for_hotswap_target(target, default=FilterType.disabled):
    """
    Returns the appropriate browser filter type for a given hotswap target.
    """
    if isinstance(target, Live.Device.Device):
        if target.type == DeviceType.instrument:
            return FilterType.instrument_hotswap
        if target.type == DeviceType.audio_effect:
            return FilterType.audio_effect_hotswap
        if target.type == DeviceType.midi_effect:
            return FilterType.midi_effect_hotswap
        FilterType.disabled
    elif isinstance(target, Live.DrumPad.DrumPad):
        return FilterType.drum_pad_hotswap
    else:
        if isinstance(target, Live.Chain.Chain):
            if target:
                return filter_type_for_hotswap_target(target.canonical_parent)
            return FilterType.disabled

    return default


def get_selection_for_new_device(selection, insert_left=False):
    """
    Returns a device, depending on the type of object that is selected at this moment.
    For drum pads, it returns the last device in the pads chain.
    If the selected object is no device, it returns the selected deviec.
    """
    selected = selection.selected_object
    if isinstance(selected, Live.DrumPad.DrumPad) and selected.chains and selected.chains[0].devices:
        index = 0 if insert_left else -1
        selected = selected.chains[0].devices[index]
    elif not isinstance(selected, Live.Device.Device):
        selected = selection.selected_device
    return selected