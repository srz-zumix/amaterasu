#!/usr/bin/env python
#
# amaterasu.py
#

from kamidana import (
    as_filter,
    as_global,
    # as_globals_generator,
    # as_test,
)

from wandbox.wrapper import Wrapper as Wandbox
import fnmatch

w = Wandbox()


def get_compiler_list():
    return w.get_compiler_list(1, 10)


@as_global
def wandbox_list():
    return get_compiler_list()


@as_global
def wandbox_languages():
    r = get_compiler_list()
    langs = map(lambda x: x['language'], r)
    return sorted(set(langs))


@as_filter
def wandbox_fnmatch_compilers(v, m):
    result = []
    for d in v:
        if fnmatch.fnmatch(d['name'], m):
            result.append(d)
    return result


@as_filter
def wandbox_language_compilers(v, lang):
    result = []
    for d in v:
        if d['language'] == lang:
            result.append(d)
    return result
