#!/usr/bin/python3
"""This module contains the uniitest for the rectangle.py
"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
import sys


class TestRectangle(unittest.TestCase):
    """class definition for TestRectangle"""
    
    def setUp(self):
        from models.rectangle import Rectangle

    def tearDown(self):
        Rectangle.set_objects(0)

    def test_IntegrateId(self):
        rectangle1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(rectangle1.id, 1)
        rectangle2 = Rectangle(1, 1, 1, 1, None)
        self.assertEqual(rectangle2.id, 2)
        rectangle3 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle3.id, 5)
        rectangle3.id = 20
        self.assertEqual(rectangle3.id, 20)
        rectangle4 = Rectangle(1, 1, 1, 1)
        self.assertEqual(rectangle4.id, 3)

    def test_InitAttrs(self):
        rectangle1 = Rectangle(1, 2)
        self.assertEqual(rectangle1.width, 1)
        self.assertEqual(rectangle1.height, 2)
        self.assertEqual(rectangle1.x, 0)
        self.assertEqual(rectangle1.y, 0)

        rectangle2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle2.width, 1)
        self.assertEqual(rectangle2.height, 2)
        self.assertEqual(rectangle2.x, 3)
        self.assertEqual(rectangle2.y, 4)
        
        rect = Rectangle(1, 2, 0, 0)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        
        with self.assertRaises(TypeError):
            rectangle3 = Rectangle()
        with self.assertRaises(TypeError):
            rectangle3 = Rectangle(1)

    def test_AttrValidateTypeError(self):
        with self.assertRaises(TypeError):
            Rectangle("width", 1, 2, 3)
        with self.assertRaises(TypeError):
            Rectangle([1], 1, 2, 3)
        with self.assertRaises(TypeError):
            Rectangle((1,), 1, 2, 3)
        with self.assertRaises(TypeError):
            Rectangle(1.0, 1, 2, 3)

        with self.assertRaises(TypeError):
            Rectangle(1, "height", 2, 3)
        with self.assertRaises(TypeError):
            Rectangle(1, [1], 2, 3)
        with self.assertRaises(TypeError):
            Rectangle(1, (1,), 2, 3)
        with self.assertRaises(TypeError):
            Rectangle(1, 1.0, 2, 3)

        with self.assertRaises(TypeError):
            Rectangle(1, 2, "height", 3)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, [1], 3)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, (1,), 3)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 0.0, 3)

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "height")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, [1])
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, (1,))
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 0.0)

        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 2, 3, (1,))
        with self.assertRaises(TypeError):
            Rectangle(float('nan'), 2, 3, (1,))
    
    def test_AttrValidateValueError(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1, 2, 3)
        with self.assertRaises(ValueError):
            Rectangle(-1, 1, 2, 3)
        with self.assertRaises(ValueError):
            Rectangle(-100, 1, 2, 3)

        with self.assertRaises(ValueError):
            Rectangle(1, 0, 2, 3)
        with self.assertRaises(ValueError):
            Rectangle(1, -1, 2, 3)
        with self.assertRaises(ValueError):
            Rectangle(1, -100, 2, 3)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1, 3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -100, 3)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -100)

    def test_area(self):
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 100)
        r3 = Rectangle(100, 1)
        r4 = Rectangle(100, 100)
        self.assertEqual(r1.area(), 1)
        self.assertEqual(r2.area(), 100)
        self.assertEqual(r3.area(), 100)
        self.assertEqual(r4.area(), 10000)

    def test_str(self):
        rectangle1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(rectangle1.__str__(), "[Rectangle] (1) 1/1 - 1/1")
        rectangle2 = Rectangle(1, 1, 1, 1, None)
        self.assertEqual(rectangle2.__str__(), "[Rectangle] (2) 1/1 - 1/1")
        rectangle3 = Rectangle(5, 7, 12, 19, 31)
        self.assertEqual(rectangle3.__str__(), "[Rectangle] (31) 12/19 - 5/7")
        rectangle4 = Rectangle(5, 7, 12, 19)
        self.assertEqual(rectangle4.__str__(), "[Rectangle] (3) 12/19 - 5/7")
        rectangle5 = Rectangle(5, 7)
        self.assertEqual(rectangle5.__str__(), "[Rectangle] (4) 0/0 - 5/7")

    def test_display(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            Rectangle(2, 2, 2, 2).display()
            expected_out = "\n\n  ##\n  ##\n"
            self.assertEqual(fake_out.getvalue(), expected_out)
            fake_out.seek(0)
            fake_out.truncate(0)
            Rectangle(1, 1).display()
            expected_out = "#\n"
            self.assertEqual(fake_out.getvalue(), expected_out)
            fake_out.seek(0)
            fake_out.truncate(0)
            Rectangle(1, 1, 1).display()
            expected_out = " #\n"
            self.assertEqual(fake_out.getvalue(), expected_out)
            fake_out.seek(0)
            fake_out.truncate(0)
            Rectangle(1, 1, y = 1).display()
            expected_out = "\n#\n"
            self.assertEqual(fake_out.getvalue(), expected_out)
            fake_out.seek(0)
            fake_out.truncate(0)

    def test_update0(self):
        rectangle = Rectangle(2, 2, 2, 2)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            rectangle.update()
            print(rectangle)
            expected = "[Rectangle] (1) 2/2 - 2/2\n"
            self.assertEqual(fake_out.getvalue(), expected)
            fake_out.seek(0)
            fake_out.truncate(0)
            
            rectangle.update(None)
            print(rectangle)
            expected = "[Rectangle] (2) 2/2 - 2/2\n"
            self.assertEqual(fake_out.getvalue(), expected)
            fake_out.seek(0)
            fake_out.truncate(0)

            rectangle.update(67)
            print(rectangle)
            expected = "[Rectangle] (67) 2/2 - 2/2\n"
            self.assertEqual(fake_out.getvalue(), expected)
            fake_out.seek(0)
            fake_out.truncate(0)
            
            rectangle.update(None, 23, 24)
            print(rectangle)
            expected = "[Rectangle] (3) 2/2 - 23/24\n"
            self.assertEqual(fake_out.getvalue(), expected)
            fake_out.seek(0)
            fake_out.truncate(0)
            
            rectangle.update(89, 23, 24, 14, 15)
            print(rectangle)
            expected = "[Rectangle] (89) 14/15 - 23/24\n"
            self.assertEqual(fake_out.getvalue(), expected)
            fake_out.seek(0)
            fake_out.truncate(0)
            
            rectangle.update(89, 23, 24, 14, 15, 2, 4, 5)
            print(rectangle)
            expected = "[Rectangle] (89) 14/15 - 23/24\n"
            self.assertEqual(fake_out.getvalue(), expected)
            fake_out.seek(0)
            fake_out.truncate(0)
        
        self.assertRaises(ValueError, rectangle.update, None, 0)
        self.assertRaises(ValueError, rectangle.update, None, 10, -1)
        self.assertRaises(ValueError, rectangle.update, None, 10, 1, -1)
        
        self.assertRaises(TypeError, rectangle.update, None, [10], 1, -1)
        self.assertRaises(TypeError, rectangle.update, None, 10, "1", 1)
