# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from samsungtv_server.models.error_response import ErrorResponse  # noqa: E501
from samsungtv_server.models.status_response import StatusResponse  # noqa: E501
from samsungtv_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_status(self):
        """Test case for get_status

        
        """
        response = self.client.open(
            '/status',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_key(self):
        """Test case for post_key

        
        """
        response = self.client.open(
            '/key/{key}'.format(key='key_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
