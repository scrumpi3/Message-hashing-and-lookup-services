import connexion
import six
import hashlib

from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server import util

hashDictionary = {}

def add_message(body):  # noqa: E501
    """Add a new message to the store

     # noqa: E501

    :param body: message to store
    :type body: dict | bytes

    :rtype: Hash
    """
    if connexion.request.is_json:
        body = Message.from_dict(connexion.request.get_json())  # noqa: E501
    message = body.message.encode('utf-8')
    hasher = hashlib.sha256()
    hasher.update(message)
    hashDigest = hasher.hexdigest()
    hashDictionary[hashDigest] = message
    return hashDigest


def get_msg_by_hash(hash):  # noqa: E501
    """Find message by hash

    Returns a single message # noqa: E501

    :param hash: Hash of message to return
    :type hash: str

    :rtype: Message
    """
    storedMessage = hashDictionary[hash].decode("utf-8")
    returnedValue =  Hash(storedMessage)
    return returnedValue
