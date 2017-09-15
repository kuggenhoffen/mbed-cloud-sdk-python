# coding: utf-8

"""
    Connect Statistics API

    mbed Cloud Connect Statistics API provides statistics about other cloud services through defined counters.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Metric(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, registration_updates=None, connect_rest_api_success=None, bootstraps_failed=None, transactions=None, timestamp=None, device_subscription_request_error=None, bootstraps_pending=None, device_proxy_request_success=None, bootstraps_successful=None, full_registrations=None, device_subscription_request_success=None, expired_registrations=None, handshakes_successful=None, device_observations=None, device_proxy_request_error=None, deleted_registrations=None, connect_rest_api_error=None, id=None):
        """
        Metric - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'registration_updates': 'int',
            'connect_rest_api_success': 'int',
            'bootstraps_failed': 'int',
            'transactions': 'int',
            'timestamp': 'datetime',
            'device_subscription_request_error': 'int',
            'bootstraps_pending': 'int',
            'device_proxy_request_success': 'int',
            'bootstraps_successful': 'int',
            'full_registrations': 'int',
            'device_subscription_request_success': 'int',
            'expired_registrations': 'int',
            'handshakes_successful': 'int',
            'device_observations': 'int',
            'device_proxy_request_error': 'int',
            'deleted_registrations': 'int',
            'connect_rest_api_error': 'int',
            'id': 'str'
        }

        self.attribute_map = {
            'registration_updates': 'registration_updates',
            'connect_rest_api_success': 'connect_rest_api_success',
            'bootstraps_failed': 'bootstraps_failed',
            'transactions': 'transactions',
            'timestamp': 'timestamp',
            'device_subscription_request_error': 'device_subscription_request_error',
            'bootstraps_pending': 'bootstraps_pending',
            'device_proxy_request_success': 'device_proxy_request_success',
            'bootstraps_successful': 'bootstraps_successful',
            'full_registrations': 'full_registrations',
            'device_subscription_request_success': 'device_subscription_request_success',
            'expired_registrations': 'expired_registrations',
            'handshakes_successful': 'handshakes_successful',
            'device_observations': 'device_observations',
            'device_proxy_request_error': 'device_proxy_request_error',
            'deleted_registrations': 'deleted_registrations',
            'connect_rest_api_error': 'connect_rest_api_error',
            'id': 'id'
        }

        self._registration_updates = registration_updates
        self._connect_rest_api_success = connect_rest_api_success
        self._bootstraps_failed = bootstraps_failed
        self._transactions = transactions
        self._timestamp = timestamp
        self._device_subscription_request_error = device_subscription_request_error
        self._bootstraps_pending = bootstraps_pending
        self._device_proxy_request_success = device_proxy_request_success
        self._bootstraps_successful = bootstraps_successful
        self._full_registrations = full_registrations
        self._device_subscription_request_success = device_subscription_request_success
        self._expired_registrations = expired_registrations
        self._handshakes_successful = handshakes_successful
        self._device_observations = device_observations
        self._device_proxy_request_error = device_proxy_request_error
        self._deleted_registrations = deleted_registrations
        self._connect_rest_api_error = connect_rest_api_error
        self._id = id

    @property
    def registration_updates(self):
        """
        Gets the registration_updates of this Metric.
        The number of registration updates linked to the account. Registration update is the process of updating the registration status with the Mbed Cloud Connect to update or extend the lifetime of the device.

        :return: The registration_updates of this Metric.
        :rtype: int
        """
        return self._registration_updates

    @registration_updates.setter
    def registration_updates(self, registration_updates):
        """
        Sets the registration_updates of this Metric.
        The number of registration updates linked to the account. Registration update is the process of updating the registration status with the Mbed Cloud Connect to update or extend the lifetime of the device.

        :param registration_updates: The registration_updates of this Metric.
        :type: int
        """

        self._registration_updates = registration_updates

    @property
    def connect_rest_api_success(self):
        """
        Gets the connect_rest_api_success of this Metric.
        The number of successful [Connect API](/docs/v1.2/api-references/connect-api.html) requests the account has performed. The metric do not consider the actual response from the device and it includes only the result of the http request used to subscibe to the device resources.

        :return: The connect_rest_api_success of this Metric.
        :rtype: int
        """
        return self._connect_rest_api_success

    @connect_rest_api_success.setter
    def connect_rest_api_success(self, connect_rest_api_success):
        """
        Sets the connect_rest_api_success of this Metric.
        The number of successful [Connect API](/docs/v1.2/api-references/connect-api.html) requests the account has performed. The metric do not consider the actual response from the device and it includes only the result of the http request used to subscibe to the device resources.

        :param connect_rest_api_success: The connect_rest_api_success of this Metric.
        :type: int
        """

        self._connect_rest_api_success = connect_rest_api_success

    @property
    def bootstraps_failed(self):
        """
        Gets the bootstraps_failed of this Metric.
        The number of failed bootstraps the account has performed. Bootstrap is the process of provisioning a Lightweight Machine to Machine Client to a state where it can initiate a management session to a new Lightweight Machine to Machine Server.

        :return: The bootstraps_failed of this Metric.
        :rtype: int
        """
        return self._bootstraps_failed

    @bootstraps_failed.setter
    def bootstraps_failed(self, bootstraps_failed):
        """
        Sets the bootstraps_failed of this Metric.
        The number of failed bootstraps the account has performed. Bootstrap is the process of provisioning a Lightweight Machine to Machine Client to a state where it can initiate a management session to a new Lightweight Machine to Machine Server.

        :param bootstraps_failed: The bootstraps_failed of this Metric.
        :type: int
        """

        self._bootstraps_failed = bootstraps_failed

    @property
    def transactions(self):
        """
        Gets the transactions of this Metric.
        The number of transaction events from or to devices linked to the account. A transaction is a 512-byte block of data processed by mbed Cloud. It can be either sent by the device (device --> mbed cloud) or received by the device (mbed cloud --> device). A transaction does not include IP, TCP or UDP, TLS or DTLS packet overhead. It only contains the packet payload (full CoAP packet including CoAP headers).

        :return: The transactions of this Metric.
        :rtype: int
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """
        Sets the transactions of this Metric.
        The number of transaction events from or to devices linked to the account. A transaction is a 512-byte block of data processed by mbed Cloud. It can be either sent by the device (device --> mbed cloud) or received by the device (mbed cloud --> device). A transaction does not include IP, TCP or UDP, TLS or DTLS packet overhead. It only contains the packet payload (full CoAP packet including CoAP headers).

        :param transactions: The transactions of this Metric.
        :type: int
        """

        self._transactions = transactions

    @property
    def timestamp(self):
        """
        Gets the timestamp of this Metric.
        UTC time in RFC3339 format. The timestamp is the starting point of the interval for which the data is aggregated. Each interval includes data for the time greater than or equal to the timestamp and less than the next interval's starting point.

        :return: The timestamp of this Metric.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this Metric.
        UTC time in RFC3339 format. The timestamp is the starting point of the interval for which the data is aggregated. Each interval includes data for the time greater than or equal to the timestamp and less than the next interval's starting point.

        :param timestamp: The timestamp of this Metric.
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def device_subscription_request_error(self):
        """
        Gets the device_subscription_request_error of this Metric.
        The number of failed subscription requests from Mbed Cloud Connect to devices linked to the account. The subscription requests are made from Mbed Cloud Connect to devices when you try to subscribe to a resource path using [Connect API](/docs/v1.2/api-references/connect-api.html) endpoints.

        :return: The device_subscription_request_error of this Metric.
        :rtype: int
        """
        return self._device_subscription_request_error

    @device_subscription_request_error.setter
    def device_subscription_request_error(self, device_subscription_request_error):
        """
        Sets the device_subscription_request_error of this Metric.
        The number of failed subscription requests from Mbed Cloud Connect to devices linked to the account. The subscription requests are made from Mbed Cloud Connect to devices when you try to subscribe to a resource path using [Connect API](/docs/v1.2/api-references/connect-api.html) endpoints.

        :param device_subscription_request_error: The device_subscription_request_error of this Metric.
        :type: int
        """

        self._device_subscription_request_error = device_subscription_request_error

    @property
    def bootstraps_pending(self):
        """
        Gets the bootstraps_pending of this Metric.
        The number of pending bootstraps the account has performed. Bootstrap is the process of provisioning a Lightweight Machine to Machine Client to a state where it can initiate a management session to a new Lightweight Machine to Machine Server.

        :return: The bootstraps_pending of this Metric.
        :rtype: int
        """
        return self._bootstraps_pending

    @bootstraps_pending.setter
    def bootstraps_pending(self, bootstraps_pending):
        """
        Sets the bootstraps_pending of this Metric.
        The number of pending bootstraps the account has performed. Bootstrap is the process of provisioning a Lightweight Machine to Machine Client to a state where it can initiate a management session to a new Lightweight Machine to Machine Server.

        :param bootstraps_pending: The bootstraps_pending of this Metric.
        :type: int
        """

        self._bootstraps_pending = bootstraps_pending

    @property
    def device_proxy_request_success(self):
        """
        Gets the device_proxy_request_success of this Metric.
        The number of successful proxy requests from Mbed Cloud Connect to devices linked to the account. The proxy requests are made from Mbed Cloud Connect to devices when you try to read or write values to device resources using [Connect API](/docs/v1.2/api-references/connect-api.html) endpoints.

        :return: The device_proxy_request_success of this Metric.
        :rtype: int
        """
        return self._device_proxy_request_success

    @device_proxy_request_success.setter
    def device_proxy_request_success(self, device_proxy_request_success):
        """
        Sets the device_proxy_request_success of this Metric.
        The number of successful proxy requests from Mbed Cloud Connect to devices linked to the account. The proxy requests are made from Mbed Cloud Connect to devices when you try to read or write values to device resources using [Connect API](/docs/v1.2/api-references/connect-api.html) endpoints.

        :param device_proxy_request_success: The device_proxy_request_success of this Metric.
        :type: int
        """

        self._device_proxy_request_success = device_proxy_request_success

    @property
    def bootstraps_successful(self):
        """
        Gets the bootstraps_successful of this Metric.
        The number of successful bootstraps the account has performed. Bootstrap is the process of provisioning a Lightweight Machine to Machine Client to a state where it can initiate a management session to a new Lightweight Machine to Machine Server.

        :return: The bootstraps_successful of this Metric.
        :rtype: int
        """
        return self._bootstraps_successful

    @bootstraps_successful.setter
    def bootstraps_successful(self, bootstraps_successful):
        """
        Sets the bootstraps_successful of this Metric.
        The number of successful bootstraps the account has performed. Bootstrap is the process of provisioning a Lightweight Machine to Machine Client to a state where it can initiate a management session to a new Lightweight Machine to Machine Server.

        :param bootstraps_successful: The bootstraps_successful of this Metric.
        :type: int
        """

        self._bootstraps_successful = bootstraps_successful

    @property
    def full_registrations(self):
        """
        Gets the full_registrations of this Metric.
        The number of full registrations linked to the account. Full registration is the process of registering a device with the Mbed Cloud Connect by providing its lifetime and capabilities such as the resource structure.The registered status of the device does not guarantee that the device is active and accessible from Mebd Cloud Connect at any point of time.

        :return: The full_registrations of this Metric.
        :rtype: int
        """
        return self._full_registrations

    @full_registrations.setter
    def full_registrations(self, full_registrations):
        """
        Sets the full_registrations of this Metric.
        The number of full registrations linked to the account. Full registration is the process of registering a device with the Mbed Cloud Connect by providing its lifetime and capabilities such as the resource structure.The registered status of the device does not guarantee that the device is active and accessible from Mebd Cloud Connect at any point of time.

        :param full_registrations: The full_registrations of this Metric.
        :type: int
        """

        self._full_registrations = full_registrations

    @property
    def device_subscription_request_success(self):
        """
        Gets the device_subscription_request_success of this Metric.
        The number of successful subscription requests from Mbed Cloud Connect to devices linked to the account. The subscription requests are made from Mbed Cloud Connect to devices when you try to subscribe to a resource path using [Connect API](/docs/v1.2/api-references/connect-api.html) endpoints.

        :return: The device_subscription_request_success of this Metric.
        :rtype: int
        """
        return self._device_subscription_request_success

    @device_subscription_request_success.setter
    def device_subscription_request_success(self, device_subscription_request_success):
        """
        Sets the device_subscription_request_success of this Metric.
        The number of successful subscription requests from Mbed Cloud Connect to devices linked to the account. The subscription requests are made from Mbed Cloud Connect to devices when you try to subscribe to a resource path using [Connect API](/docs/v1.2/api-references/connect-api.html) endpoints.

        :param device_subscription_request_success: The device_subscription_request_success of this Metric.
        :type: int
        """

        self._device_subscription_request_success = device_subscription_request_success

    @property
    def expired_registrations(self):
        """
        Gets the expired_registrations of this Metric.
        The number of expired registrations linked to the account. Mbed Cloud Connect removes the device registrations when the devices cannot update their registration before the expiry of the lifetime. Mbed Cloud Connect no longer handles requests for a device whose registration has expired already.

        :return: The expired_registrations of this Metric.
        :rtype: int
        """
        return self._expired_registrations

    @expired_registrations.setter
    def expired_registrations(self, expired_registrations):
        """
        Sets the expired_registrations of this Metric.
        The number of expired registrations linked to the account. Mbed Cloud Connect removes the device registrations when the devices cannot update their registration before the expiry of the lifetime. Mbed Cloud Connect no longer handles requests for a device whose registration has expired already.

        :param expired_registrations: The expired_registrations of this Metric.
        :type: int
        """

        self._expired_registrations = expired_registrations

    @property
    def handshakes_successful(self):
        """
        Gets the handshakes_successful of this Metric.
        The number of successful TLS handshakes the account has performed. The SSL or TLS handshake enables the SSL or TLS client and server to establish the secret keys with which they communicate. A successful TLS handshake is required for establishing a connection with Mbed Cloud Connect for any operaton such as registration, registration update and deregistration.

        :return: The handshakes_successful of this Metric.
        :rtype: int
        """
        return self._handshakes_successful

    @handshakes_successful.setter
    def handshakes_successful(self, handshakes_successful):
        """
        Sets the handshakes_successful of this Metric.
        The number of successful TLS handshakes the account has performed. The SSL or TLS handshake enables the SSL or TLS client and server to establish the secret keys with which they communicate. A successful TLS handshake is required for establishing a connection with Mbed Cloud Connect for any operaton such as registration, registration update and deregistration.

        :param handshakes_successful: The handshakes_successful of this Metric.
        :type: int
        """

        self._handshakes_successful = handshakes_successful

    @property
    def device_observations(self):
        """
        Gets the device_observations of this Metric.
        The number of observations received by Mbed Cloud Connect from the devices linked to the account. The observations are pushed from the device to Mbed Cloud Connect when you have successfully subscribed to the device resources using [Connect API](/docs/v1.2/api-references/connect-api.html) endpoints.

        :return: The device_observations of this Metric.
        :rtype: int
        """
        return self._device_observations

    @device_observations.setter
    def device_observations(self, device_observations):
        """
        Sets the device_observations of this Metric.
        The number of observations received by Mbed Cloud Connect from the devices linked to the account. The observations are pushed from the device to Mbed Cloud Connect when you have successfully subscribed to the device resources using [Connect API](/docs/v1.2/api-references/connect-api.html) endpoints.

        :param device_observations: The device_observations of this Metric.
        :type: int
        """

        self._device_observations = device_observations

    @property
    def device_proxy_request_error(self):
        """
        Gets the device_proxy_request_error of this Metric.
        The number of failed proxy requests from Mbed Cloud Connect to devices linked to the account. The proxy requests are made from Mbed Cloud Connect to devices when you try to read or write values to device resources using [Connect API](/docs/v1.2/api-references/connect-api.html) endpoints.

        :return: The device_proxy_request_error of this Metric.
        :rtype: int
        """
        return self._device_proxy_request_error

    @device_proxy_request_error.setter
    def device_proxy_request_error(self, device_proxy_request_error):
        """
        Sets the device_proxy_request_error of this Metric.
        The number of failed proxy requests from Mbed Cloud Connect to devices linked to the account. The proxy requests are made from Mbed Cloud Connect to devices when you try to read or write values to device resources using [Connect API](/docs/v1.2/api-references/connect-api.html) endpoints.

        :param device_proxy_request_error: The device_proxy_request_error of this Metric.
        :type: int
        """

        self._device_proxy_request_error = device_proxy_request_error

    @property
    def deleted_registrations(self):
        """
        Gets the deleted_registrations of this Metric.
        The number of deleted registrations (deregistrations) linked to the account. Deregistration is the process of removing the device registration from the Mbed Cloud Connect registry. The deregistration is usually initiated by the device. Mbed Cloud Connect no longer handles requests for a deregistered device.

        :return: The deleted_registrations of this Metric.
        :rtype: int
        """
        return self._deleted_registrations

    @deleted_registrations.setter
    def deleted_registrations(self, deleted_registrations):
        """
        Sets the deleted_registrations of this Metric.
        The number of deleted registrations (deregistrations) linked to the account. Deregistration is the process of removing the device registration from the Mbed Cloud Connect registry. The deregistration is usually initiated by the device. Mbed Cloud Connect no longer handles requests for a deregistered device.

        :param deleted_registrations: The deleted_registrations of this Metric.
        :type: int
        """

        self._deleted_registrations = deleted_registrations

    @property
    def connect_rest_api_error(self):
        """
        Gets the connect_rest_api_error of this Metric.
        The number of failed [Connect API](/docs/v1.2/api-references/connect-api.html) requests the account has performed.The metric do not consider the actual response from the device and it includes only the result of the http request used to subscibe to the device resources.

        :return: The connect_rest_api_error of this Metric.
        :rtype: int
        """
        return self._connect_rest_api_error

    @connect_rest_api_error.setter
    def connect_rest_api_error(self, connect_rest_api_error):
        """
        Sets the connect_rest_api_error of this Metric.
        The number of failed [Connect API](/docs/v1.2/api-references/connect-api.html) requests the account has performed.The metric do not consider the actual response from the device and it includes only the result of the http request used to subscibe to the device resources.

        :param connect_rest_api_error: The connect_rest_api_error of this Metric.
        :type: int
        """

        self._connect_rest_api_error = connect_rest_api_error

    @property
    def id(self):
        """
        Gets the id of this Metric.
        A unique metric ID.

        :return: The id of this Metric.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Metric.
        A unique metric ID.

        :param id: The id of this Metric.
        :type: str
        """

        self._id = id

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
        if not isinstance(other, Metric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
