#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""

    def test_max_integer_regular_case(self)
        """Unittest for max_integer([..])"""
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5)

    def test_max_integer_empty_list(self):
        """Unittest for max_integer([..])"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_negative_numbers(self):
        """Unittest for max_integer([..])"""
        result = max_integer([-1, -5, -3, -2, -4])
        self.assertEqual(result, -1)

    def test_max_integer_duplicate_max(self):
        """Unittest for max_integer([..])"""
        result = max_integer([7, 3, 7, 2, 4])
        self.assertEqual(result, 7)

    def test_max_integer_single_element_list(self):
        """Unittest for max_integer([..])"""
        x = [None]
        self.assertEqual(max_integer(x), None)

        x = [1]
        self.assertEqual(max_integer(x), 1)

        x = [7]
        self.assertEqual(max_integer(x), 7)

    def test_max_integer_mixed_data_types(self):
        """Unittest for max_integer([..])"""
        x = [1, 1, -5, 3]
        self.assertEqual(max_integer(x), 3)

        x = [100, 3, 5, 2]
        self.assertEqual(max_integer(x), 100)

        x = [-5, -4, -3, -1]
        self.assertEqual(max_integer(x), -1)

        x = [3.14, 5, 8, 9]
        self.assertEqual(max_integer(x), 9)

    def test_max_integer_negative_values(self):
        """Unittest for max_integer([..])"""
        x = [-10, -5, -15]
        self.assertEqual(max_integer(x), -5)

    def test_max_integer_duplicate_max_values(self):
        """Unittest for max_integer([..])"""
        x = [10, 1, 1, 10]
        self.assertEqual(max_integer(x), 10)

    def test_max_integer_large_values(self):
        """Unittest for max_integer([..])"""
        x = [1_000_000, 999_999, 1_000_001]
        self.assertEqual(max_integer(x), 1_000_001)

    def test_max_integer_zero_values(self):
        """Unittest for max_integer([..])"""
        x = [0, 0, 0, 0]
        self.assertEqual(max_integer(x), 0)

    def test_max_integer_mixed_sign_values(self):
        """Unittest for max_integer([..])"""
        x = [10, -5, 20, -30, 15]
        self.assertEqual(max_integer(x), 20)

    def test_max_integer_large_list(self):
        """Unittest for max_integer([..])"""
        x = list(range(1, 10_000))
        self.assertEqual(max_integer(x), 9999)

if __name__ == "__main__":
    unittest.main()
