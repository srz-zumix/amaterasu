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

import urllib.parse
import re


@as_filter
def markdown_link_pair(v):
    cache = {}
    result = []
    for name in v:
        link = name
        link = link.replace(' ', '-')
        link = re.sub('[!@#$+]', '', link)
        if link in cache:
            cache[link] += 1
            link = '{0}-{1}'.format(link, cache[link])
        else:
            cache[link] = 0
        result.append({"name": name, "link": link})
    return result


@as_filter
def urlencode(v):
    return urllib.parse.urlencode(v)


@as_filter
def url_quote(v, safe=''):
    return urllib.parse.quote(v, safe=safe)


@as_filter
def url_quote_plus(v, safe=''):
    return urllib.parse.quote_plus(v, safe=safe)


@as_filter
def replace_url_quote(v):
    return v.replace('%23', '%2523').replace('%20', '%2520')


@as_global
def fread(path):
    with open(path) as f:
        return f.read()
