# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\base\event.py
# Compiled at: 2018-11-30 15:48:12
"""
Module for adding and listening to events.
"""
from __future__ import absolute_import, print_function, unicode_literals
from itertools import izip, repeat, chain
from functools import partial, wraps
from .disconnectable import Disconnectable, CompoundDisconnectable
from .live_api_utils import liveobj_valid
from .signal import Signal
from .util import instance_decorator, monkeypatch, monkeypatch_extend, NamedTuple
__all__ = ('EventObject', 'Event', 'EventError', 'listenable_property', 'listens',
           'listens_group', 'Slot', 'SlotGroup', 'MultiSlot', 'has_event', 'validate_event_interface')

class EventError(Exception):
    """
    Error that is raised when an object does not meet the required interface of an event
    (you try to register to an event, that an object does not have).
    """
    pass


class Event(NamedTuple):
    """
    Describes an event of a class. Is used by :class:`~EventObject` in case more control
    over the event configuration is needed.
    """
    name = None
    doc = b''
    signal = Signal
    override = False


def add_event(cls, event_name_or_event):
    """
    Adds an event to a Disconnectable class. event_name_or_event must either be a string
    or an Event object.

    The class will get a number of new methods:
        * add_[event_name]_listener
        * remove_[event_name]_listener
        * notify_[event_name]_listener
        * [event_name]_has_listener()
        * [event_name]_listener_count

    The disconnect method will be patched to remove all registered listeners.
    """
    if isinstance(event_name_or_event, basestring):
        event = Event(name=event_name_or_event)
    else:
        event = event_name_or_event
    assert callable(event.signal)
    signal_attr = b'_' + event.name + b'_signal'

    def get_signal(self):
        try:
            return getattr(self, signal_attr)
        except AttributeError:
            signal = event.signal(sender=self)
            setattr(self, signal_attr, signal)
            return signal

    kwargs = dict({b'doc': event.doc, 
       b'override': event.override})

    @monkeypatch(cls, (event.name + b'_has_listener'), **kwargs)
    def has_method(self, slot):
        return get_signal(self).is_connected(slot)

    @monkeypatch(cls, (b'add_' + event.name + b'_listener'), **kwargs)
    def add_method(self, slot, identify_sender=False, *a, **k):
        sender = self if identify_sender else None
        return get_signal(self).connect(slot, sender=sender, *a, **k)

    @monkeypatch(cls, (b'remove_' + event.name + b'_listener'), **kwargs)
    def remove_method(self, slot):
        return get_signal(self).disconnect(slot)

    @monkeypatch(cls, (b'notify_' + event.name), **kwargs)
    def notify_method(self, *a, **k):
        return get_signal(self)(*a, **k)

    @monkeypatch(cls, (event.name + b'_listener_count'), **kwargs)
    def listener_count_method(self):
        return get_signal(self).count

    @monkeypatch_extend(cls)
    def disconnect(self):
        get_signal(self).disconnect_all()


def validate_event_interface(obj, event_name):
    """
    Validates that obj has all required methods available for the given
    event name. Raises EventError if the interface is not available.
    """
    if not callable(getattr(obj, b'add_' + event_name + b'_listener', None)):
        raise EventError(b'Object %s missing "add" method for event: %s' % (obj, event_name))
    if not callable(getattr(obj, b'remove_' + event_name + b'_listener', None)):
        raise EventError(b'Object %s missing "remove" method for event: %s' % (obj, event_name))
    if not callable(getattr(obj, event_name + b'_has_listener', None)):
        raise EventError(b'Object %s missing "has" method for event: %s' % (obj, event_name))
    return


def has_event(obj, event_name):
    """
    Returns true if obj has all required methods available for the given event name.
    """
    return callable(getattr(obj, b'add_' + event_name + b'_listener', None)) and callable(getattr(obj, b'remove_' + event_name + b'_listener', None)) and callable(getattr(obj, event_name + b'_has_listener', None))


class listenable_property_base(object):
    """
    Base class for properties of a class, for which a corresponding event (with the same
    name as the property) will be created.
    EventObjectMeta will generate an event for every class attribute, whose base class
    is listenable_property_base.
    """

    def set_property_name(self, name):
        """
        Is called with the name of the class attribute by EventObjectMeta.
        """
        pass


