"""This contain the test module to test for our
base.py module that initializes objects
"""


from models.base import Base
import unittest


class TestBaseInit(unittest.TestCase):
    """Class definition to test the Base class initializer
    """
    def test_init(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)

        base2 = Base()
        self.assertEqual(base2.id, 2)

        base3 = Base(12)
        self.assertEqual(base3.id, 12)

        base4 = Base()
        self.assertEqual(base4.id, 3)
