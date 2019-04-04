# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMessagesController(BaseTestCase):
    """MessagesController integration test stubs"""

    def test_add_message(self):
        """Test case for add_message

        Add a new message to the store
        """
        body = Message()
        response = self.client.open(
            '//messages',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_msg_by_hash(self):
        """Test case for get_msg_by_hash

        Find message by hash
        """
        response = self.client.open(
            '//messages/{hash}'.format(hash='hash_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
