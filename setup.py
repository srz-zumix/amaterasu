import os
import re
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

f = open(os.path.join(os.path.dirname(__file__), 'amaterasu/__init__.py'))
for line in f:
    if '__version__ = ' in line:
        version_ = [x for x in re.split(r"[ =']", line) if x][1]
    elif '__author__ = ' in line:
        author_ = [x for x in re.split(r"[ =']", line) if x][1]
f.close()

test_deps = ['importlib-metadata<2,>=0.12', 'tox', 'pytest']

setup(
    name = "amaterasu-j2"
    , version = version_
    , author = author_
    , author_email = "zumix.cpp@gmail.com"
    , url = "https://github.com/srz-zumix/amaterasu/"
    , description = "Wandbox API Jinja2 template cli."
    , license = "MIT"
    , platforms = ["any"]
    , keywords = "jinja2, cli, kamidana, Wandbox"
    , packages = ['amaterasu']
    , long_description = readme
    , long_description_content_type='text/markdown'
    , classifiers = [
        "Development Status :: 4 - Beta"
        , "Topic :: Utilities"
        , "License :: OSI Approved :: MIT License"
        , "Programming Language :: Python"
        , "Programming Language :: Python :: 3.7"
        , "Programming Language :: Python :: 3.8"
        , "Programming Language :: Python :: 3.9"
    ]
    , entry_points={
        'console_scripts': [
            'amaterasu = amaterasu.__main__:main'
        ]
    }
    , install_requires=[
        'requests'
        , 'pyyaml'
        , 'wandbox-api >= 0.9.28'
        # jinja2 <= 3.0.2 reason:
        #   https://stackoverflow.com/questions/72163382/attributeerror-module-jinja2-ext-has-no-attribute-with
        , 'jinja2 <= 3.0.2'
        # markupsafe == 2.0.1 reason:
        #   cannot import name 'soft_unicode' from 'markupsafe'
        , 'markupsafe==2.0.1'
        , 'kamidana'
    ]
    , tests_require=test_deps
    , test_suite="tests.test_suite"
    , extras_require={
        'test': test_deps
    }
)
