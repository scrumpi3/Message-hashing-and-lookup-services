# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMessagesController(BaseTestCase):
    """MessagesController integration test stubs"""

    def test_add_empty_message(self):
        """Test case for add_message

        Add a new empty message to the store
        """
        body = Message()
        response = self.client.open('/messages', method='POST',
                                    data=json.dumps(body), content_type='application/json')
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))
    
    def test_add_nonempty_message(self):
        """Test case for add_message
            
            Add a new empty message to the store
            """
        body = Message("foo")
        response = self.client.open('/messages', method='POST',
                                    data=json.dumps(body), content_type='application/json')
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_get_hash_not_found(self):
        """Test case for get_msg_by_hash

        Return message not found for unknown hash
        """
        response = self.client.open('/messages/{hash}'.format(hash='hash_example'), method='GET')
        self.assert404(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_get_msg_by_hash_not_found(self):
        """Test case combining add_message and get_msg_by_hash
            
        Create a  message and retrieve its hash.
        Then retreive the message using its hash
        """
        messageText = "foo"
        body = Message(messageText)
        postResponse = self.client.open('/messages', method='POST',
                                    data=json.dumps(body), content_type='application/json')
        self.assert200(postResponse, 'Response body is : ' + postResponse.data.decode('utf-8'))
        responseHash = postResponse.json['digest']
        
        getResponse = self.client.open('/messages/{hash}'.format(hash=responseHash), method='GET')
        self.assert200(getResponse, 'Response body is : ' + getResponse.data.decode('utf-8'))
        responseMessage = getResponse.json['message']

        assert(responseMessage == messageText)



if __name__ == '__main__':
    import unittest
    unittest.main()
