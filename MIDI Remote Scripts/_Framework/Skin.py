# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\Skin.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
from itertools import chain

class SkinColorMissingError(Exception):
    pass


class Skin(object):

    def __init__(self, colors=None, *a, **k):
        super(Skin, self).__init__(*a, **k)
        self._colors = {}
        if colors is not None:
            self._fill_colors(colors)
        return

    def _fill_colors(self, colors, pathname=b''):
        try:
            self._fill_colors(super(colors))
        except TypeError:
            map(self._fill_colors, colors.__bases__)

        for k, v in colors.__dict__.iteritems():
            if k[:1] != b'_':
                if callable(v):
                    self._fill_colors(v, pathname + k + b'.')
                else:
                    self._colors[pathname + k] = v

    def __getitem__(self, key):
        try:
            return self._colors[key]
        except KeyError:
            raise SkinColorMissingError, b'Skin color missing: %s' % str(key)

    def iteritems(self):
        return self._colors.iteritems()


def merge_skins(*skins):
    skin = Skin()
    skin._colors = dict(chain(*map(lambda s: s._colors.items(), skins)))
    return skin