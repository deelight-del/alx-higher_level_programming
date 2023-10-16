#!/usr/bin/python3
"""This module contains the uniitest for the rectangle.py
"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square
import sys
import json


class TestSquare(unittest.TestCase):
    """class definition for TestSquare"""
    
    def setUp(self):
        from models.square import Square

    def tearDown(self):
        Square.set_objects(0)

    def test_IntegrateId(self):
        square1 = Square(1, 1, 1)
        self.assertEqual(square1.id, 1)
        square2 = Square(1, 1, 1, None)
        self.assertEqual(square2.id, 2)

        square3 = Square(2, 3, 4, 5)
        self.assertEqual(square3.id, 5)
        square3.id = 20
        self.assertEqual(square3.id, 20)
        square4 = Square(1, 1, 1)
        self.assertEqual(square4.id, 3)

    def test_InitAttrs(self):
        square1 = Square(2)
        self.assertEqual(square1.width, 2)
        self.assertEqual(square1.height, 2)
        self.assertEqual(square1.size, 2)
        self.assertEqual(square1.x, 0)
        self.assertEqual(square1.y, 0)

        """Test width, height and size equality to on one another when using
        the dot notation"""
        square1.width = 7
        self.assertEqual(square1.width, 7)
        self.assertEqual(square1.size, 7)
        self.assertNotEqual(square1.height, 7)
        square1.height = 8
        self.assertEqual(square1.height, 8)
        self.assertNotEqual(square1.size, 8)
        self.assertNotEqual(square1.width, 8)
        square1.size = 10
        self.assertEqual(square1.height, 10)
        self.assertEqual(square1.size, 10)
        self.assertEqual(square1.width, 10)
        
        """Iniitializing size, and check effect on width and height
        Also changing x via dot notaion on"""
        square2 = Square(2, 3, 4)
        self.assertEqual(square2.size, 2)
        self.assertEqual(square2.width, 2)
        self.assertEqual(square2.height, 2)
        self.assertEqual(square2.x, 3)
        self.assertEqual(square2.y, 4)
        square2.x = 100
        self.assertEqual(square2.x, 100)
        square2.y = 120
        self.assertEqual(square2.y, 120)
        sq = Square(2, 0, 0)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        
        """Check for TypeErrors, whenn require args is not passed"""
        with self.assertRaises(TypeError):
            square3 = Square()
        with self.assertRaises(TypeError):
            square3 = Square(y=120)

    def test_AttrValidateTypeError(self):
        with self.assertRaises(TypeError):
            Square("width", 2, 3)
        with self.assertRaises(TypeError):
            Square([1], 2, 3)
        with self.assertRaises(TypeError):
            Square((1,), 2, 3)
        with self.assertRaises(TypeError):
            Square(1.0, 2, 3)
        with self.assertRaises(TypeError):
            square1 = Square(20, 2, 3)
            square1.width = "width"
        with self.assertRaises(TypeError):
            square1 = Square(20, 2, 3)
            square1.width = 20.0
        with self.assertRaises(TypeError):
            square1 = Square(20, 2, 3)
            square1.height = "width"
        with self.assertRaises(TypeError):
            square1 = Square(20, 2, 3)
            square1.height = 20.0
        with self.assertRaises(TypeError):
            square1 = Square(20, 2, 3)
            square1.size = 20.0
        with self.assertRaises(TypeError):
            square1 = Square(20, 2, 3)
            square1.size = "98"
        with self.assertRaises(TypeError):
            square1 = Square(20, 2, 3)
            square1.height = (98,)

        """Type Error of the x attribute"""
        with self.assertRaises(TypeError):
            Square(2, "height", 3)
        with self.assertRaises(TypeError):
            Square(2, [1], 3)
        with self.assertRaises(TypeError):
            Square(2, (1,), 3)
        with self.assertRaises(TypeError):
            Square(2, 0.0, 3)
        with self.assertRaises(TypeError):
            square1 = Square(20, 2, 3)
            square1.x = "98"
        with self.assertRaises(TypeError):
            square1 = Square(20, 2, 3)
            square1.x = (98,)
        with self.assertRaises(TypeError):
            square1 = Square(20, 2, 3)
            square1.x = 98.0
        with self.assertRaises(TypeError):
            square1 = Square(20, 2, 3)
            square1.x = [98]

        """Tyepe Error for the y attribute"""
        with self.assertRaises(TypeError):
            Square(2, 3, "height")
        with self.assertRaises(TypeError):
            Square(1, 3, [1])
        with self.assertRaises(TypeError):
            Square(2, 3, (1,))
        with self.assertRaises(TypeError):
            Square(2, 3, 0.0)
        with self.assertRaises(TypeError):
            square1 = Square(20, 2, 3)
            square1.y = "98"
        with self.assertRaises(TypeError):
            square1 = Square(20, 2, 3)
            square1.y = (98,)
        with self.assertRaises(TypeError):
            square1 = Square(20, 2, 3)
            square1.y = 98.0
        with self.assertRaises(TypeError):
            square1 = Square(20, 2, 3)
            square1.y = [98]

        with self.assertRaises(TypeError):
            Square(float('inf'), 3, (1,))
        with self.assertRaises(TypeError):
            Square(float('nan'), 3, (1,))
    
    def test_AttrValidateValueError(self):
        with self.assertRaises(ValueError):
            Square(0, 2, 3)
        with self.assertRaises(ValueError):
            Square(-1, 2, 3)
        with self.assertRaises(ValueError):
            Square(-100, 2, 3)
        with self.assertRaises(ValueError):
            square1 = Square(100, 2, 3)
            square1.width = 0
        with self.assertRaises(ValueError):
            square1 = Square(100, 2, 3)
            square1.width = -1
        with self.assertRaises(ValueError):
            square1 = Square(100, 2, 3)
            square1.height = 0
        with self.assertRaises(ValueError):
            square1 = Square(100, 2, 3)
            square1.height = -1
        with self.assertRaises(ValueError):
            square1 = Square(100, 2, 3)
            square1.size = 0
        with self.assertRaises(ValueError):
            square1 = Square(100, 2, 3)
            square1.size = -1

        with self.assertRaises(ValueError):
            Square(1, 2, -1, 3)
        with self.assertRaises(ValueError):
            Square(1, 2, -100, 3)
        with self.assertRaises(ValueError):
            square1 = Square(100, 2, 3)
            square1.x = -1
        with self.assertRaises(ValueError):
            square1 = Square(100, 2, 3)
            square1.x = -100

        with self.assertRaises(ValueError):
            Square(2, 3, -1)
        with self.assertRaises(ValueError):
            Square(2, 3, -100)
        with self.assertRaises(ValueError):
            square1 = Square(100, 2, 3)
            square1.y = -1
        with self.assertRaises(ValueError):
            square1 = Square(100, 2, 3)
            square1.y = -100

    def test_area(self):
        r1 = Square(1)
        r2 = Square(100)
        self.assertEqual(r1.area(), 1)
        self.assertEqual(r2.area(), 10000)

    def test_str(self):
        square1 = Square(1, 1, 1)
        self.assertEqual(square1.__str__(), "[Square] (1) 1/1 - 1")
        square2 = Square(1, 1, 1, None)
        self.assertEqual(square2.__str__(), "[Square] (2) 1/1 - 1")
        square3 = Square(7, 12, 19, 31)
        self.assertEqual(square3.__str__(), "[Square] (31) 12/19 - 7")
        square4 = Square(5, 12, 19)
        self.assertEqual(square4.__str__(), "[Square] (3) 12/19 - 5")
        square5 = Square(7)
        self.assertEqual(square5.__str__(), "[Square] (4) 0/0 - 7")

    def test_display(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            Square(2, 2, 2).display()
            expected_out = "\n\n  ##\n  ##\n"
            self.assertEqual(fake_out.getvalue(), expected_out)
            fake_out.seek(0)
            fake_out.truncate(0)
            Square(1).display()
            expected_out = "#\n"
            self.assertEqual(fake_out.getvalue(), expected_out)
            fake_out.seek(0)
            fake_out.truncate(0)
            Square(1, 1).display()
            expected_out = " #\n"
            self.assertEqual(fake_out.getvalue(), expected_out)
            fake_out.seek(0)
            fake_out.truncate(0)
            Square(1, y = 1).display()
            expected_out = "\n#\n"
            self.assertEqual(fake_out.getvalue(), expected_out)
            fake_out.seek(0)
            fake_out.truncate(0)

    def test_update(self):
        square = Square(1, 2, 3)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            square.update()
            print(square)
            expected = "[Square] (1) 2/3 - 1\n"
            self.assertEqual(fake_out.getvalue(), expected)
            fake_out.seek(0)
            fake_out.truncate(0)
            
            square.update(None)
            print(square)
            expected = "[Square] (2) 2/3 - 1\n"
            self.assertEqual(fake_out.getvalue(), expected)
            fake_out.seek(0)
            fake_out.truncate(0)

            square.update(67)
            print(square)
            expected = "[Square] (67) 2/3 - 1\n"
            self.assertEqual(fake_out.getvalue(), expected)
            fake_out.seek(0)
            fake_out.truncate(0)
            
            square.update(None, 23)
            print(square)
            expected = "[Square] (3) 2/3 - 23\n"
            self.assertEqual(fake_out.getvalue(), expected)
            fake_out.seek(0)
            fake_out.truncate(0)
            
            square.update(89, 23, 24, 14)
            print(square)
            expected = "[Square] (89) 24/14 - 23\n"
            self.assertEqual(fake_out.getvalue(), expected)
            fake_out.seek(0)
            fake_out.truncate(0)
            
            square.update(89, 23, 24, 14, 15, 2, 4, 5)
            print(square)
            expected = "[Square] (89) 24/14 - 23\n"
            self.assertEqual(fake_out.getvalue(), expected)
            fake_out.seek(0)
            fake_out.truncate(0)
            
            square.update(id=89, x=14, size=24, y=15)
            print(square)
            expected = "[Square] (89) 14/15 - 24\n"
            self.assertEqual(fake_out.getvalue(), expected)
            fake_out.seek(0)
            fake_out.truncate(0)
            
            square = Square(15)
            square.update(89, id=89, x=14, height=24, y=15, width=23)
            print(square)
            expected = "[Square] (89) 0/0 - 15\n"
            self.assertEqual(fake_out.getvalue(), expected)
            fake_out.seek(0)
            fake_out.truncate(0)
        
        self.assertRaises(ValueError, square.update, None, 0)
        self.assertRaises(ValueError, square.update, None, 10, -1)
        self.assertRaises(ValueError, square.update, None, 10, 1, -1)
        self.assertRaises(ValueError, square.update, id = None, size = 0)
        self.assertRaises(ValueError, square.update, id = None, size = 10, x = -1)
        self.assertRaises(ValueError, square.update, id = None, size = 10, x = 1, y = -1)
        
        self.assertRaises(TypeError, square.update, None, [10], 1, -1)
        self.assertRaises(TypeError, square.update, None, 10, "1", 1)

    def test_dictionary(self):
        square = Square(10, 20, 30)
        self.assertDictEqual(square.to_dictionary(),
                {'id': 1, 'size': 10, 'x': 20, 'y': 30})
    
    def test_save_to_file(self):
        s1 = Square(7, 2, 8, 89)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        expected_out = [{"y": 8, "x": 2, "id": 89, "size": 7}, 
                {"y": 0, "x": 0, "id": 1, "size": 2}]
        with open('Square.json', 'r') as f:
            actual_out = json.load(f)
        self.assertEqual(actual_out, expected_out)
        
        Square.save_to_file(None)
        expected_out = []
        with open('Square.json', 'r') as f:
            actual_out = json.load(f)
        self.assertEqual(actual_out, expected_out)
