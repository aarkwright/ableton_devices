# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\components\item_lister.py
# Compiled at: 2019-05-15 03:17:58
from __future__ import absolute_import, print_function, unicode_literals
from itertools import izip
from ...base import forward_property, listenable_property, listens, EventObject
from .. import Component
from ..control import control_list, ButtonControl

class SimpleItemSlot(EventObject):

    def __init__(self, item=None, name=b'', nesting_level=-1, *a, **k):
        super(SimpleItemSlot, self).__init__(*a, **k)
        self._item = item
        self._name = name
        self._nesting_level = nesting_level
        self.__on_name_changed.subject = self._item if getattr(self._item, b'name_has_listener', None) else None
        self.__on_color_index_changed.subject = self._item if getattr(self._item, b'color_index_has_listener', None) else None
        return

    @listenable_property
    def name(self):
        return self._name

    @property
    def item(self):
        return self._item

    @property
    def nesting_level(self):
        return self._nesting_level

    @listenable_property
    def color_index(self):
        return getattr(self._item, b'color_index', -1)

    @listens(b'name')
    def __on_name_changed(self):
        self.notify_name()
        self._name = self._item.name

    @listens(b'color_index')
    def __on_color_index_changed(self):
        self.notify_color_index()


class ItemSlot(SimpleItemSlot):

    def __init__(self, item=None, nesting_level=0, **k):
        assert item != None
        super(ItemSlot, self).__init__(item=item, name=item.name, nesting_level=nesting_level, **k)
        return

    def __eq__(self, other):
        return id(self) == id(other) or self._item == other

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self._item)

    _live_ptr = forward_property(b'_item')(b'_live_ptr')


class ItemProvider(EventObject):
    """ General interface to implement for providers used in ItemListerComponent """
    __events__ = ('items', 'selected_item')

    @property
    def items(self):
        """
        Returns a list of tuples, each of which contains an item
        followed by its nesting level
        """
        return []

    @property
    def selected_item(self):
        return


class ItemListerComponentBase(Component):
    __events__ = ('items', )

    def __init__(self, item_provider=ItemProvider(), num_visible_items=8, *a, **k):
        super(ItemListerComponentBase, self).__init__(*a, **k)
        self._item_offset = 0
        self._item_provider = item_provider
        self._items = []
        self._num_visible_items = num_visible_items
        self.__on_items_changed.subject = item_provider
        self.update_items()

    def reset_offset(self):
        self._item_offset = 0

    @property
    def items(self):
        return self._items

    @property
    def item_provider(self):
        return self._item_provider

    def _get_item_offset(self):
        return self._item_offset

    def _set_item_offset(self, offset):
        self._item_offset = offset
        self.update_items()

    item_offset = property(_get_item_offset, _set_item_offset)

    def can_scroll_left(self):
        return self.item_offset > 0

    def can_scroll_right(self):
        items = self._item_provider.items[self.item_offset:]
        return len(items) > self._num_visible_items

    def scroll_left(self):
        self.item_offset -= 1

    def scroll_right(self):
        self.item_offset += 1

    def _adjust_offset(self):
        num_raw_items = len(self._item_provider.items)
        list_length = self._num_visible_items
        if list_length >= num_raw_items or self._item_offset >= num_raw_items - list_length:
            self._item_offset = max(0, num_raw_items - list_length)

    def update_items(self):
        for item in self._items:
            self.disconnect_disconnectable(item)

        self._adjust_offset()
        self._items = map(self.register_disconnectable, self._create_slots())
        self.notify_items()

    def _create_slots(self):
        items = self._item_provider.items[self.item_offset:]
        num_slots = min(self._num_visible_items, len(items))
        new_items = []
        if num_slots > 0:
            new_items = [ self._create_slot(index, *item) for index, item in enumerate(items[:num_slots]) if item[0] != None
                        ]
        return new_items

    def _create_slot(self, index, item, nesting_level):
        return ItemSlot(item=item, nesting_level=nesting_level)

    @listens(b'items')
    def __on_items_changed(self):
        self.update_items()


