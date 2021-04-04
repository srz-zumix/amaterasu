try:
    import unittest2 as unittest
except:
    import unittest

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class amaterasu_test_base(unittest.TestCase):
    pass

class test_amaterasu_cli(amaterasu_test_base):

    def test_pass(self):
        pass
