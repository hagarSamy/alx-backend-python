#!/usr/bin/env python3

import unittest
from  parameterized import parameterized
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
    @patch('')
    def test_memoize(self):
        # Define the TestClass within the test method
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        # Create an instance of the TestClass
        test_obj = TestClass()

        # Patch the 'a_method' to track its calls
        with patch.object(test_obj, 'a_method', wraps=test_obj.a_method) as mock_method:
            # First call should compute and cache the result
            result_first_call = test_obj.a_property
            self.assertEqual(result_first_call, 42)
            mock_method.assert_called_once()  # Ensure 'a_method' is called once

            # Reset the mock to track subsequent calls accurately
            mock_method.reset_mock()

            # Second call should use the cached result, no method call
            result_second_call = test_obj.a_property
            self.assertEqual(result_second_call, 42)
            mock_method.assert_not_called()  # Ensure 'a_method' is not called again
    


if __name__ == '__main__':
    unittest.main()
