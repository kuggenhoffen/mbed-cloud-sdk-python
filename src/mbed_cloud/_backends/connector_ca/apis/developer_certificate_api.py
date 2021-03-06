# coding: utf-8

"""
    Connect CA API

    mbed Cloud Connect CA API allows services to get device credentials.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class DeveloperCertificateApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_developer_certificate(self, authorization, body, **kwargs):
        """
        Create a new developer certificate to connect to the bootstrap server.
        This REST API is intended to be used by customers to get a developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server).  **Note:** The number of developer certificates allowed per account is limited. Please see [Using your own certificate authority](/docs/v1.2/mbed-cloud-deploy/instructions-for-factory-setup-and-device-provision.html#using-your-own-certificate-authority-with-mbed-cloud).  **Example usage:** curl -X POST \"http://api.us-east-1.mbedcloud.com/v3/developer-certificates\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\" -H \"content-type: application/json\" -d \"{ \\\"name\\\": \\\"THE_CERTIFICATE_NAME\\\", \\\"description\\\": \\\"THE_CERTIFICATE_DESCRIPTION\\\"}\"         
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_developer_certificate(authorization, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Bearer {Access Token}.  (required)
        :param DeveloperCertificateRequestData body: (required)
        :return: DeveloperCertificateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_developer_certificate_with_http_info(authorization, body, **kwargs)
        else:
            (data) = self.create_developer_certificate_with_http_info(authorization, body, **kwargs)
            return data

    def create_developer_certificate_with_http_info(self, authorization, body, **kwargs):
        """
        Create a new developer certificate to connect to the bootstrap server.
        This REST API is intended to be used by customers to get a developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server).  **Note:** The number of developer certificates allowed per account is limited. Please see [Using your own certificate authority](/docs/v1.2/mbed-cloud-deploy/instructions-for-factory-setup-and-device-provision.html#using-your-own-certificate-authority-with-mbed-cloud).  **Example usage:** curl -X POST \"http://api.us-east-1.mbedcloud.com/v3/developer-certificates\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\" -H \"content-type: application/json\" -d \"{ \\\"name\\\": \\\"THE_CERTIFICATE_NAME\\\", \\\"description\\\": \\\"THE_CERTIFICATE_DESCRIPTION\\\"}\"         
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_developer_certificate_with_http_info(authorization, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: Bearer {Access Token}.  (required)
        :param DeveloperCertificateRequestData body: (required)
        :return: DeveloperCertificateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'body']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_developer_certificate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `create_developer_certificate`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_developer_certificate`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api('/v3/developer-certificates', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeveloperCertificateResponseData',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_developer_certificate(self, developer_certificate_id, authorization, **kwargs):
        """
        Fetch an existing developer certificate to connect to the bootstrap server.
        This REST API is intended to be used by customers to fetch an existing developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server).  **Example usage:** curl -X GET \"http://api.us-east-1.mbedcloud.com/v3/developer-certificates/THE_CERTIFICATE_ID\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\" 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_developer_certificate(developer_certificate_id, authorization, async=True)
        >>> result = thread.get()

        :param async bool
        :param str developer_certificate_id: A unique identifier for the developer certificate.  (required)
        :param str authorization: Bearer {Access Token}.  (required)
        :return: DeveloperCertificateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_developer_certificate_with_http_info(developer_certificate_id, authorization, **kwargs)
        else:
            (data) = self.get_developer_certificate_with_http_info(developer_certificate_id, authorization, **kwargs)
            return data

    def get_developer_certificate_with_http_info(self, developer_certificate_id, authorization, **kwargs):
        """
        Fetch an existing developer certificate to connect to the bootstrap server.
        This REST API is intended to be used by customers to fetch an existing developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server).  **Example usage:** curl -X GET \"http://api.us-east-1.mbedcloud.com/v3/developer-certificates/THE_CERTIFICATE_ID\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\" 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_developer_certificate_with_http_info(developer_certificate_id, authorization, async=True)
        >>> result = thread.get()

        :param async bool
        :param str developer_certificate_id: A unique identifier for the developer certificate.  (required)
        :param str authorization: Bearer {Access Token}.  (required)
        :return: DeveloperCertificateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['developer_certificate_id', 'authorization']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_developer_certificate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'developer_certificate_id' is set
        if ('developer_certificate_id' not in params) or (params['developer_certificate_id'] is None):
            raise ValueError("Missing the required parameter `developer_certificate_id` when calling `get_developer_certificate`")
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_developer_certificate`")


        collection_formats = {}

        path_params = {}
        if 'developer_certificate_id' in params:
            path_params['developerCertificateId'] = params['developer_certificate_id']

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api('/v3/developer-certificates/{developerCertificateId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeveloperCertificateResponseData',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
