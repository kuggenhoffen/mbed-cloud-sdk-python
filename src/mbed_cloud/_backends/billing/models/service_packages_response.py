# coding: utf-8

"""
    billing REST API documentation

    This document contains the public REST API definitions of the mbed-billing service.

    OpenAPI spec version: 1.4.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ServicePackagesResponse(object):
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
        'active': 'ActiveServicePackage',
        'object': 'str',
        'pending': 'PendingServicePackage',
        'previous': 'list[PreviousServicePackage]'
    }

    attribute_map = {
        'active': 'active',
        'object': 'object',
        'pending': 'pending',
        'previous': 'previous'
    }

    def __init__(self, active=None, object=None, pending=None, previous=None):
        """
        ServicePackagesResponse - a model defined in Swagger
        """

        self._active = active
        self._object = object
        self._pending = pending
        self._previous = previous
        self.discriminator = None

    @property
    def active(self):
        """
        Gets the active of this ServicePackagesResponse.
        Currently active service package. Can be null.

        :return: The active of this ServicePackagesResponse.
        :rtype: ActiveServicePackage
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this ServicePackagesResponse.
        Currently active service package. Can be null.

        :param active: The active of this ServicePackagesResponse.
        :type: ActiveServicePackage
        """

        self._active = active

    @property
    def object(self):
        """
        Gets the object of this ServicePackagesResponse.
        Always set to 'service-packages'.

        :return: The object of this ServicePackagesResponse.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this ServicePackagesResponse.
        Always set to 'service-packages'.

        :param object: The object of this ServicePackagesResponse.
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")
        allowed_values = ["service-packages"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def pending(self):
        """
        Gets the pending of this ServicePackagesResponse.
        Current pending service package. Can be null.

        :return: The pending of this ServicePackagesResponse.
        :rtype: PendingServicePackage
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """
        Sets the pending of this ServicePackagesResponse.
        Current pending service package. Can be null.

        :param pending: The pending of this ServicePackagesResponse.
        :type: PendingServicePackage
        """

        self._pending = pending

    @property
    def previous(self):
        """
        Gets the previous of this ServicePackagesResponse.
        List of previous service packages.

        :return: The previous of this ServicePackagesResponse.
        :rtype: list[PreviousServicePackage]
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """
        Sets the previous of this ServicePackagesResponse.
        List of previous service packages.

        :param previous: The previous of this ServicePackagesResponse.
        :type: list[PreviousServicePackage]
        """
        if previous is None:
            raise ValueError("Invalid value for `previous`, must not be `None`")

        self._previous = previous

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
        if not isinstance(other, ServicePackagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
