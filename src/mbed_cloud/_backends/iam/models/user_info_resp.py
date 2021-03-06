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


class UserInfoResp(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_id': 'str',
        'address': 'str',
        'created_at': 'datetime',
        'creation_time': 'int',
        'custom_fields': 'dict(str, str)',
        'email': 'str',
        'email_verified': 'bool',
        'etag': 'str',
        'full_name': 'str',
        'groups': 'list[str]',
        'id': 'str',
        'is_gtc_accepted': 'bool',
        'is_marketing_accepted': 'bool',
        'is_totp_enabled': 'bool',
        'last_login_time': 'int',
        'login_history': 'list[LoginHistory]',
        'object': 'str',
        'password': 'str',
        'password_changed_time': 'int',
        'phone_number': 'str',
        'status': 'str',
        'updated_at': 'datetime',
        'username': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'address': 'address',
        'created_at': 'created_at',
        'creation_time': 'creation_time',
        'custom_fields': 'custom_fields',
        'email': 'email',
        'email_verified': 'email_verified',
        'etag': 'etag',
        'full_name': 'full_name',
        'groups': 'groups',
        'id': 'id',
        'is_gtc_accepted': 'is_gtc_accepted',
        'is_marketing_accepted': 'is_marketing_accepted',
        'is_totp_enabled': 'is_totp_enabled',
        'last_login_time': 'last_login_time',
        'login_history': 'login_history',
        'object': 'object',
        'password': 'password',
        'password_changed_time': 'password_changed_time',
        'phone_number': 'phone_number',
        'status': 'status',
        'updated_at': 'updated_at',
        'username': 'username'
    }

    def __init__(self, account_id=None, address=None, created_at=None, creation_time=None, custom_fields=None, email=None, email_verified=None, etag=None, full_name=None, groups=None, id=None, is_gtc_accepted=None, is_marketing_accepted=None, is_totp_enabled=None, last_login_time=None, login_history=None, object=None, password=None, password_changed_time=None, phone_number=None, status=None, updated_at=None, username=None):
        """
        UserInfoResp - a model defined in Swagger
        """

        self._account_id = account_id
        self._address = address
        self._created_at = created_at
        self._creation_time = creation_time
        self._custom_fields = custom_fields
        self._email = email
        self._email_verified = email_verified
        self._etag = etag
        self._full_name = full_name
        self._groups = groups
        self._id = id
        self._is_gtc_accepted = is_gtc_accepted
        self._is_marketing_accepted = is_marketing_accepted
        self._is_totp_enabled = is_totp_enabled
        self._last_login_time = last_login_time
        self._login_history = login_history
        self._object = object
        self._password = password
        self._password_changed_time = password_changed_time
        self._phone_number = phone_number
        self._status = status
        self._updated_at = updated_at
        self._username = username
        self.discriminator = None

    @property
    def account_id(self):
        """
        Gets the account_id of this UserInfoResp.
        The UUID of the account.

        :return: The account_id of this UserInfoResp.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this UserInfoResp.
        The UUID of the account.

        :param account_id: The account_id of this UserInfoResp.
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")

        self._account_id = account_id

    @property
    def address(self):
        """
        Gets the address of this UserInfoResp.
        Address.

        :return: The address of this UserInfoResp.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this UserInfoResp.
        Address.

        :param address: The address of this UserInfoResp.
        :type: str
        """

        self._address = address

    @property
    def created_at(self):
        """
        Gets the created_at of this UserInfoResp.
        Creation UTC time RFC3339.

        :return: The created_at of this UserInfoResp.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this UserInfoResp.
        Creation UTC time RFC3339.

        :param created_at: The created_at of this UserInfoResp.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def creation_time(self):
        """
        Gets the creation_time of this UserInfoResp.
        A timestamp of the user creation in the storage, in milliseconds.

        :return: The creation_time of this UserInfoResp.
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this UserInfoResp.
        A timestamp of the user creation in the storage, in milliseconds.

        :param creation_time: The creation_time of this UserInfoResp.
        :type: int
        """

        self._creation_time = creation_time

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this UserInfoResp.
        User's account specific custom properties. The value is a string.

        :return: The custom_fields of this UserInfoResp.
        :rtype: dict(str, str)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this UserInfoResp.
        User's account specific custom properties. The value is a string.

        :param custom_fields: The custom_fields of this UserInfoResp.
        :type: dict(str, str)
        """

        self._custom_fields = custom_fields

    @property
    def email(self):
        """
        Gets the email of this UserInfoResp.
        The email address.

        :return: The email of this UserInfoResp.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserInfoResp.
        The email address.

        :param email: The email of this UserInfoResp.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def email_verified(self):
        """
        Gets the email_verified of this UserInfoResp.
        A flag indicating whether the user's email address has been verified or not.

        :return: The email_verified of this UserInfoResp.
        :rtype: bool
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, email_verified):
        """
        Sets the email_verified of this UserInfoResp.
        A flag indicating whether the user's email address has been verified or not.

        :param email_verified: The email_verified of this UserInfoResp.
        :type: bool
        """

        self._email_verified = email_verified

    @property
    def etag(self):
        """
        Gets the etag of this UserInfoResp.
        API resource entity version.

        :return: The etag of this UserInfoResp.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this UserInfoResp.
        API resource entity version.

        :param etag: The etag of this UserInfoResp.
        :type: str
        """
        if etag is None:
            raise ValueError("Invalid value for `etag`, must not be `None`")

        self._etag = etag

    @property
    def full_name(self):
        """
        Gets the full_name of this UserInfoResp.
        The full name of the user.

        :return: The full_name of this UserInfoResp.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """
        Sets the full_name of this UserInfoResp.
        The full name of the user.

        :param full_name: The full_name of this UserInfoResp.
        :type: str
        """

        self._full_name = full_name

    @property
    def groups(self):
        """
        Gets the groups of this UserInfoResp.
        A list of IDs of the groups this user belongs to.

        :return: The groups of this UserInfoResp.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this UserInfoResp.
        A list of IDs of the groups this user belongs to.

        :param groups: The groups of this UserInfoResp.
        :type: list[str]
        """

        self._groups = groups

    @property
    def id(self):
        """
        Gets the id of this UserInfoResp.
        The UUID of the user.

        :return: The id of this UserInfoResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserInfoResp.
        The UUID of the user.

        :param id: The id of this UserInfoResp.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_gtc_accepted(self):
        """
        Gets the is_gtc_accepted of this UserInfoResp.
        A flag indicating that the General Terms and Conditions has been accepted.

        :return: The is_gtc_accepted of this UserInfoResp.
        :rtype: bool
        """
        return self._is_gtc_accepted

    @is_gtc_accepted.setter
    def is_gtc_accepted(self, is_gtc_accepted):
        """
        Sets the is_gtc_accepted of this UserInfoResp.
        A flag indicating that the General Terms and Conditions has been accepted.

        :param is_gtc_accepted: The is_gtc_accepted of this UserInfoResp.
        :type: bool
        """

        self._is_gtc_accepted = is_gtc_accepted

    @property
    def is_marketing_accepted(self):
        """
        Gets the is_marketing_accepted of this UserInfoResp.
        A flag indicating that receiving marketing information has been accepted.

        :return: The is_marketing_accepted of this UserInfoResp.
        :rtype: bool
        """
        return self._is_marketing_accepted

    @is_marketing_accepted.setter
    def is_marketing_accepted(self, is_marketing_accepted):
        """
        Sets the is_marketing_accepted of this UserInfoResp.
        A flag indicating that receiving marketing information has been accepted.

        :param is_marketing_accepted: The is_marketing_accepted of this UserInfoResp.
        :type: bool
        """

        self._is_marketing_accepted = is_marketing_accepted

    @property
    def is_totp_enabled(self):
        """
        Gets the is_totp_enabled of this UserInfoResp.
        A flag indicating whether 2-factor authentication (TOTP) has been enabled.

        :return: The is_totp_enabled of this UserInfoResp.
        :rtype: bool
        """
        return self._is_totp_enabled

    @is_totp_enabled.setter
    def is_totp_enabled(self, is_totp_enabled):
        """
        Sets the is_totp_enabled of this UserInfoResp.
        A flag indicating whether 2-factor authentication (TOTP) has been enabled.

        :param is_totp_enabled: The is_totp_enabled of this UserInfoResp.
        :type: bool
        """

        self._is_totp_enabled = is_totp_enabled

    @property
    def last_login_time(self):
        """
        Gets the last_login_time of this UserInfoResp.
        A timestamp of the latest login of the user, in milliseconds.

        :return: The last_login_time of this UserInfoResp.
        :rtype: int
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, last_login_time):
        """
        Sets the last_login_time of this UserInfoResp.
        A timestamp of the latest login of the user, in milliseconds.

        :param last_login_time: The last_login_time of this UserInfoResp.
        :type: int
        """

        self._last_login_time = last_login_time

    @property
    def login_history(self):
        """
        Gets the login_history of this UserInfoResp.
        Timestamps, succeedings, IP addresses and user agent information of the last five logins of the user, with timestamps in RFC3339 format.

        :return: The login_history of this UserInfoResp.
        :rtype: list[LoginHistory]
        """
        return self._login_history

    @login_history.setter
    def login_history(self, login_history):
        """
        Sets the login_history of this UserInfoResp.
        Timestamps, succeedings, IP addresses and user agent information of the last five logins of the user, with timestamps in RFC3339 format.

        :param login_history: The login_history of this UserInfoResp.
        :type: list[LoginHistory]
        """

        self._login_history = login_history

    @property
    def object(self):
        """
        Gets the object of this UserInfoResp.
        Entity name: always 'user'

        :return: The object of this UserInfoResp.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this UserInfoResp.
        Entity name: always 'user'

        :param object: The object of this UserInfoResp.
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")
        allowed_values = ["user"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def password(self):
        """
        Gets the password of this UserInfoResp.
        The password when creating a new user. It will be generated when not present in the request.

        :return: The password of this UserInfoResp.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UserInfoResp.
        The password when creating a new user. It will be generated when not present in the request.

        :param password: The password of this UserInfoResp.
        :type: str
        """

        self._password = password

    @property
    def password_changed_time(self):
        """
        Gets the password_changed_time of this UserInfoResp.
        A timestamp of the latest change of the user password, in milliseconds.

        :return: The password_changed_time of this UserInfoResp.
        :rtype: int
        """
        return self._password_changed_time

    @password_changed_time.setter
    def password_changed_time(self, password_changed_time):
        """
        Sets the password_changed_time of this UserInfoResp.
        A timestamp of the latest change of the user password, in milliseconds.

        :param password_changed_time: The password_changed_time of this UserInfoResp.
        :type: int
        """

        self._password_changed_time = password_changed_time

    @property
    def phone_number(self):
        """
        Gets the phone_number of this UserInfoResp.
        Phone number.

        :return: The phone_number of this UserInfoResp.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this UserInfoResp.
        Phone number.

        :param phone_number: The phone_number of this UserInfoResp.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def status(self):
        """
        Gets the status of this UserInfoResp.
        The status of the user. ENROLLING state indicates that the user is in the middle of the enrollment process. INVITED means that the user has not accepted the invitation request. RESET means that the password must be changed immediately. INACTIVE users are locked out and not permitted to use the system.

        :return: The status of this UserInfoResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UserInfoResp.
        The status of the user. ENROLLING state indicates that the user is in the middle of the enrollment process. INVITED means that the user has not accepted the invitation request. RESET means that the password must be changed immediately. INACTIVE users are locked out and not permitted to use the system.

        :param status: The status of this UserInfoResp.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        allowed_values = ["ENROLLING", "INVITED", "ACTIVE", "RESET", "INACTIVE"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def updated_at(self):
        """
        Gets the updated_at of this UserInfoResp.
        Last update UTC time RFC3339.

        :return: The updated_at of this UserInfoResp.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this UserInfoResp.
        Last update UTC time RFC3339.

        :param updated_at: The updated_at of this UserInfoResp.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def username(self):
        """
        Gets the username of this UserInfoResp.
        A username containing alphanumerical letters and -,._@+= characters.

        :return: The username of this UserInfoResp.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UserInfoResp.
        A username containing alphanumerical letters and -,._@+= characters.

        :param username: The username of this UserInfoResp.
        :type: str
        """

        self._username = username

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
        if not isinstance(other, UserInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
