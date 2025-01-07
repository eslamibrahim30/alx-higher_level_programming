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
    def testSquareGetters(self):
        r = Square(2)
        self.assertEqual(2, r.size)

    def testSquareSetters(self):
        r = Square(1, 1)
        r.size = 2
        self.assertEqual(2, r.size)

    def testNegativeDimensions(self):
        with self.assertRaises(ValueError) as ev:
            r = Square(-1)
        self.assertEqual(str(ev.exception), 'width must be > 0')

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

    def testSquareUpdate(self):
        r = Square(4, 2, 1, 12)
        self.assertEqual("[Square] (12) 2/1 - 4", r.__str__())
        r.update(13)
        self.assertEqual("[Square] (13) 2/1 - 4", r.__str__())
        r.update(12, 3)
        self.assertEqual("[Square] (12) 2/1 - 3", r.__str__())
        r.update(height=1)
        self.assertEqual("[Square] (12) 2/1 - 3", r.__str__())
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual("[Square] (89) 3/1 - 2", r.__str__())
        r.update(4, 6, y=8, x=9)
        self.assertEqual("[Square] (4) 3/1 - 6", r.__str__())
        r.update(1, y=8, x=9)
        self.assertEqual("[Square] (1) 3/1 - 6", r.__str__())

    def testSquareToDictionary(self):
        sq1 = Square(10, 1, 9, 1)
        check_dict = {'x': 1, 'y': 9, 'id': 1, 'size': 10}
        sq1_dict = sq1.to_dictionary()
        self.assertEqual(dict, type(sq1_dict))
        self.assertEqual(check_dict, sq1_dict)
        sq2 = Square(3, 11)
        new_dict = sq1_dict
        sq2.update(**new_dict)
        self.assertNotEqual(sq1, sq2)

    def testSquareCreate(self):
        r1 = Square.create(**{'id': 1})
        r2 = Square.create(**{'id': 2, 'size': 1})
        r3 = Square.create(**{'id': 3, 'size': 1, 'x': 2})
        r4 = Square.create(**{'id': 4, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r4.id, 4)
        self.assertEqual(r2.size, 1)
        self.assertEqual(r3.size, 1)
        self.assertEqual(r4.size, 1)
        self.assertEqual(r3.x, 2)
        self.assertEqual(r4.x, 2)
        self.assertEqual(r4.y, 3)


if __name__ == '__main__':
    unittest.main()
