# coding: utf-8

"""
    mbed-billing REST API documentation for API-server

    This document contains the public REST API definitions of the mbed-billing service's API server component.

    OpenAPI spec version: 1.3.7-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Health(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, iam=None, psql=None, all=None, last_updated=None):
        """
        Health - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'iam': 'bool',
            'psql': 'bool',
            'all': 'bool',
            'last_updated': 'datetime'
        }

        self.attribute_map = {
            'iam': 'iam',
            'psql': 'psql',
            'all': 'all',
            'last_updated': 'last_updated'
        }

        self._iam = iam
        self._psql = psql
        self._all = all
        self._last_updated = last_updated

    @property
    def iam(self):
        """
        Gets the iam of this Health.

        :return: The iam of this Health.
        :rtype: bool
        """
        return self._iam

    @iam.setter
    def iam(self, iam):
        """
        Sets the iam of this Health.

        :param iam: The iam of this Health.
        :type: bool
        """
        if iam is None:
            raise ValueError("Invalid value for `iam`, must not be `None`")

        self._iam = iam

    @property
    def psql(self):
        """
        Gets the psql of this Health.

        :return: The psql of this Health.
        :rtype: bool
        """
        return self._psql

    @psql.setter
    def psql(self, psql):
        """
        Sets the psql of this Health.

        :param psql: The psql of this Health.
        :type: bool
        """
        if psql is None:
            raise ValueError("Invalid value for `psql`, must not be `None`")

        self._psql = psql

    @property
    def all(self):
        """
        Gets the all of this Health.

        :return: The all of this Health.
        :rtype: bool
        """
        return self._all

    @all.setter
    def all(self, all):
        """
        Sets the all of this Health.

        :param all: The all of this Health.
        :type: bool
        """
        if all is None:
            raise ValueError("Invalid value for `all`, must not be `None`")

        self._all = all

    @property
    def last_updated(self):
        """
        Gets the last_updated of this Health.

        :return: The last_updated of this Health.
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """
        Sets the last_updated of this Health.

        :param last_updated: The last_updated of this Health.
        :type: datetime
        """
        if last_updated is None:
            raise ValueError("Invalid value for `last_updated`, must not be `None`")

        self._last_updated = last_updated

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
        if not isinstance(other, Health):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
