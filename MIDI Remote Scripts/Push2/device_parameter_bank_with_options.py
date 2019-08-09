# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\device_parameter_bank_with_options.py
# Compiled at: 2019-04-23 16:19:13
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import listenable_property, liveobj_valid, find_if
from ableton.v2.control_surface import create_device_bank, DescribedDeviceParameterBank
from .custom_bank_definitions import OPTIONS_KEY, VIEW_DESCRIPTION_KEY
OPTIONS_PER_BANK = 7

class DescribedDeviceParameterBankWithOptions(DescribedDeviceParameterBank):
    _options = []

    @listenable_property
    def options(self):
        return self._options

    @property
    def bank_view_description(self):
        bank = self._definition.value_by_index(self.index)
        return unicode(bank.get(VIEW_DESCRIPTION_KEY, b''))

    def _current_option_slots(self):
        bank = self._definition.value_by_index(self.index)
        return bank.get(OPTIONS_KEY) or ('', ) * OPTIONS_PER_BANK

    def _content_slots(self):
        return self._current_option_slots() + super(DescribedDeviceParameterBankWithOptions, self)._content_slots()

    def _collect_options(self):
        option_slots = self._current_option_slots()
        options = getattr(self._device, b'options', [])
        return [ find_if(lambda o: o.name == str(slot_definition), options)
         for slot_definition in option_slots
               ]

    def _update_parameters(self):
        super(DescribedDeviceParameterBankWithOptions, self)._update_parameters()
        self._options = self._collect_options()
        self.notify_options()


def create_device_bank_with_options(device, banking_info):
    if liveobj_valid(device) and banking_info.device_bank_definition(device) is not None:
        bank = DescribedDeviceParameterBankWithOptions(device=device, size=8, banking_info=banking_info)
    else:
        bank = create_device_bank(device, banking_info)
    return bank