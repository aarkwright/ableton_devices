# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\Profile.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
from functools import wraps, partial
ENABLE_PROFILING = False
if ENABLE_PROFILING:
    import cProfile
    PROFILER = cProfile.Profile()

def profile(fn):
    """
    Decorator to mark a function to be profiled. Only mark top level functions
    """
    if ENABLE_PROFILING:

        @wraps(fn)
        def wrapper(self, *a, **k):
            if PROFILER:
                return PROFILER.runcall(partial(fn, self, *a, **k))
            else:
                print(b'Can not profile (%s), it is probably reloaded' % fn.__name__)
                return fn(*a, **k)

        return wrapper
    else:
        return fn


def dump(name=b'default'):
    assert ENABLE_PROFILING
    import pstats
    fname = name + b'.profile'
    PROFILER.dump_stats(fname)

    def save_human_data(sort):
        s = pstats.Stats(fname, stream=open(b'%s.%s.txt' % (fname, sort), b'w'))
        s.sort_stats(sort)
        s.print_stats()

    save_human_data(b'time')
    save_human_data(b'cumulative')