class EventObjectMeta(type):
    """
    Meta class for EventObject, that generates an events interfaces. An event is
    defined by the __events__ attribute or an attribute that inherits from
    listenable_property_base.
    """

    @staticmethod
    def collect_listenable_properties(dct):
        return filter(lambda item: isinstance(item[1], listenable_property_base), dct.iteritems())

    def __new__(cls, name, bases, dct):
        listenable_properties = EventObjectMeta.collect_listenable_properties(dct)
        for property_name, obj in listenable_properties:
            obj.set_property_name(property_name)

        events = dct.get(b'__events__', [])
        property_events = [ event_name for event_name, obj in listenable_properties ]
        has_events = events or property_events
        if has_events and b'disconnect' not in dct:
            dct[b'disconnect'] = lambda self: super(cls, self).disconnect()
        cls = super(EventObjectMeta, cls).__new__(cls, name, bases, dct)
        assert not has_events or hasattr(cls, b'disconnect')
        for lst in chain(events, property_events):
            add_event(cls, lst)

        return cls


class EventObject(CompoundDisconnectable):
    """
    Base class to enable defining and listening to events.

    Events can be defined in two ways:

        * Add a class property __events__, that needs to be a tuple of event names or
          Event objects.
        * Use listenable_property to define properties of a class, that have a
          corresponding event.

    Events can be listened to using the listens decorator, register_slot, or calling
    the add_[event_name]_listener method directly. The listens decorator and register_slot
    guarantee that listeners are disconnected correctly, if the EventObject itself is
    disconnected and should be the preferred way of connecting to events.
    """
    __metaclass__ = EventObjectMeta

    def register_slot(self, *a, **k):
        """
        Creates a new :class:`~Slot` and registers it, so it gets disconnected.
        All arguments are forwarded to the constructor of :class:`~Slot`.
        In case the argument is already a `Slot`, the object gets simply registered.
        """
        slot = a[0] if a and isinstance(a[0], Slot) else Slot(*a, **k)
        self.register_disconnectable(slot)
        return slot


