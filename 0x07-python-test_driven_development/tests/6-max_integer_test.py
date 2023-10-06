#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        maximum = max_integer()
        two = max_integer([-20, -14, 2, 0, -8])
        minus_one = max_integer([-90, -85, -1, -19, -2])
        eighty = max_integer([80, 70, 60, 50])
        self.assertEqual(maximum, None)
        self.assertEqual(two, 2)
        self.assertEqual(minus_one, -1)
        self.assertEqual(eighty, 80)
