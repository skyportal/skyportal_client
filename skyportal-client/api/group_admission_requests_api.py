"""
    Fritz: SkyPortal API

    SkyPortal provides an API to access most of its underlying functionality. To use it, you will need an API token. This can be generated via the web application from your profile page or, if you are an admin, you may use the system provisioned token stored inside of `.tokens.yaml`.  ### Accessing the SkyPortal API  Once you have a token, you may access SkyPortal programmatically as follows.  #### Python  ```python import requests  token = 'ea70a5f0-b321-43c6-96a1-b2de225e0339'  def api(method, endpoint, data=None):     headers = {'Authorization': f'token {token}'}     response = requests.request(method, endpoint, json=data, headers=headers)     return response  response = api('GET', 'http://localhost:5000/api/sysinfo')  print(f'HTTP code: {response.status_code}, {response.reason}') if response.status_code in (200, 400):     print(f'JSON response: {response.json()}') ```  #### Command line (curl)  ```shell curl -s -H 'Authorization: token ea70a5f0-b321-43c6-96a1-b2de225e0339' http://localhost:5000/api/sysinfo ```  ### Response  In the above examples, the SkyPortal server is located at `http://localhost:5000`. In case of success, the HTTP response is 200:  ``` HTTP code: 200, OK JSON response: {'status': 'success', 'data': {}, 'version': '0.9.dev0+git20200819.84c453a'} ```  On failure, it is 400; the JSON response has `status=\"error\"` with the reason for the failure given in `message`:  ```js {   \"status\": \"error\",   \"message\": \"Invalid API endpoint\",   \"data\": {},   \"version\": \"0.9.1\" } ```  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 0.9.dev0+git20201221.76627dd
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from skyportal-client.api_client import ApiClient, Endpoint
from skyportal-client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from skyportal-client.model.array_of_group_admission_requests import ArrayOfGroupAdmissionRequests
from skyportal-client.model.error import Error
from skyportal-client.model.inline_object7 import InlineObject7
from skyportal-client.model.inline_object8 import InlineObject8
from skyportal-client.model.single_group_admission_request import SingleGroupAdmissionRequest
from skyportal-client.model.success import Success


class GroupAdmissionRequestsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __api_group_admission_requests_admission_request_id_delete(
            self,
            admission_request_id,
            **kwargs
        ):
            """api_group_admission_requests_admission_request_id_delete  # noqa: E501

            Delete a group admission request  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_group_admission_requests_admission_request_id_delete(admission_request_id, async_req=True)
            >>> result = thread.get()

            Args:
                admission_request_id (int):

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
            kwargs['admission_request_id'] = \
                admission_request_id
            return self.call_with_http_info(**kwargs)

        self.api_group_admission_requests_admission_request_id_delete = Endpoint(
            settings={
                'response_type': (Success,),
                'auth': [],
                'endpoint_path': '/api/group_admission_requests/admission_request_id',
                'operation_id': 'api_group_admission_requests_admission_request_id_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'admission_request_id',
                ],
                'required': [
                    'admission_request_id',
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
                    'admission_request_id':
                        (int,),
                },
                'attribute_map': {
                    'admission_request_id': 'admission_request_id',
                },
                'location_map': {
                    'admission_request_id': 'path',
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
            callable=__api_group_admission_requests_admission_request_id_delete
        )

        def __api_group_admission_requests_admission_request_id_get(
            self,
            admission_request_id,
            **kwargs
        ):
            """api_group_admission_requests_admission_request_id_get  # noqa: E501

            Retrieve a group admission request  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_group_admission_requests_admission_request_id_get(admission_request_id, async_req=True)
            >>> result = thread.get()

            Args:
                admission_request_id (int):

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
                SingleGroupAdmissionRequest
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
            kwargs['admission_request_id'] = \
                admission_request_id
            return self.call_with_http_info(**kwargs)

        self.api_group_admission_requests_admission_request_id_get = Endpoint(
            settings={
                'response_type': (SingleGroupAdmissionRequest,),
                'auth': [],
                'endpoint_path': '/api/group_admission_requests/admission_request_id',
                'operation_id': 'api_group_admission_requests_admission_request_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'admission_request_id',
                ],
                'required': [
                    'admission_request_id',
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
                    'admission_request_id':
                        (int,),
                },
                'attribute_map': {
                    'admission_request_id': 'admission_request_id',
                },
                'location_map': {
                    'admission_request_id': 'path',
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
            callable=__api_group_admission_requests_admission_request_id_get
        )

        def __api_group_admission_requests_admission_request_id_patch(
            self,
            admission_request_id,
            **kwargs
        ):
            """api_group_admission_requests_admission_request_id_patch  # noqa: E501

            Update a group admission request's status  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_group_admission_requests_admission_request_id_patch(admission_request_id, async_req=True)
            >>> result = thread.get()

            Args:
                admission_request_id (int):

            Keyword Args:
                inline_object7 (InlineObject7): [optional]
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
            kwargs['admission_request_id'] = \
                admission_request_id
            return self.call_with_http_info(**kwargs)

        self.api_group_admission_requests_admission_request_id_patch = Endpoint(
            settings={
                'response_type': (Success,),
                'auth': [],
                'endpoint_path': '/api/group_admission_requests/admission_request_id',
                'operation_id': 'api_group_admission_requests_admission_request_id_patch',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'admission_request_id',
                    'inline_object7',
                ],
                'required': [
                    'admission_request_id',
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
                    'admission_request_id':
                        (int,),
                    'inline_object7':
                        (InlineObject7,),
                },
                'attribute_map': {
                    'admission_request_id': 'admission_request_id',
                },
                'location_map': {
                    'admission_request_id': 'path',
                    'inline_object7': 'body',
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
            callable=__api_group_admission_requests_admission_request_id_patch
        )

        def __api_group_admission_requests_get(
            self,
            **kwargs
        ):
            """api_group_admission_requests_get  # noqa: E501

            Retrieve all group admission requests  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_group_admission_requests_get(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                group_id (int): ID of group for which admission requests are desired. [optional]
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
                ArrayOfGroupAdmissionRequests
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
            return self.call_with_http_info(**kwargs)

        self.api_group_admission_requests_get = Endpoint(
            settings={
                'response_type': (ArrayOfGroupAdmissionRequests,),
                'auth': [],
                'endpoint_path': '/api/group_admission_requests',
                'operation_id': 'api_group_admission_requests_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'group_id',
                ],
                'required': [],
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
                    'group_id':
                        (int,),
                },
                'attribute_map': {
                    'group_id': 'groupID',
                },
                'location_map': {
                    'group_id': 'query',
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
            callable=__api_group_admission_requests_get
        )

        def __api_group_admission_requests_post(
            self,
            **kwargs
        ):
            """api_group_admission_requests_post  # noqa: E501

            Create a new group admission request  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_group_admission_requests_post(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                inline_object8 (InlineObject8): [optional]
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
                object
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
            return self.call_with_http_info(**kwargs)

        self.api_group_admission_requests_post = Endpoint(
            settings={
                'response_type': (object,),
                'auth': [],
                'endpoint_path': '/api/group_admission_requests',
                'operation_id': 'api_group_admission_requests_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'inline_object8',
                ],
                'required': [],
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
                    'inline_object8':
                        (InlineObject8,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'inline_object8': 'body',
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
            callable=__api_group_admission_requests_post
        )
