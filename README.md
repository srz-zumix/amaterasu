# amaterasu

[![PyPI version](https://badge.fury.io/py/amaterasu-j2.svg)](https://badge.fury.io/py/amaterasu-j2)
[![Python Versions](https://img.shields.io/pypi/pyversions/amaterasu_j2.svg)](https://pypi.org/project/amaterasu-j2/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2ff3eb34b617416c97f590b45b5e82fe)](https://app.codacy.com/manual/srz-zumix/amaterasu?utm_source=github.com&utm_medium=referral&utm_content=srz-zumix/amaterasu&utm_campaign=Badge_Grade_Settings)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/srz-zumix/amaterasu.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/srz-zumix/amaterasu/context:python)
[![GitHub Actions](https://github.com/srz-zumix/amaterasu/actions/workflows/main.yml/badge.svg)](https://github.com/srz-zumix/amaterasu/actions/workflows/main.yml)

It is wandbox additional of [kamidana][] of jinja2 cli

amaterasu cli is kamidana wrapper, Adds additional option automatically.

## Usage

### List Example

```sh
$ pip install amaterasu-j2
$ amaterasu sample/wandbox.j2
* cpython-3*
  * cpython-3.10.2
  * cpython-3.9.3
  * cpython-3.8.9
  * cpython-3.7.10
  * cpython-3.6.12
```

sample/wandbox.j2

```j2
* cpython-3*
{%- set compilers = wandbox_list() | wandbox_fnmatch_compilers("cpython-3*") %}
{%- for compiler in compilers %}
  * {{ compiler.name }}
{%- endfor %}
```

### Compile Example

````sh
$ pip install amaterasu-j2
$ amaterasu sample/wandbox-run.j2
```
# This file is a "Hello, world!" in Python language by CPython for wandbox.

import sys

print("Hello, world!")

if len(sys.argv) > 1:
    print(sys.argv[1])

# CPython references:
#   https://www.python.org/

```

```
Hello, world!

```

```
Hello, world!
Test

```
````

sample/wandbox-run.j2

````j2
{%- set compilers = wandbox_list() | wandbox_fnmatch_compilers("cpython-3*") %}
{%- set compiler = compilers[0].name %}
{%- set src = fread("sample/main.py") %}
```
{{ src }}
```

```
{{ wandbox_run(compiler, src).program_message }}
```

```
{{ wandbox_run(compiler, src, runtime_option="Test").program_message }}
```
````

### Use kamidana

```sh
$ pip install amaterasu-j2
$ kamidana -a=amaterasu.amaterasu sample/wandbox.j2
* cpython-3*
  * cpython-3.10.2
  * cpython-3.9.3
  * cpython-3.8.9
  * cpython-3.7.10
  * cpython-3.6.12
```

## Features

### Global

|name|usage|detail|
|:--|:--|:--|
|wandbox_list| {{ wandbox_list() }} | return wandbox compilers list json|
|wandbox_languages| {{ wandbox_languages() }} | return wandbox language list array|
|wandbox_run| {{ wandbox_run(compiler, src, \[options\], \[compier_option\], \[runtime_option\] ) }} | return wandbox compile result|

### Filter

|name|usage|detail|
|:--|:--|:--|
|wandbox_fnmatch_compilers| {{ wandbox_list() \| wandbox_fnmatch_compilers("clang-3*c") }}|filter compiler name by fnmatch|
|wandbox_language_compilers| {{ wandbox_list() \| wandbox_language_compilers("C++") }}|filter by language|

#### Utilities

[utils.py](./amaterasu/utils.py)

* markdown_link_pair
* urlencode
* url_quote
* url_quote_plus
* replace_url_quote

[kamidana]:https://github.com/podhmo/kamidana
