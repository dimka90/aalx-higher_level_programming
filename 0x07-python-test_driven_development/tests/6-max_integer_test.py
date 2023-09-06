import unittest
""" A unittest module for a list of numbers"""
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntger(unittest.TestCase):
    """
    A unittest that checks for the maximum int
    """
    def testCorrectOut(self):
        """
        a unittest for correct output
        """
        list_1 = [1, 2, 3]
        list_2 = [3, 4, 10]
        self.assertEqual(max_integer(list_1), 3)
        self.assertEqual(max_integer(list_2), 10)

    def testNegativenum(self):
        """
        a unittest function for negative integer
        """
        neg_list1 = [-2, -3, -5]
        neg_list2 = [-1, -10, -100]
        self.assertEqual(max_integer(neg_list1), -2)
        self.assertEqual(max_integer(neg_list2), -1)

    def test_neg_pos(self):
        """
        test for both negative and positve number
        """
        test_list = [10, -1, 0, -1000]
        test_list1 = [-1000, -100, 90]
        self.assertEqual(max_integer(test_list), 10)
        self.assertEqual(max_integer(test_list1), 90)

    def testEmptylist(self):
        """
        Testing for an empty list
        """
        empty_list = []
        self.assertIsNone(max_integer(empty_list), None)

    def test_one_arg(self):
        """
        testing for one argument
        """
        list_test = [10]
        self.assertEqual(max_integer(list_test), 10)

    def test_none_list(self):
        """Test for passing None as list
        """
        test_list = [None]
        self.assertIsNone(max_integer(test_list), None)

    def test_integers_and_strings(self):
        """Test for passing a string in the list
        """
        test_list = [1, 2, 3, 4, "2"]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_string_numbers(self):
        """Test for passing a string of numbers in list
        """
        test_list = ["1234"]
        self.assertEqual(max_integer(test_list), "1234")

    def test_same_integers(self):
        """Test for passing same integers in list
        """
        test_list1 = [2, 2, 2, 2, 2]
        test_list2 = [-55, -55, -55, -55]

        self.assertEqual(max_integer(test_list1), 2)
        self.assertEqual(max_integer(test_list2), -55)

    def test_zero(self):
        """Test for passing a zero in the list
        """
        test_list = [0]
        self.assertEqual(max_integer(test_list), 0)

    def test_dictionary(self):
        """Test for passing a dictionary as a list
        """
        test_list = [{'key1': 1}, {'key2': 2}]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_list_in_list(self):
        """Test for list within a list
        """
        test_list = [1, 2, 3, 4, [1, 2, 3, 4]]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_tuple_in_list(self):
        """Test for tuple within a list
        """
        test_list = [1, 2, 3, 4, (1, 2, 3)]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_set_in_list(self):
        """Test for set within a list
        """
        test_list = [1, 2, 3, 4, {1, 2, 3}]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_characters_list(self):
        """Test for list of characters
        """
        test_list = ['a', 'c', 'd', 'v']
        self.assertEqual(max_integer(test_list), 'v')

    def test_numbers_character(self):
        """Test for a list of numbers and character/s
        """
        test_list1 = [1, 2, 3, 's']
        test_list2 = [-1, -2, -3, 's']
        test_list3 = [1.1, 2.2, 3.3, 's']
        test_list4 = [-1.1, 2.2, -3.3, 's']

        with self.assertRaises(TypeError):
            max_integer(test_list1)
        with self.assertRaises(TypeError):
            max_integer(test_list2)
        with self.assertRaises(TypeError):
            max_integer(test_list3)
        with self.assertRaises(TypeError):
            max_integer(test_list4)
