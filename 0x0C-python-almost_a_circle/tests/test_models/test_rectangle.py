#!/usr/bin/python3
"""
Unittest for Rectangle class.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    This class for testing a Rectangle class.
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
        self.assertEqual("\n #\n #", Rectangle.display(Rectangle(1, 2, 1, 1)))

    def testRectangleStr(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual("[Rectangle] (12) 2/1 - 4/6", r.__str__())
        self.assertEqual("[Rectangle] (12) 2/1 - 4/6", Rectangle.__str__(r))
        my_str = Rectangle.__str__(Rectangle(5, 5, 0, 0, 25))
        self.assertEqual("[Rectangle] (25) 0/0 - 5/5", my_str)

    def testRectangleUpdate(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual("[Rectangle] (12) 2/1 - 4/6", r.__str__())
        r.update(13)
        self.assertEqual("[Rectangle] (13) 2/1 - 4/6", r.__str__())
        r.update(12, 3)
        self.assertEqual("[Rectangle] (12) 2/1 - 3/6", r.__str__())
        r.update(height=1)
        self.assertEqual("[Rectangle] (12) 2/1 - 3/1", r.__str__())
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual("[Rectangle] (89) 3/1 - 2/1", r.__str__())
        r.update(4, 6, y=8, x=9)
        self.assertEqual("[Rectangle] (4) 3/1 - 6/1", r.__str__())
        r.update(1, y=8, x=9)
        self.assertEqual("[Rectangle] (1) 3/1 - 6/1", r.__str__())

    def testRectangleToDictionary(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        check_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        rect1_dict = r1.to_dictionary()
        self.assertEqual(dict, type(rect1_dict))
        self.assertEqual(check_dict, rect1_dict)
        r2 = Rectangle(3, 11)
        new_dict = rect1_dict
        r2.update(**new_dict)
        self.assertNotEqual(r1, r2)

if __name__ == '__main__':
    unittest.main()
