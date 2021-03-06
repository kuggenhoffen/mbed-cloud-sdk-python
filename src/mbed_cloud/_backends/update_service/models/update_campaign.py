# coding: utf-8

"""
    Update Service API

    This is the API documentation for the Mbed deployment service, which is part of the update service.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpdateCampaign(object):
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
        'created_at': 'datetime',
        'description': 'str',
        'device_filter': 'str',
        'etag': 'str',
        'finished': 'datetime',
        'id': 'str',
        'name': 'str',
        'object': 'str',
        'phase': 'str',
        'root_manifest_id': 'str',
        'root_manifest_url': 'str',
        'started_at': 'datetime',
        'state': 'str',
        'updated_at': 'datetime',
        'when': 'datetime'
    }

    attribute_map = {
        'created_at': 'created_at',
        'description': 'description',
        'device_filter': 'device_filter',
        'etag': 'etag',
        'finished': 'finished',
        'id': 'id',
        'name': 'name',
        'object': 'object',
        'phase': 'phase',
        'root_manifest_id': 'root_manifest_id',
        'root_manifest_url': 'root_manifest_url',
        'started_at': 'started_at',
        'state': 'state',
        'updated_at': 'updated_at',
        'when': 'when'
    }

    def __init__(self, created_at=None, description=None, device_filter=None, etag=None, finished=None, id=None, name=None, object=None, phase=None, root_manifest_id=None, root_manifest_url=None, started_at=None, state=None, updated_at=None, when=None):
        """
        UpdateCampaign - a model defined in Swagger
        """

        self._created_at = created_at
        self._description = description
        self._device_filter = device_filter
        self._etag = etag
        self._finished = finished
        self._id = id
        self._name = name
        self._object = object
        self._phase = phase
        self._root_manifest_id = root_manifest_id
        self._root_manifest_url = root_manifest_url
        self._started_at = started_at
        self._state = state
        self._updated_at = updated_at
        self._when = when
        self.discriminator = None

    @property
    def created_at(self):
        """
        Gets the created_at of this UpdateCampaign.
        The time the update campaign was created

        :return: The created_at of this UpdateCampaign.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this UpdateCampaign.
        The time the update campaign was created

        :param created_at: The created_at of this UpdateCampaign.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """
        Gets the description of this UpdateCampaign.
        The optional description of the campaign

        :return: The description of this UpdateCampaign.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateCampaign.
        The optional description of the campaign

        :param description: The description of this UpdateCampaign.
        :type: str
        """
        if description is not None and len(description) > 2000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `2000`")

        self._description = description

    @property
    def device_filter(self):
        """
        Gets the device_filter of this UpdateCampaign.
        The filter for the devices the campaign will target

        :return: The device_filter of this UpdateCampaign.
        :rtype: str
        """
        return self._device_filter

    @device_filter.setter
    def device_filter(self, device_filter):
        """
        Sets the device_filter of this UpdateCampaign.
        The filter for the devices the campaign will target

        :param device_filter: The device_filter of this UpdateCampaign.
        :type: str
        """

        self._device_filter = device_filter

    @property
    def etag(self):
        """
        Gets the etag of this UpdateCampaign.
        The entity instance signature

        :return: The etag of this UpdateCampaign.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this UpdateCampaign.
        The entity instance signature

        :param etag: The etag of this UpdateCampaign.
        :type: str
        """

        self._etag = etag

    @property
    def finished(self):
        """
        Gets the finished of this UpdateCampaign.
        The campaign finish timestamp

        :return: The finished of this UpdateCampaign.
        :rtype: datetime
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """
        Sets the finished of this UpdateCampaign.
        The campaign finish timestamp

        :param finished: The finished of this UpdateCampaign.
        :type: datetime
        """

        self._finished = finished

    @property
    def id(self):
        """
        Gets the id of this UpdateCampaign.
        The campaign ID

        :return: The id of this UpdateCampaign.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UpdateCampaign.
        The campaign ID

        :param id: The id of this UpdateCampaign.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this UpdateCampaign.
        The campaign name

        :return: The name of this UpdateCampaign.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateCampaign.
        The campaign name

        :param name: The name of this UpdateCampaign.
        :type: str
        """
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")

        self._name = name

    @property
    def object(self):
        """
        Gets the object of this UpdateCampaign.
        The API resource entity

        :return: The object of this UpdateCampaign.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this UpdateCampaign.
        The API resource entity

        :param object: The object of this UpdateCampaign.
        :type: str
        """

        self._object = object

    @property
    def phase(self):
        """
        Gets the phase of this UpdateCampaign.
        The current phase of the campaign.

        :return: The phase of this UpdateCampaign.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """
        Sets the phase of this UpdateCampaign.
        The current phase of the campaign.

        :param phase: The phase of this UpdateCampaign.
        :type: str
        """

        self._phase = phase

    @property
    def root_manifest_id(self):
        """
        Gets the root_manifest_id of this UpdateCampaign.

        :return: The root_manifest_id of this UpdateCampaign.
        :rtype: str
        """
        return self._root_manifest_id

    @root_manifest_id.setter
    def root_manifest_id(self, root_manifest_id):
        """
        Sets the root_manifest_id of this UpdateCampaign.

        :param root_manifest_id: The root_manifest_id of this UpdateCampaign.
        :type: str
        """

        self._root_manifest_id = root_manifest_id

    @property
    def root_manifest_url(self):
        """
        Gets the root_manifest_url of this UpdateCampaign.

        :return: The root_manifest_url of this UpdateCampaign.
        :rtype: str
        """
        return self._root_manifest_url

    @root_manifest_url.setter
    def root_manifest_url(self, root_manifest_url):
        """
        Sets the root_manifest_url of this UpdateCampaign.

        :param root_manifest_url: The root_manifest_url of this UpdateCampaign.
        :type: str
        """

        self._root_manifest_url = root_manifest_url

    @property
    def started_at(self):
        """
        Gets the started_at of this UpdateCampaign.

        :return: The started_at of this UpdateCampaign.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """
        Sets the started_at of this UpdateCampaign.

        :param started_at: The started_at of this UpdateCampaign.
        :type: datetime
        """

        self._started_at = started_at

    @property
    def state(self):
        """
        Gets the state of this UpdateCampaign.
        The state of the campaign

        :return: The state of this UpdateCampaign.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this UpdateCampaign.
        The state of the campaign

        :param state: The state of this UpdateCampaign.
        :type: str
        """
        allowed_values = ["draft", "scheduled", "allocatingquota", "allocatedquota", "quotaallocationfailed", "checkingmanifest", "checkedmanifest", "devicefetch", "devicecopy", "devicecheck", "publishing", "deploying", "deployed", "manifestremoved", "expired", "stopping", "autostopped", "userstopped", "conflict"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def updated_at(self):
        """
        Gets the updated_at of this UpdateCampaign.
        The time the object was updated

        :return: The updated_at of this UpdateCampaign.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this UpdateCampaign.
        The time the object was updated

        :param updated_at: The updated_at of this UpdateCampaign.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def when(self):
        """
        Gets the when of this UpdateCampaign.
        The scheduled start time for the update campaign

        :return: The when of this UpdateCampaign.
        :rtype: datetime
        """
        return self._when

    @when.setter
    def when(self, when):
        """
        Sets the when of this UpdateCampaign.
        The scheduled start time for the update campaign

        :param when: The when of this UpdateCampaign.
        :type: datetime
        """

        self._when = when

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
        if not isinstance(other, UpdateCampaign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
