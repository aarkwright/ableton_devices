# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\internal_parameter.py
# Compiled at: 2019-04-23 16:19:13
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import clamp, listenable_property, liveobj_valid, nop, EventError, EventObject, forward_property, Proxy, Slot
from ableton.v2.control_surface import EnumWrappingParameter, InternalParameter, InternalParameterBase, RelativeInternalParameter, WrappingParameter, to_percentage_display

class ConstantParameter(InternalParameterBase):
    forward_from_original = forward_property(b'_original_parameter')

    def __init__(self, original_parameter=None, *a, **k):
        assert original_parameter is not None
        super(InternalParameterBase, self).__init__(*a, **k)
        self._original_parameter = original_parameter
        return

    add_value_listener = forward_from_original(b'add_value_listener')
    remove_value_listener = forward_from_original(b'remove_value_listener')
    value_has_listener = forward_from_original(b'value_has_listener')
    canonical_parent = forward_from_original(b'canonical_parent')
    min = forward_from_original(b'min')
    max = forward_from_original(b'max')
    name = forward_from_original(b'name')
    original_name = forward_from_original(b'original_name')
    default_value = forward_from_original(b'default_value')
    automation_state = forward_from_original(b'automation_state')
    state = forward_from_original(b'state')
    _live_ptr = forward_from_original(b'_live_ptr')

    @property
    def display_value(self):
        return str(self._original_parameter)

    def _get_value(self):
        return self._original_parameter.value

    def _set_value(self, _):
        pass

    value = property(_get_value, _set_value)
    linear_value = property(_get_value, _set_value)

    def __str__(self):
        return self.display_value


class ProxyParameter(Proxy):
    """
    Behaves like Proxy, but with inverted logic of getting arguments from the passed
    interface / proxied object. It means the proxied interface can override
    proxied object's attributes.
    """

    def __getattr__(self, name):
        if not self._skip_wrapper_lookup:
            obj = self.proxied_object
            return getattr(self.proxied_interface, name, getattr(obj, name))
        raise AttributeError(b'Does not have attribute %s' % name)

    def __unicode__(self):
        return unicode(self.proxied_object)

    def __eq__(self, other):
        if isinstance(other, ProxyParameter):
            return self.proxied_object == other.proxied_object and self.proxied_interface == other.proxied_interface
        return self.proxied_object == other

    def __ne__(self, other):
        if isinstance(other, ProxyParameter):
            return self.proxied_object != other.proxied_object or self.proxied_interface != other.proxied_interface
        return self.proxied_object != other