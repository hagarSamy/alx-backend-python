#!/usr/bin/env python3
'''A module to handle different test concepts with test clients'''

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
from urllib import request
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''test GithubOrgClient class'''
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        '''tests that GithubOrgClient.org returns the correct value'''
        test_client = GithubOrgClient(org_name)
        response = test_client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(response, {"payload": True})

if __name__ == '__main__':
    unittest.main()
