# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\MessageScheduler.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
from collections import namedtuple

class MessageScheduler(object):
    """
    Schedules outgoing messages (sysex and other MIDI) sent to a
    MIDI port shared between multiple owners and synchronizes them
    with incoming messages (sysex only).
    For request/response message pairs this ensures that responses are
    sent back to where the requests came from (the owner).
    Also, it allows for a temporary routing of unexpected messages
    to an owner grabbing the device.
    """

    def __init__(self, send_message_callback, timer):
        self._send_message_callback = send_message_callback
        self._timer = timer
        self._state = b'idle'
        self._owner = None
        self._request_type = namedtuple(b'Request', b'action owner message timeout')
        self._request_queue = []
        return

    @property
    def is_idling(self):
        return self._state == b'idle' and self._owner == None and len(self._request_queue) == 0

    def __repr__(self):
        return (b'MessageScheduler(state={}, owner={})').format(self._state, self._owner)

    def _process_request(self, request):
        assert self._owner == None or self._owner == request.owner
        if request.action == b'send':
            if self._state == b'idle' or self._state == b'grabbed' and self._owner == request.owner:
                self._send_message_callback(request.message)
                return True
            else:
                return False

        elif request.action == b'grab':
            if self._state == b'idle':
                self._state = b'grabbed'
                self._owner = request.owner
                self._owner.send_reply(b'grab', b'1')
                return True
            else:
                if self._state == b'grabbed':
                    request.owner.report_error(b'unexpected grab')
                    return True
                return False

        elif request.action == b'release':
            if self._state == b'idle':
                request.owner.report_error(b'unexpected release')
                return True
            else:
                if self._state == b'grabbed':
                    assert self._owner == request.owner
                    self._owner.send_reply(b'release', b'1')
                    self._state = b'idle'
                    self._owner = None
                    return True
                return False

        elif request.action == b'send_receive':
            if self._state == b'idle':
                self._send_message_callback(request.message)
                self._state = b'wait'
                self._owner = request.owner
                self._timer.start(request.timeout, self.handle_timeout)
                return True
            else:
                if self._state == b'grabbed' and self._owner == request.owner:
                    self._send_message_callback(request.message)
                    self._state = b'grabbed_wait'
                    self._timer.start(request.timeout, self.handle_timeout)
                    return True
                return False

        return

    def _queue(self, request):
        if request.owner is not None:
            self._request_queue.append(request)
        return

    def _process_single_request(self):
        for i, request in enumerate(self._request_queue):
            if self._owner in (None, request.owner):
                if self._process_request(request):
                    del self._request_queue[i]
                    return True
                else:
                    return False

        return False

    def _process_queue(self):
        while self._process_single_request():
            pass

    def send(self, owner, message):
        request = self._request_type(b'send', owner, message, 0)
        self._queue(request)
        self._process_queue()

    def grab(self, owner):
        request = self._request_type(b'grab', owner, None, 0)
        self._queue(request)
        self._process_queue()
        return

    def release(self, owner):
        request = self._request_type(b'release', owner, None, 0)
        self._queue(request)
        self._process_queue()
        return

    def send_receive(self, owner, message, timeout):
        request = self._request_type(b'send_receive', owner, message, timeout)
        self._queue(request)
        self._process_queue()

    def handle_message(self, message):
        if self._state == b'idle':
            pass
        elif self._state == b'wait':
            if self._owner.is_expected_reply(message):
                self._owner.send_reply(b'send_receive', message)
                self._state = b'idle'
                self._owner = None
                self._timer.cancel()
                self._process_queue()
        elif self._state == b'grabbed':
            self._owner.send_reply(b'received', message)
        elif self._state == b'grabbed_wait':
            if self._owner.is_expected_reply(message):
                self._owner.send_reply(b'send_receive', message)
                self._state = b'grabbed'
                self._timer.cancel()
                self._process_queue()
            else:
                self._owner.send_reply(b'received', message)
        return

    def handle_timeout(self):
        if self._state == b'wait':
            self._owner.send_reply(b'send_receive', b'timeout')
            self._state = b'idle'
            self._owner = None
            self._process_queue()
        elif self._state == b'grabbed_wait':
            self._owner.send_reply(b'send_receive', b'timeout')
            self._state = b'grabbed'
            self._process_queue()
        return

    def disconnect(self, owner):
        if self._state != b'idle':
            self._request_queue = [ r for r in self._request_queue if r.owner != owner ]
            if self._owner == owner:
                self._owner = None
                self._state = b'idle'
                self._timer.cancel()
            self._process_queue()
        return