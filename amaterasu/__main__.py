#!/usr/bin/env python
#
# __main__.py
#

import sys
import kamidana.commands.onefile as kamidana
from argparse import ArgumentParser
from . import __version__ as VERSION


def main():
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version=u'%(prog)s version ' + VERSION
    )
    opts, args = parser.parse_known_args()
    sys.argv = ['kamidana'] + args + ['-a=amaterasu.amaterasu', '-a=amaterasu.utils']
    kamidana.main()


if __name__ == '__main__':
    main()
