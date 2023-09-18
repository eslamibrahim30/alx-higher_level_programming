#!/usr/bin/python3
"""
Unittest for Base class.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    This class for testing a Base class.
    """
    def testRectangleGetters(self):
        r = Rectangle(2, 3, 0, 0)
        self.assertEqual(2, r.width)
        self.assertEqual(3, r.height)
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)

    def testRectangleSetters(self):
        r = Rectangle(1, 1)
        r.width = 2
        r.height = 3
        r.x = 4
        r.y = 5
        self.assertEqual(2, r.width)
        self.assertEqual(3, r.height)
        self.assertEqual(4, r.x)
        self.assertEqual(5, r.y)

    def testRectangleHandlingErrorsWidth(self):
        with self.assertRaises(TypeError) as et:
            r = Rectangle('1', 2, 3, 4)
        self.assertEqual(str(et.exception), 'width must be an integer')
        with self.assertRaises(ValueError) as ev:
            r = Rectangle(0, 2, 3, 4)
        self.assertEqual(str(ev.exception), 'width must be > 0')

    def testRectangleHandlingErrorsHeight(self):
        with self.assertRaises(TypeError) as et:
            r = Rectangle(1, '2', 3, 4)
        self.assertEqual(str(et.exception), 'height must be an integer')
        with self.assertRaises(ValueError) as ev:
            r = Rectangle(1, -2, 3, 4)
        self.assertEqual(str(ev.exception), 'height must be > 0')

    def testRectangleHandlingErrorsX(self):
        with self.assertRaises(TypeError) as et:
            r = Rectangle(1, 2, '3', 4)
        self.assertEqual(str(et.exception), 'x must be an integer')
        with self.assertRaises(ValueError) as ev:
            r = Rectangle(1, 2, -3, 4)
        self.assertEqual(str(ev.exception), 'x must be >= 0')

    def testRectangleHandlingErrorsY(self):
        with self.assertRaises(TypeError) as et:
            r = Rectangle(1, 2, 3, '4')
        self.assertEqual(str(et.exception), 'y must be an integer')
        with self.assertRaises(ValueError) as ev:
            r = Rectangle(1, 2, 3, -1)
        self.assertEqual(str(ev.exception), 'y must be >= 0')

    def testRectangleArea(self):
        r = Rectangle(2, 4)
        self.assertEqual(8, r.area())
        self.assertEqual(8, Rectangle.area(r))
        self.assertEqual(6, Rectangle.area(Rectangle(2, 3)))

    def testRectangleDisplay(self):
        r = Rectangle(2, 2)
        self.assertEqual("##\n##", r.display())
        self.assertEqual("##\n##", Rectangle.display(r))
        self.assertEqual("##\n##\n##", Rectangle.display(Rectangle(2, 3)))


if __name__ == '__main__':
    unittest.main()
