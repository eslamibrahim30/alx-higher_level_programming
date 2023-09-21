#!/usr/bin/python3
"""
Unittest for Base class.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    This class for testing a Base class.
    """
    def testBaseCreateWithArg(self):
        b = Base(12)
        self.assertIsNotNone(b)
        self.assertIsInstance(b, Base)
        self.assertEqual(b.id, 12)

    def testBaseCreateNoArg(self):
        b0 = Base(15)
        b1 = Base()
        b2 = Base()
        self.assertIsNotNone(b0)
        self.assertIsInstance(b0, Base)
        self.assertEqual(b0.id, 15)
        self.assertIsNotNone(b1)
        self.assertIsInstance(b1, Base)
        self.assertEqual(b1.id, 1)
        self.assertIsNotNone(b2)
        self.assertIsInstance(b2, Base)
        self.assertEqual(b2.id, 2)

    def testBaseToJSONString(self):
        dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dictionary = Base.to_json_string([dictionary])
        expected_json = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(type(json_dictionary), str)
        self.assertEqual(json_dictionary, expected_json)

if __name__ == '__main__':
    unittest.main()