class Slot(Disconnectable):
    """
    This class maintains the relationship between a subject and a
    listener. As soon as both are non-null, it connects the listener to the given 'event'
    of the subject and releases the connection when any of them change.

    The finalizer of the object also cleans up both parameters and so
    does the __exit__ override, being able to use it as a context
    manager with the 'with' clause.

    Note that the connection can already be made manually before the
    subject and listener are fed to the slot.
    """
    _extra_kws = {}
    _extra_args = []

    def __init__(self, subject=None, listener=None, event_name=None, extra_kws=None, extra_args=None, *a, **k):
        super(Slot, self).__init__(*a, **k)
        assert event_name
        self._event_name = event_name
        if extra_kws is not None:
            self._extra_kws = extra_kws
        if extra_args is not None:
            self._extra_args = extra_args
        self._subject = None
        self._listener = None
        self.subject = subject
        self.listener = listener
        return

    def subject_valid(self, subject):
        """
        Returns True if a subject is valid and can be connected.
        """
        return liveobj_valid(subject)

    def disconnect(self):
        """
        Disconnects the slot clearing its members.
        """
        self.subject = None
        self.listener = None
        super(Slot, self).disconnect()
        return

    def connect(self):
        """
        Connects the listener with the current subject.
        """
        if not self.is_connected and self.subject_valid(self._subject) and self._listener is not None:
            add_method = getattr(self._subject, b'add_' + self._event_name + b'_listener')
            all_args = tuple(self._extra_args) + (self._listener,)
            try:
                add_method(*all_args, **self._extra_kws)
            except RuntimeError:
                pass

        return

    def soft_disconnect(self):
        """
        Disconnects the listener from the subject keeping their
        values.
        """
        if self.is_connected and self.subject_valid(self._subject) and self._listener is not None:
            all_args = tuple(self._extra_args) + (self._listener,)
            remove_method = getattr(self._subject, b'remove_' + self._event_name + b'_listener')
            try:
                remove_method(*all_args)
            except RuntimeError:
                pass

        return

    @property
    def is_connected(self):
        """
        Returns True if the associated listener is connected to the current subject.
        """
        all_args = tuple(self._extra_args) + (self._listener,)
        connected = False
        try:
            connected = bool(self.subject_valid(self._subject) and self._listener is not None and getattr(self._subject, self._event_name + b'_has_listener')(*all_args))
        except RuntimeError:
            pass

        return connected

    @property
    def subject(self):
        """
        The object with the given event, that is connected with the listener.
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        if subject != self._subject:
            if self.subject_valid(subject):
                validate_event_interface(subject, self._event_name)
            self.soft_disconnect()
            self._subject = subject
            self.connect()

    @property
    def listener(self):
        """
        The listener, that is called when the event is notified.
        """
        return self._listener

    @listener.setter
    def listener(self, listener):
        if listener != self._listener:
            self.soft_disconnect()
            self._listener = listener
            self.connect()

    def __call__(self, *a, **k):
        if self._listener is not None:
            return self._listener(*a, **k)
        else:
            return


class SlotGroup(EventObject):
    """
    A slot that connects a given listener to many subjects.
    """
    listener = None
    _extra_kws = None
    _extra_args = None

    def __init__(self, listener=None, event_name=None, extra_kws=None, extra_args=None, *a, **k):
        super(SlotGroup, self).__init__(*a, **k)
        self.listener = listener
        self._event_name = event_name
        if listener is not None:
            self.listener = listener
        if extra_kws is not None:
            self._extra_kws = extra_kws
        if extra_args is not None:
            self._extra_args = extra_args
        return

    def replace_subjects(self, subjects, identifiers=repeat(None)):
        """
        Replaces all currently connected subjects of this slot with the new subjects.
        All listeners get the notifying subject passed as an argument.
        The `identifiers` argument can be used to notify with an identifier instead of
        the subject itself.
        """
        self.disconnect()
        for subject, identifier in izip(subjects, identifiers):
            self.add_subject(subject, identifier=identifier)

    def add_subject(self, subject, identifier=None):
        """
        Adds a subject to this slot. Listeners get the notifying subject passed as an
        argument, or with identifier if it's not None.
        """
        if identifier is None:
            identifier = subject
        listener = self._listener_for_subject(identifier)
        self.register_slot(subject, listener, self._event_name, self._extra_kws, self._extra_args)
        return

    def remove_subject(self, subject):
        """
        Removes a previously added subject from this slot.
        """
        slot = self.find_disconnectable(lambda x: x.subject == subject)
        self.disconnect_disconnectable(slot)

    def has_subject(self, subject):
        """
        Returns true if the given subject has been added to the slot.
        """
        return liveobj_valid(self.find_disconnectable(lambda x: x.subject == subject))

    def _listener_for_subject(self, identifier):
        return lambda *a, **k: self.listener and self.listener(*(a + (identifier,)), **k)

    def __call__(self, *a, **k):
        return self.listener(*a, **k)


class MultiSlot(EventObject, Slot):
    """
    A slot that takes a string describing the path to the event to listen to.
    It will make sure that any changes to the elements of this path notify the given
    listener and will follow the changing subjects.
    """

    def __init__(self, subject=None, listener=None, event_name_list=None, extra_kws=None, extra_args=None, *a, **k):
        self._original_listener = listener
        self._slot_subject = None
        self._nested_slot = None
        super(MultiSlot, self).__init__(event_name=event_name_list[0], listener=self._event_fired, subject=subject, extra_kws=extra_kws, extra_args=extra_args)
        if len(event_name_list) > 1:
            self._nested_slot = self.register_disconnectable(MultiSlot(event_name_list=event_name_list[1:], listener=listener, extra_kws=extra_kws, extra_args=extra_args))
            self._update_nested_subject()
        return

    @property
    def subject(self):
        """
        The object with the given event, that is connected with the listener.
        """
        return super(MultiSlot, self).subject

    @subject.setter
    def subject(self, subject):
        try:
            super(MultiSlot, MultiSlot).subject.fset(self, subject)
        except EventError:
            if self._nested_slot is None:
                raise
        finally:
            self._slot_subject = subject
            self._update_nested_subject()

        return

    def _event_fired(self, *a, **k):
        self._update_nested_subject()
        self._original_listener(*a, **k)

    def _update_nested_subject(self):
        if self._nested_slot is not None:
            self._nested_slot.subject = getattr(self._slot_subject, self._event_name) if self.subject_valid(self._slot_subject) else None
        return

    def __call__(self, *a, **k):
        return self._original_listener(*a, **k)


def listens(event_path, *a, **k):
    """
    Decorator for making a method easily connectable with an event.

    The method will be made into either a :class:`~Slot` or :class:`~MultiSlot`,
    depending on the event_path being a simple event or an actual path.

    It can than be connected using :attr:`Slot.subject`.
    """

    @instance_decorator
    def decorator(self, method):
        assert isinstance(self, EventObject)
        event_name_list = event_path.split(b'.')
        if len(event_name_list) > 1:
            slot = wraps(method)(MultiSlot(event_name_list=event_name_list, extra_kws=k, extra_args=a, listener=partial(method, self)))
        else:
            slot = wraps(method)(Slot(event_name=event_path, extra_kws=k, extra_args=a, listener=partial(method, self)))
        self.register_slot(slot)
        return slot

    return decorator


def listens_group(event_name, *a, **k):
    """
    Decorator for making a method easily connectable with a group of subjects, that
    have an event `event_name`.

    The decorated method is wrapped in an instance of :class:`~SlotGroup`.

    It can than be connected using :meth:`SlotGroup.replace_subject` or
    :meth:`SlotGroup.add_subject`.
    """

    @instance_decorator
    def decorator(self, method):
        assert isinstance(self, EventObject)
        slot = wraps(method)(SlotGroup(event_name=event_name, extra_kws=k, extra_args=a, listener=partial(method, self)))
        self.register_disconnectable(slot)
        return slot

    return decorator


class listenable_property(listenable_property_base, property):
    """
    Can be used like Pythons built-in property and will in addition generate a
    corresponding event for it. The event has the same name as the property. The class
    hosting the property must inherit from :class:`~EventObject`.
    """

    @classmethod
    def managed(cls, default_value):
        """
        Adds a property to the class and manages the properties value internally. No
        explicit setter and getter is required.
        A corresponding event will be created, which will notify whenever a new value
        is assigned to the property. Assigning the same value again has no effect.
        """
        return _managed_listenable_property(default_value=default_value)


class _managed_listenable_property(listenable_property_base):

    def __init__(self, default_value=None, *a, **k):
        super(_managed_listenable_property, self).__init__(*a, **k)
        self._default_value = default_value
        self._property_name = None
        self._member_name = None
        return

    def set_property_name(self, property_name):
        self._property_name = property_name
        self._member_name = b'__listenable_property_%s' % property_name

    def _get_value(self, obj):
        assert self._member_name is not None, b'Cannot get member for managed listenable property. Listenable property might be used without inheriting from EventObject.'
        return getattr(obj, self._member_name, self._default_value)

    def __get__(self, obj, owner):
        return self._get_value(obj)

    def __set__(self, obj, value):
        if value != self._get_value(obj):
            setattr(obj, self._member_name, value)
            getattr(obj, b'notify_%s' % self._property_name)(value)


class SerializableListenablePropertiesMeta(EventObjectMeta):

    def __new__(cls, name, bases, dct):
        listenable_properties = EventObjectMeta.collect_listenable_properties(dct)

        def getstate(self):
            data = super(generated_class, self).__getstate__()
            data.update(dict((property_name, getattr(self, property_name)) for property_name, _ in listenable_properties))
            return data

        def setstate(self, data):
            for k, v in data.iteritems():
                setattr(self, k, v)

        dct[b'__getstate__'] = getstate
        dct[b'__setstate__'] = setstate
        generated_class = super(SerializableListenablePropertiesMeta, cls).__new__(cls, name, bases, dct)
        return generated_class


class SerializableListenablePropertiesBase(Disconnectable):

    def __getstate__(self):
        return dict()

    def __setstate__(self, data):
        pass


class SerializableListenableProperties(SerializableListenablePropertiesBase):
    """
    Installs a meta class, that generates __getstate__ and __setstate__ for
    serializing all listenable properties.
    """
    __metaclass__ = SerializableListenablePropertiesMeta


class ObservablePropertyAlias(EventObject):

    def __init__(self, alias_host, property_host=None, property_name=b'', alias_name=None, getter=None, *a, **k):
        super(ObservablePropertyAlias, self).__init__(*a, **k)
        self._alias_host = alias_host
        self._alias_name = alias_name or property_name
        self._property_host = property_host
        self._property_name = property_name
        self._property_slot = None
        self._setup_alias(getter)
        return

    def _get_property_host(self):
        return self._property_host

    def _set_property_host(self, host):
        self._property_host = host
        self._property_slot.subject = host

    property_host = property(_get_property_host, _set_property_host)

    def _setup_alias(self, getter):
        aliased_prop = property(getter or self._get_property)
        setattr(self._alias_host.__class__, self._alias_name, aliased_prop)
        notifier = getattr(self._alias_host, b'notify_' + self._alias_name)
        self._property_slot = self.register_slot(Slot(self.property_host, notifier, self._property_name))

    def _get_property(self, _):
        return getattr(self.property_host, self._property_name, None)