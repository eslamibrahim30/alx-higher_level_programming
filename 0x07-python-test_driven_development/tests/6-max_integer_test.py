#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):    
    def test_max(self):
        self.assertEqual(max_integer([1, 3, 4, -6]), 4)
        self.assertEqual(max_integer([-10, -5, -2, -6]), -2)
        self.assertEqual(max_integer([0, -4, -2, -6]), 0)
        self.assertEqual(max_integer([0, -4, -2, 6]), 6)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
