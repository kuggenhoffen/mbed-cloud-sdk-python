# coding: utf-8

"""
    Account Management API

    API for managing accounts, users, creating API keys, uploading trusted certificates

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserUpdateReq(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, phone_number=None, username=None, is_marketing_accepted=None, is_gtc_accepted=None, full_name=None, address=None, password=None, email=None):
        """
        UserUpdateReq - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'phone_number': 'str',
            'username': 'str',
            'is_marketing_accepted': 'bool',
            'is_gtc_accepted': 'bool',
            'full_name': 'str',
            'address': 'str',
            'password': 'str',
            'email': 'str'
        }

        self.attribute_map = {
            'phone_number': 'phone_number',
            'username': 'username',
            'is_marketing_accepted': 'is_marketing_accepted',
            'is_gtc_accepted': 'is_gtc_accepted',
            'full_name': 'full_name',
            'address': 'address',
            'password': 'password',
            'email': 'email'
        }

        self._phone_number = phone_number
        self._username = username
        self._is_marketing_accepted = is_marketing_accepted
        self._is_gtc_accepted = is_gtc_accepted
        self._full_name = full_name
        self._address = address
        self._password = password
        self._email = email

    @property
    def phone_number(self):
        """
        Gets the phone_number of this UserUpdateReq.
        Phone number, not longer than 100 characters.

        :return: The phone_number of this UserUpdateReq.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this UserUpdateReq.
        Phone number, not longer than 100 characters.

        :param phone_number: The phone_number of this UserUpdateReq.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def username(self):
        """
        Gets the username of this UserUpdateReq.
        A username containing alphanumerical letters and -,._@+= characters. It must be at least 4 but not more than 30 character long.

        :return: The username of this UserUpdateReq.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UserUpdateReq.
        A username containing alphanumerical letters and -,._@+= characters. It must be at least 4 but not more than 30 character long.

        :param username: The username of this UserUpdateReq.
        :type: str
        """

        self._username = username

    @property
    def is_marketing_accepted(self):
        """
        Gets the is_marketing_accepted of this UserUpdateReq.
        A flag indicating that receiving marketing information has been accepted.

        :return: The is_marketing_accepted of this UserUpdateReq.
        :rtype: bool
        """
        return self._is_marketing_accepted

    @is_marketing_accepted.setter
    def is_marketing_accepted(self, is_marketing_accepted):
        """
        Sets the is_marketing_accepted of this UserUpdateReq.
        A flag indicating that receiving marketing information has been accepted.

        :param is_marketing_accepted: The is_marketing_accepted of this UserUpdateReq.
        :type: bool
        """

        self._is_marketing_accepted = is_marketing_accepted

    @property
    def is_gtc_accepted(self):
        """
        Gets the is_gtc_accepted of this UserUpdateReq.
        A flag indicating that the General Terms and Conditions has been accepted.

        :return: The is_gtc_accepted of this UserUpdateReq.
        :rtype: bool
        """
        return self._is_gtc_accepted

    @is_gtc_accepted.setter
    def is_gtc_accepted(self, is_gtc_accepted):
        """
        Sets the is_gtc_accepted of this UserUpdateReq.
        A flag indicating that the General Terms and Conditions has been accepted.

        :param is_gtc_accepted: The is_gtc_accepted of this UserUpdateReq.
        :type: bool
        """

        self._is_gtc_accepted = is_gtc_accepted

    @property
    def full_name(self):
        """
        Gets the full_name of this UserUpdateReq.
        The full name of the user, not longer than 100 characters.

        :return: The full_name of this UserUpdateReq.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """
        Sets the full_name of this UserUpdateReq.
        The full name of the user, not longer than 100 characters.

        :param full_name: The full_name of this UserUpdateReq.
        :type: str
        """

        self._full_name = full_name

    @property
    def address(self):
        """
        Gets the address of this UserUpdateReq.
        Address, not longer than 100 characters.

        :return: The address of this UserUpdateReq.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this UserUpdateReq.
        Address, not longer than 100 characters.

        :param address: The address of this UserUpdateReq.
        :type: str
        """

        self._address = address

    @property
    def password(self):
        """
        Gets the password of this UserUpdateReq.
        The password when creating a new user. It will will generated when not present in the request.

        :return: The password of this UserUpdateReq.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UserUpdateReq.
        The password when creating a new user. It will will generated when not present in the request.

        :param password: The password of this UserUpdateReq.
        :type: str
        """

        self._password = password

    @property
    def email(self):
        """
        Gets the email of this UserUpdateReq.
        The email address, not longer than 254 characters.

        :return: The email of this UserUpdateReq.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserUpdateReq.
        The email address, not longer than 254 characters.

        :param email: The email of this UserUpdateReq.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

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
        if not isinstance(other, UserUpdateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
