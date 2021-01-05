"""
    Fritz: SkyPortal API

    SkyPortal provides an API to access most of its underlying functionality. To use it, you will need an API token. This can be generated via the web application from your profile page or, if you are an admin, you may use the system provisioned token stored inside of `.tokens.yaml`.  ### Accessing the SkyPortal API  Once you have a token, you may access SkyPortal programmatically as follows.  #### Python  ```python import requests  token = 'ea70a5f0-b321-43c6-96a1-b2de225e0339'  def api(method, endpoint, data=None):     headers = {'Authorization': f'token {token}'}     response = requests.request(method, endpoint, json=data, headers=headers)     return response  response = api('GET', 'http://localhost:5000/api/sysinfo')  print(f'HTTP code: {response.status_code}, {response.reason}') if response.status_code in (200, 400):     print(f'JSON response: {response.json()}') ```  #### Command line (curl)  ```shell curl -s -H 'Authorization: token ea70a5f0-b321-43c6-96a1-b2de225e0339' http://localhost:5000/api/sysinfo ```  ### Response  In the above examples, the SkyPortal server is located at `http://localhost:5000`. In case of success, the HTTP response is 200:  ``` HTTP code: 200, OK JSON response: {'status': 'success', 'data': {}, 'version': '0.9.dev0+git20200819.84c453a'} ```  On failure, it is 400; the JSON response has `status=\"error\"` with the reason for the failure given in `message`:  ```js {   \"status\": \"error\",   \"message\": \"Invalid API endpoint\",   \"data\": {},   \"version\": \"0.9.1\" } ```  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 0.9.dev0+git20201221.76627dd
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.inline_object20 import InlineObject20
from openapi_client.model.success import Success


class AclsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __api_user_user_id_acls_acl_id_delete(
            self,
            user_id,
            acl_id,
            **kwargs
        ):
            """api_user_user_id_acls_acl_id_delete  # noqa: E501

            Remove ACL from user permissions  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_user_user_id_acls_acl_id_delete(user_id, acl_id, async_req=True)
            >>> result = thread.get()

            Args:
                user_id (int):
                acl_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Success
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['user_id'] = \
                user_id
            kwargs['acl_id'] = \
                acl_id
            return self.call_with_http_info(**kwargs)

        self.api_user_user_id_acls_acl_id_delete = Endpoint(
            settings={
                'response_type': (Success,),
                'auth': [],
                'endpoint_path': '/api/user/user_id/acls/acl_id',
                'operation_id': 'api_user_user_id_acls_acl_id_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'acl_id',
                ],
                'required': [
                    'user_id',
                    'acl_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_id':
                        (int,),
                    'acl_id':
                        (str,),
                },
                'attribute_map': {
                    'user_id': 'user_id',
                    'acl_id': 'acl_id',
                },
                'location_map': {
                    'user_id': 'path',
                    'acl_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__api_user_user_id_acls_acl_id_delete
        )

        def __api_user_user_id_acls_ignored_args_post(
            self,
            user_id,
            **kwargs
        ):
            """api_user_user_id_acls_ignored_args_post  # noqa: E501

            Grant new ACL(s) to a user  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_user_user_id_acls_ignored_args_post(user_id, async_req=True)
            >>> result = thread.get()

            Args:
                user_id (int):

            Keyword Args:
                inline_object20 (InlineObject20): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Success
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['user_id'] = \
                user_id
            return self.call_with_http_info(**kwargs)

        self.api_user_user_id_acls_ignored_args_post = Endpoint(
            settings={
                'response_type': (Success,),
                'auth': [],
                'endpoint_path': '/api/user/user_id/acls/ignored_args',
                'operation_id': 'api_user_user_id_acls_ignored_args_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'inline_object20',
                ],
                'required': [
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_id':
                        (int,),
                    'inline_object20':
                        (InlineObject20,),
                },
                'attribute_map': {
                    'user_id': 'user_id',
                },
                'location_map': {
                    'user_id': 'path',
                    'inline_object20': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__api_user_user_id_acls_ignored_args_post
        )
