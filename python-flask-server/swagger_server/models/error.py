# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Error(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, err_msg: str=None):  # noqa: E501
        """Error - a model defined in Swagger

        :param err_msg: The error message if Hash is not found.  # noqa: E501
        :type err_msg: str
        """
        self.swagger_types = {
            'err_msg': str
        }

        self.attribute_map = {
            'err_msg': 'err_msg'
        }

        self._err_msg = err_msg

    @classmethod
    def from_dict(cls, dikt) -> 'Error':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The err_msg of this err_msg.  # noqa: E501
        :rtype: err_msg
        """
        return util.deserialize_model(dikt, cls)

    @property
    def err_msg(self) -> str:
        """Gets the message of this err_msg.


        :return: The message of this err_msg.
        :rtype: str
        """
        return self._err_msg

    @err_msg.setter
    def err_msg(self, err_msg: str):
        """Sets the message of this err_msg.


        :param digest: The message of this err_msg.
        :type digest: str
        """
        if err_msg is None:
            raise ValueError("Invalid value for `err_msg`, must not be `None`")  # noqa: E501

        self._err_msg = err_msg
