# coding: utf-8

"""
    Device Query Service API

    This is the API Documentation for the mbed device query service update service.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WriteDeviceQueryPage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, limit=None, after=None, data=None, order=None):
        """
        WriteDeviceQueryPage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'limit': 'int',
            'after': 'str',
            'data': 'list[DeviceQuery]',
            'order': 'str'
        }

        self.attribute_map = {
            'limit': 'limit',
            'after': 'after',
            'data': 'data',
            'order': 'order'
        }

        self._limit = limit
        self._after = after
        self._data = data
        self._order = order

    @property
    def limit(self):
        """
        Gets the limit of this WriteDeviceQueryPage.

        :return: The limit of this WriteDeviceQueryPage.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this WriteDeviceQueryPage.

        :param limit: The limit of this WriteDeviceQueryPage.
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")

        self._limit = limit

    @property
    def after(self):
        """
        Gets the after of this WriteDeviceQueryPage.

        :return: The after of this WriteDeviceQueryPage.
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """
        Sets the after of this WriteDeviceQueryPage.

        :param after: The after of this WriteDeviceQueryPage.
        :type: str
        """

        self._after = after

    @property
    def data(self):
        """
        Gets the data of this WriteDeviceQueryPage.

        :return: The data of this WriteDeviceQueryPage.
        :rtype: list[DeviceQuery]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this WriteDeviceQueryPage.

        :param data: The data of this WriteDeviceQueryPage.
        :type: list[DeviceQuery]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def order(self):
        """
        Gets the order of this WriteDeviceQueryPage.

        :return: The order of this WriteDeviceQueryPage.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this WriteDeviceQueryPage.

        :param order: The order of this WriteDeviceQueryPage.
        :type: str
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")

        self._order = order

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, WriteDeviceQueryPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
