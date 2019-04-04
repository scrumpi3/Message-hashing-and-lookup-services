import connexion
import six

from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server import util


def add_message(body):  # noqa: E501
    """Add a new pet to the store

     # noqa: E501

    :param body: order placed for purchasing the pet
    :type body: dict | bytes

    :rtype: Hash
    """
    if connexion.request.is_json:
        body = Message.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_msg_by_hash(hash):  # noqa: E501
    """Find message by hash

    Returns a single message # noqa: E501

    :param hash: Hash of message to return
    :type hash: str

    :rtype: Message
    """
    return 'do some magic!'