class ScrollComponent(Component):
    __events__ = ('scroll', )
    button = ButtonControl(color=b'ItemNavigation.ItemNotSelected', repeat=True)

    @button.pressed
    def button(self, button):
        self.notify_scroll()


class ScrollOverlayComponent(Component):

    def __init__(self, *a, **k):
        super(ScrollOverlayComponent, self).__init__(*a, **k)
        self._scroll_left_component, self._scroll_right_component = self.add_children(ScrollComponent(is_enabled=False), ScrollComponent(is_enabled=False))
        self.__on_scroll_left.subject = self._scroll_left_component
        self.__on_scroll_right.subject = self._scroll_right_component

    scroll_left_layer = forward_property(b'_scroll_left_component')(b'layer')
    scroll_right_layer = forward_property(b'_scroll_right_component')(b'layer')

    def can_scroll_left(self):
        raise NotImplementedError

    def can_scroll_right(self):
        raise NotImplementedError

    def scroll_left(self):
        raise NotImplementedError

    def scroll_right(self):
        raise NotImplementedError

    def update_scroll_buttons(self):
        if self.is_enabled():
            self._scroll_left_component.set_enabled(self.can_scroll_left())
            self._scroll_right_component.set_enabled(self.can_scroll_right())

    @listens(b'scroll')
    def __on_scroll_left(self):
        self.scroll_left()

    @listens(b'scroll')
    def __on_scroll_right(self):
        self.scroll_right()

    def update(self):
        super(ScrollOverlayComponent, self).update()
        if self.is_enabled():
            self.update_scroll_buttons()


class ItemListerComponent(ItemListerComponentBase):
    color_class_name = b'ItemNavigation'
    select_buttons = control_list(ButtonControl, unavailable_color=color_class_name + b'.NoItem')

    def __init__(self, *a, **k):
        super(ItemListerComponent, self).__init__(*a, **k)
        self._scroll_overlay = self.add_children(ScrollOverlayComponent(is_enabled=True))
        self._scroll_overlay.can_scroll_left = self.can_scroll_left
        self._scroll_overlay.can_scroll_right = self.can_scroll_right
        self._scroll_overlay.scroll_left = self.scroll_left
        self._scroll_overlay.scroll_right = self.scroll_right
        self.__on_items_changed.subject = self
        self.__on_selection_changed.subject = self._item_provider

    scroll_left_layer = forward_property(b'_scroll_overlay')(b'scroll_left_layer')
    scroll_right_layer = forward_property(b'_scroll_overlay')(b'scroll_right_layer')

    @listens(b'items')
    def __on_items_changed(self):
        self.select_buttons.control_count = len(self.items)
        self._update_button_colors()
        self._scroll_overlay.update_scroll_buttons()

    @listens(b'selected_item')
    def __on_selection_changed(self):
        self._update_button_colors()

    def _items_equal(self, item, selected_item):
        return item == selected_item

    def _update_button_colors(self):
        selected_item = self._item_provider.selected_item
        for button, item in izip(self.select_buttons, self.items):
            button.color = self._color_for_button(button.index, self._items_equal(item, selected_item))

    def _color_for_button(self, button_index, is_selected):
        if is_selected:
            return self.color_class_name + b'.ItemSelected'
        return self.color_class_name + b'.ItemNotSelected'

    @select_buttons.pressed
    def select_buttons(self, button):
        self._on_select_button_pressed(button)

    @select_buttons.pressed_delayed
    def select_buttons(self, button):
        self._on_select_button_pressed_delayed(button)

    @select_buttons.released
    def select_buttons(self, button):
        self._on_select_button_released(button)

    @select_buttons.released_immediately
    def select_buttons(self, button):
        self._on_select_button_released_immediately(button)

    def _on_select_button_pressed(self, button):
        pass

    def _on_select_button_pressed_delayed(self, button):
        pass

    def _on_select_button_released(self, button):
        pass

    def _on_select_button_released_immediately(self, button):
        pass