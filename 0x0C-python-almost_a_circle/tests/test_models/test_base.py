from models.base import Base
import unittest
"""A module that test for the value of the base class """


class Test(unittest.TestCase):
    """
     a unit test for the base class
    """

    def test_ob(self):
        """
        A function that checks for each id of object created
        """
        ob1 = Base()
        ob2 = Base(12)
        self.assertEqual(ob1.id, 1)
        self.assertEqual(ob2.id, 12)
