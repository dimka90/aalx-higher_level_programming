#!/usr/bin/python3
""" A unnitest module for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    """

    def test_one_instance(self):
        print("TEST ONE")
        b = Base()
        actual = b.id
        expected = 1
        print("Id", b.id)
        print("=========")
        self.assertEqual(actual, expected)

    def test_two(self):
        b1 = Base()
        actual = b1.id
        expected = 2
        print("I am godd")
        self.assertEqual(actual, b1.id)

    def test_three(self):
        b = Base()
        b1 = Base()
        b2 = Base()
        actual = 5
        expected = 5
        print("coding is fun")
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
