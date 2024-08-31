#!/usr/bin/env python3

import unittest
from  parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''Test case for access_nested_map function from utils.'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''Test access to nested map using parameterized inputs.'''
        self.assertEqual(access_nested_map(nested_map, path), expected)


    @parameterized.expand([
        ({}, ("a",), None),
        ({"a": 1}, ("a", "b"), None),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        ''' test exceptions in a nested map'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
