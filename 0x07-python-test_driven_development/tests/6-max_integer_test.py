#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):

    """run test with python3 -m unittest -v tests.6-max_integer_test"""

    def test_module_docstring_len(self):
        moduleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDoc) > 1)

    def test_func_docstring_len(self):
        functionDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(functionDoc) > 1)

    def test_signed_unsigned_mixed_ints_floats(self):
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-16.5, -2.5, -1]), -1)
        self.assertEqual(max_integer([7.1, -1.9, 1, 0]), 7.1)
        self.assertEqual(max_integer([{7, 9.1}, {2}, {3}]), {7, 9.1})

    def test_strings_list(self):
        self.assertEqual(max_integer("081"), '8')
        self.assertEqual(max_integer("temitope"), 't')
        self.assertEqual(max_integer(['t', 'e', 'm', 'i', 't', 'o', 'p', 'e']), 't')
        self.assertEqual(max_integer(["sharon", 'x']), 'x')

    def test_lists(self):
        self.assertEqual(max_integer([[1, 2], [1, 3]]), [1, 3])

    def test_on_errors(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2}, {3, 4, 5})
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3, 4, 5})
        with self.assertRaises(TypeError):
            max_integer([-10, 0.5, "str", {1, 2}])
        with self.assertRaises(TypeError):
            max_integer([None, True])

    def test_with_none_data(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([None]), None)

if __name__ == "__main__":
    unittest.main()
