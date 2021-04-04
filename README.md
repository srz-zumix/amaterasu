# amaterasu

It is wandbox additional of [kamidana][] of jinja2 cli

amaterasu cli is kamidana wrapper, Adds additional option automatically.

## Usage

```sh
$ pip install amaterasu
$ amaterasu sample/wandbox.j2
* clang-3*c
  * clang-3.9.1-c
  * clang-3.8.1-c
  * clang-3.7.1-c
  * clang-3.6.0-c
  * clang-3.5.0-c
  * clang-3.4-c
  * clang-3.3-c
  * clang-3.2-c
  * clang-3.1-c
```

sample/wandbox.j2

```j2
* clang-3*c
{%- set compilers = wandbox_list() | wandbox_fnmatch_compilers("*clang-3*c") %}
{%- for compiler in compilers %}
  * {{ compiler.name }}
{%- endfor %}
```

### Use kamidana

```sh
$ pip install amaterasu
$ kamidana -a=amaterasu.amaterasu sample/wandbox.j2
* clang-3*c
  * clang-3.9.1-c
  * clang-3.8.1-c
  * clang-3.7.1-c
  * clang-3.6.0-c
  * clang-3.5.0-c
  * clang-3.4-c
  * clang-3.3-c
  * clang-3.2-c
  * clang-3.1-c
```

## Features

### Global

|name|usage|detail|
|:--|:--|:--|
|wandbox_list| {{ wandbox_list }} | return wandbox compilers list json|
|wandbox_languages| {{ wandbox_languages }} | return wandbox language list array|

### Filter

|name|usage|detail|
|:--|:--|:--|
|wandbox_fnmatch_compilers| {{ wandbox_list | wandbox_fnmatch_compilers("clang-3*c") }}|filter compiler name by fnmatch|
|wandbox_language_compilers| {{ wandbox_list | wandbox_language_compilers("C++") }}|filter by language|

#### Utilities

[utils.py](./amaterasu/utils.py)

* markdown_link_pair
* urlencode
* url_quote
* url_quote_plus
* replace_url_quote

[kamidana]:https://github.com/podhmo/kamidana
