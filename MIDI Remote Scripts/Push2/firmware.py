# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\firmware.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
import fnmatch, logging, os, re
from collections import namedtuple
from itertools import imap
from ableton.v2.base import find_if, listenable_property, task
from ableton.v2.control_surface import Component
import Live
logger = logging.getLogger(__name__)
WELCOME_STATE_TIME = 2.0
FIRMWARE_PATH = os.path.join(os.path.dirname(__file__), b'firmware')

class FirmwareVersion(object):

    def __init__(self, major=0, minor=0, build=0, release_type=b'unknown', *a, **k):
        super(FirmwareVersion, self).__init__(*a, **k)
        self.major = major
        self.minor = minor
        self.build = build
        self.release_type = release_type

    def __cmp__(self, other):
        if other is None:
            return -1
        else:
            if self.major == other.major and self.minor == other.minor and self.build == other.build:
                return 0
            if self.major > other.major or self.major == other.major and self.minor > other.minor or self.major == other.major and self.minor == other.minor and self.build > other.build:
                return 1
            return -1

    def __repr__(self):
        return b'<FirmwareVersion %i.%i.%i %s>' % (
         self.major,
         self.minor,
         self.build,
         self.release_type)


_firmware_version_re = b'([0-9]+)\\.([0-9]+)\\.([0-9]+)'

def extract_firmware_version(filename, prefix, release_type=b'unknown'):
    match = re.match(b'%s%s.*' % (prefix, _firmware_version_re), filename)
    if match:
        return FirmwareVersion(int(match.group(1)), int(match.group(2)), int(match.group(3)), release_type)
    else:
        return


FirmwareInfo = namedtuple(b'FirmwareInfo', [b'version', b'filename'])

class FirmwareCollector(object):
    STABLE_PREFIX = b'app_push2_stable_'
    DEV_PREFIX = b'app_push2_dev_'

    def __init__(self, firmware_path=FIRMWARE_PATH, *a, **k):
        super(FirmwareCollector, self).__init__(*a, **k)
        self.firmware_path = firmware_path
        self.stable_firmwares = self._collect_firmware_files(self.STABLE_PREFIX, b'stable')
        self.dev_firmwares = self._collect_firmware_files(self.DEV_PREFIX, b'dev')
        logger.debug(b'Available stable firmware files %r', self.stable_firmwares)
        logger.debug(b'Available dev firmware files %r', self.dev_firmwares)

    @property
    def latest_stable_firmware(self):
        if self.stable_firmwares:
            return max(self.stable_firmwares, key=lambda f: f.version)
        else:
            return

    @property
    def latest_dev_firmware(self):
        if self.dev_firmwares:
            return max(self.dev_firmwares, key=lambda f: f.version)
        else:
            return

    def get_release_type(self, version):
        if version in imap(lambda f: f.version, self.stable_firmwares):
            return b'stable'
        if version in imap(lambda f: f.version, self.dev_firmwares):
            return b'dev'
        return b'unknown'

    def _collect_firmware_files(self, prefix, release_type):
        return filter(lambda x: x.version is not None, [ FirmwareInfo(extract_firmware_version(f, prefix, release_type), f) for f in os.listdir(FIRMWARE_PATH) if fnmatch.fnmatch(f, b'*.upgrade')
                                                       ])


class FirmwareUpdateComponent(Component):
    state = listenable_property.managed(b'welcome')

    def __init__(self, *a, **k):
        super(FirmwareUpdateComponent, self).__init__(is_enabled=False, *a, **k)
        self._firmware = None
        return

    def start(self, firmware):
        assert firmware is not None
        assert self.state == b'welcome'
        logger.info(b'Start firmware update using %r', firmware.filename)
        self._firmware = firmware
        self.notify_firmware_file()
        self.set_enabled(True)

        def set_state():
            self.state = b'start'

        self._tasks.add(task.sequence(task.wait(WELCOME_STATE_TIME), task.run(set_state)))
        return

    def process_firmware_response(self, data):
        assert self.state == b'start', b"'%s' != 'start'" % self.state
        entry = find_if(lambda entry: entry[b'type'] == b'firmware', data)
        if entry:
            self.state = b'success' if entry[b'success'] else b'failure'

    @listenable_property
    def firmware_file(self):
        if self._firmware is not None:
            return os.path.join(FIRMWARE_PATH, self._firmware.filename)
        else:
            return b''

    @property
    def data_file(self):
        return os.path.join(FIRMWARE_PATH, b'FlashData.bin')


class FirmwareSwitcher(object):
    """
    Class for switching between the stable and the dev firmware
    """

    def __init__(self, firmware_collector=None, firmware_update=None, installed_firmware_version=None, *a, **k):
        assert firmware_collector is not None
        assert firmware_update is not None
        assert installed_firmware_version is not None
        super(FirmwareSwitcher, self).__init__(*a, **k)
        self._installed_version = installed_firmware_version
        self._update = firmware_update
        self._collector = firmware_collector
        return

    @property
    def firmware_to_switch_to(self):
        if self.can_switch_firmware:
            if self._installed_version.release_type == b'dev':
                return self._collector.latest_stable_firmware
            else:
                return self._collector.latest_dev_firmware

        return

    @property
    def version_to_switch_to(self):
        firmware = self.firmware_to_switch_to
        if firmware is not None:
            return firmware.version
        else:
            return

    @property
    def can_switch_firmware(self):
        application = Live.Application.get_application()
        return application.has_option(b'_Push2DevFirmware') and self._collector.latest_stable_firmware is not None and self._collector.latest_dev_firmware is not None

    def switch_firmware(self):
        if not self.can_switch_firmware:
            raise RuntimeError(b'Cannot switch firmware')
        self._update.start(self.firmware_to_switch_to)