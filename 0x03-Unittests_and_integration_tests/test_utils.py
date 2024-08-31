#!/usr/bin/env python3
'''A module to handle different test concepts'''

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
from urllib import request


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
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        ''' test exceptions in a nested map'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Test case for get_json from utils'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        # Set up the mock response object
        mock_get.return_value.json.return_value = test_payload

        # Call the function under test
        result = get_json(test_url)

        # Assertions to verify the behavior
        self.assertEqual(result, test_payload)
        # mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    '''Test case for memoize from utils'''

    def test_memoize(self):
        '''testing memoize'''
        # Define the TestClass within the test method
        class TestClass:
            '''test class'''
            def a_method(self):
                '''a method to check with'''
                return 42

            @memoize
            def a_property(self):
                ''' method to check call behavior'''
                return self.a_method()
        test_obj = TestClass()
        with patch.object(test_obj, 'a_method',
                          return_value=42) as mock_a_method:
            test_obj.a_property
            test_obj.a_property

            mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
