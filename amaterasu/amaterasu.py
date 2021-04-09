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

from wandbox.wrapper import Wrapper
from wandbox.wandbox import Wandbox
import fnmatch

w = Wrapper()


def get_compiler_list():
    return w.get_compiler_list(1, 10)


@as_global
def wandbox_list():
    return get_compiler_list()


@as_global
def wandbox_languages():
    r = get_compiler_list()
    langs = map(lambda x: x['language'], r)
    return sorted(set(langs), key=str.lower)


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

@as_global
def wandbox_run(compiler, code, options=None, compiler_option=None, runtime_option=None):
    wandbox = Wandbox()
    wandbox.compiler(compiler)
    if options:
        wandbox.options(options)
    if compiler_option:
        wandbox.add_compiler_options(compiler_option)
    if runtime_option:
        wandbox.add_runtime_options(runtime_option)
    wandbox.code(code)
    return wandbox.run()
