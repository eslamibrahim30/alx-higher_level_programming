#!/usr/bin/python3
"""
Unittest for Square class.
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    This class for testing a Square class.
    """
    def testSquareHandlingErrorsSize(self):
        with self.assertRaises(TypeError) as et:
            r = Square('1', 3, 4)
        self.assertEqual(str(et.exception), 'width must be an integer')
        with self.assertRaises(ValueError) as ev:
            r = Square(0, 3, 4)
        self.assertEqual(str(ev.exception), 'width must be > 0')

    def testSquareHandlingErrorsX(self):
        with self.assertRaises(TypeError) as et:
            r = Square(1, '3', 4)
        self.assertEqual(str(et.exception), 'x must be an integer')
        with self.assertRaises(ValueError) as ev:
            r = Square(1, -3, 4)
        self.assertEqual(str(ev.exception), 'x must be >= 0')

    def testSquareHandlingErrorsY(self):
        with self.assertRaises(TypeError) as et:
            r = Square(1, 3, '4')
        self.assertEqual(str(et.exception), 'y must be an integer')
        with self.assertRaises(ValueError) as ev:
            r = Square(1, 3, -1)
        self.assertEqual(str(ev.exception), 'y must be >= 0')

    def testSquareArea(self):
        r = Square(2)
        self.assertEqual(4, r.area())
        self.assertEqual(4, Square.area(r))
        self.assertEqual(16, Square.area(Square(4)))

    def testSquareDisplay(self):
        r = Square(2)
        self.assertEqual("##\n##", r.display())
        self.assertEqual("##\n##", Square.display(r))
        self.assertEqual("####\n####\n####\n####", Square.display(Square(4)))
        self.assertEqual("\n #", Square.display(Square(1, 1, 1)))

    def testSquareStr(self):
        r = Square(4, 2, 1, 12)
        self.assertEqual("[Square] (12) 2/1 - 4", r.__str__())
        self.assertEqual("[Square] (12) 2/1 - 4", Square.__str__(r))
        my_str = Square.__str__(Square(5, 0, 0, 25))
        self.assertEqual("[Square] (25) 0/0 - 5", my_str)

if __name__ == '__main__':
    unittest.main()
