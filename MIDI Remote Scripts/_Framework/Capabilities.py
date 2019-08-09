# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\Capabilities.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
GENERIC_SCRIPT_KEY = b'generic_script'
PORTS_KEY = b'ports'
CONTROLLER_ID_KEY = b'controller_id'
TYPE_KEY = b'surface_type'
FIRMWARE_KEY = b'firmware_version'
AUTO_LOAD_KEY = b'auto_load'
VENDORID = b'vendor_id'
PRODUCTIDS = b'product_ids'
MODEL_NAMES = b'model_names'
DIRECTIONKEY = b'direction'
PORTNAMEKEY = b'name'
MACNAMEKEY = b'mac_name'
PROPSKEY = b'props'
HIDDEN = b'hidden'
SYNC = b'sync'
SCRIPT = b'script'
NOTES_CC = b'notes_cc'
REMOTE = b'remote'
PLAIN_OLD_MIDI = b'plain_old_midi'

def __create_port_dict(direction, port_name, mac_name, props):
    assert isinstance(direction, basestring)
    assert isinstance(port_name, basestring)
    assert props == None or type(props) is list
    if props:
        for prop in props:
            if not isinstance(prop, basestring):
                raise AssertionError

    assert mac_name == None or isinstance(mac_name, basestring)
    capabilities = {DIRECTIONKEY: direction, PORTNAMEKEY: port_name, PROPSKEY: props}
    if mac_name:
        capabilities[MACNAMEKEY] = mac_name
    return capabilities


def inport(port_name=b'', props=[], mac_name=None):
    """ Generate a ..."""
    return __create_port_dict(b'in', port_name, mac_name, props)


def outport(port_name=b'', props=[], mac_name=None):
    """ Generate a ..."""
    return __create_port_dict(b'out', port_name, mac_name, props)


def controller_id(vendor_id, product_ids, model_name):
    """ Generate a hardwareId dict"""
    assert type(vendor_id) is int
    assert type(product_ids) is list
    for product_id in product_ids:
        if not type(product_id) is int:
            raise AssertionError

    assert isinstance(model_name, (basestring, list))
    if isinstance(model_name, basestring):
        model_names = [
         model_name]
    else:
        model_names = model_name
    return {VENDORID: vendor_id, PRODUCTIDS: product_ids, MODEL_NAMES: model_names}