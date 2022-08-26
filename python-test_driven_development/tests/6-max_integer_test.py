import unittest
import sys

sys.path.append('..')
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    # def max_integer(list=[]):
    def test_list_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_str(self):
        with self.assertRaises(TypeError):
            (max_integer([1, 2, 3, 'red']))

    def test_negative_int(self):
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)

    def test_one_number_in_list(self):
        self.assertEqual(max_integer([3]), 3)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([6, 2, 4, 5]), 6)
