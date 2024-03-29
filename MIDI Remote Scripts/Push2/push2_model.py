# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\push2_model.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
from pprint import pformat
import logging, json
from .model import RootModel
from .model.generation import generate_mrs_model, ModelUpdateNotifier
logger = logging.getLogger(__name__)

class Sender(object):

    def __init__(self, message_sink=None, process_connected=None, *a, **k):
        super(Sender, self).__init__(*a, **k)
        assert message_sink is not None
        self._message_sink = message_sink
        if process_connected is None:
            process_connected = lambda : True
        self._process_connected = process_connected
        self._attribute_paths = []
        self._structural_change = False
        self.notifier = ModelUpdateNotifier(delegate=self)
        return

    def structural_change(self, path):
        self._attribute_paths.append((path, None))
        self._structural_change = True
        return

    def attribute_changed(self, path, value):
        self._attribute_paths.append((path, value))

    def send(self, root_model, send_all=False):

        def send_data(data):
            if data[b'command'] == b'full-model-update':
                data[b'fingerprint'] = root_model.__fingerprint__
            raw = json.dumps(data)
            self._message_sink(raw)
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(b'Model sent: %s', pformat(data))

        if send_all:
            send_data(dict(command=b'full-model-update', payload=root_model.to_json()))
        elif self._structural_change:
            root_keys = set(path[0][0] for path in self._attribute_paths)
            data = dict(command=b'full-model-update', payload=root_model.to_json(root_keys))
            send_data(data)
        elif self._attribute_paths:
            data = dict(command=b'path-model-update', payload=self._attribute_paths)
            send_data(data)
        self._attribute_paths = []
        self._structural_change = False


class Root(generate_mrs_model(RootModel)):

    def __init__(self, sender=None, *a, **k):
        self._sender = sender
        if sender is not None:
            k[b'notifier'] = sender.notifier
        super(Root, self).__init__(*a, **k)
        return

    def commit_changes(self, send_all=False):
        if self._sender is not None:
            self._sender.send(self, send_all)
        return

    def to_json(self, root_keys=None):
        if root_keys is None:
            return super(Root, self).to_json()
        else:
            res = {}
            for key in root_keys:
                res[key] = self.data[key].to_json()

            return res
            return