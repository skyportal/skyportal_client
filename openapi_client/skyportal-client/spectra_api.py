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
from openapi_client.model.error import Error
from openapi_client.model.isoutc_date_string import ISOUTCDateString
from openapi_client.model.list_of_integers import ListOfIntegers
from openapi_client.model.single_spectrum import SingleSpectrum
from openapi_client.model.spectrum_ascii_file_parse_json import SpectrumAsciiFileParseJSON
from openapi_client.model.spectrum_ascii_file_post_json import SpectrumAsciiFilePostJSON
from openapi_client.model.spectrum_no_id import SpectrumNoID
from openapi_client.model.spectrum_post import SpectrumPost
from openapi_client.model.success import Success


class SpectraApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __api_sources_obj_id_spectra_get(
            self,
            obj_id,
            **kwargs
        ):
            """api_sources_obj_id_spectra_get  # noqa: E501

            Retrieve all spectra associated with an Object  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_sources_obj_id_spectra_get(obj_id, async_req=True)
            >>> result = thread.get()

            Args:
                obj_id (str): ID of the object to retrieve spectra for

            Keyword Args:
                normalization (str): what normalization is needed for the spectra (e.g., \"median\"). If omitted, returns the original spectrum. Options for normalization are: - median: normalize the flux to have median==1 . [optional]
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
            kwargs['obj_id'] = \
                obj_id
            return self.call_with_http_info(**kwargs)

        self.api_sources_obj_id_spectra_get = Endpoint(
            settings={
                'response_type': (object,),
                'auth': [],
                'endpoint_path': '/api/sources/obj_id/spectra',
                'operation_id': 'api_sources_obj_id_spectra_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'obj_id',
                    'normalization',
                ],
                'required': [
                    'obj_id',
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
                    'obj_id':
                        (str,),
                    'normalization':
                        (str,),
                },
                'attribute_map': {
                    'obj_id': 'obj_id',
                    'normalization': 'normalization',
                },
                'location_map': {
                    'obj_id': 'path',
                    'normalization': 'query',
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
            callable=__api_sources_obj_id_spectra_get
        )

        def __api_spectrum_ascii_post(
            self,
            **kwargs
        ):
            """api_spectrum_ascii_post  # noqa: E501

            Upload spectrum from ASCII file  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_spectrum_ascii_post(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                spectrum_ascii_file_post_json (SpectrumAsciiFilePostJSON): [optional]
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

        self.api_spectrum_ascii_post = Endpoint(
            settings={
                'response_type': (object,),
                'auth': [],
                'endpoint_path': '/api/spectrum/ascii',
                'operation_id': 'api_spectrum_ascii_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'spectrum_ascii_file_post_json',
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
                    'spectrum_ascii_file_post_json':
                        (SpectrumAsciiFilePostJSON,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'spectrum_ascii_file_post_json': 'body',
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
            callable=__api_spectrum_ascii_post
        )

        def __api_spectrum_parse_ascii_post(
            self,
            **kwargs
        ):
            """api_spectrum_parse_ascii_post  # noqa: E501

            Parse spectrum from ASCII file  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_spectrum_parse_ascii_post(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                spectrum_ascii_file_parse_json (SpectrumAsciiFileParseJSON): [optional]
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
                SpectrumNoID
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

        self.api_spectrum_parse_ascii_post = Endpoint(
            settings={
                'response_type': (SpectrumNoID,),
                'auth': [],
                'endpoint_path': '/api/spectrum/parse/ascii',
                'operation_id': 'api_spectrum_parse_ascii_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'spectrum_ascii_file_parse_json',
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
                    'spectrum_ascii_file_parse_json':
                        (SpectrumAsciiFileParseJSON,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'spectrum_ascii_file_parse_json': 'body',
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
            callable=__api_spectrum_parse_ascii_post
        )

        def __api_spectrum_post(
            self,
            **kwargs
        ):
            """api_spectrum_post  # noqa: E501

            Upload spectrum  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_spectrum_post(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                spectrum_post (SpectrumPost): [optional]
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

        self.api_spectrum_post = Endpoint(
            settings={
                'response_type': (object,),
                'auth': [],
                'endpoint_path': '/api/spectrum',
                'operation_id': 'api_spectrum_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'spectrum_post',
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
                    'spectrum_post':
                        (SpectrumPost,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'spectrum_post': 'body',
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
            callable=__api_spectrum_post
        )

        def __api_spectrum_range_get(
            self,
            **kwargs
        ):
            """api_spectrum_range_get  # noqa: E501

            Retrieve spectra for given instrument within date range  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_spectrum_range_get(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                instrument_ids (ListOfIntegers): Instrument id numbers of spectrum.  If None, retrieve for all instruments. . [optional]
                min_date (ISOUTCDateString): Minimum UTC date of range in ISOT format.  If None, open ended range. . [optional]
                max_date (ISOUTCDateString): Maximum UTC date of range in ISOT format. If None, open ended range. . [optional]
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

        self.api_spectrum_range_get = Endpoint(
            settings={
                'response_type': (object,),
                'auth': [],
                'endpoint_path': '/api/spectrum/range',
                'operation_id': 'api_spectrum_range_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'instrument_ids',
                    'min_date',
                    'max_date',
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
                    'instrument_ids':
                        (ListOfIntegers,),
                    'min_date':
                        (ISOUTCDateString,),
                    'max_date':
                        (ISOUTCDateString,),
                },
                'attribute_map': {
                    'instrument_ids': 'instrument_ids',
                    'min_date': 'min_date',
                    'max_date': 'max_date',
                },
                'location_map': {
                    'instrument_ids': 'query',
                    'min_date': 'query',
                    'max_date': 'query',
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
            callable=__api_spectrum_range_get
        )

        def __api_spectrum_spectrum_id_delete(
            self,
            spectrum_id,
            **kwargs
        ):
            """api_spectrum_spectrum_id_delete  # noqa: E501

            Delete a spectrum  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_spectrum_spectrum_id_delete(spectrum_id, async_req=True)
            >>> result = thread.get()

            Args:
                spectrum_id (int):

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
            kwargs['spectrum_id'] = \
                spectrum_id
            return self.call_with_http_info(**kwargs)

        self.api_spectrum_spectrum_id_delete = Endpoint(
            settings={
                'response_type': (Success,),
                'auth': [],
                'endpoint_path': '/api/spectrum/spectrum_id',
                'operation_id': 'api_spectrum_spectrum_id_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'spectrum_id',
                ],
                'required': [
                    'spectrum_id',
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
                    'spectrum_id':
                        (int,),
                },
                'attribute_map': {
                    'spectrum_id': 'spectrum_id',
                },
                'location_map': {
                    'spectrum_id': 'path',
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
            callable=__api_spectrum_spectrum_id_delete
        )

        def __api_spectrum_spectrum_id_get(
            self,
            spectrum_id,
            **kwargs
        ):
            """api_spectrum_spectrum_id_get  # noqa: E501

            Retrieve a spectrum  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_spectrum_spectrum_id_get(spectrum_id, async_req=True)
            >>> result = thread.get()

            Args:
                spectrum_id (int):

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
                SingleSpectrum
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
            kwargs['spectrum_id'] = \
                spectrum_id
            return self.call_with_http_info(**kwargs)

        self.api_spectrum_spectrum_id_get = Endpoint(
            settings={
                'response_type': (SingleSpectrum,),
                'auth': [],
                'endpoint_path': '/api/spectrum/spectrum_id',
                'operation_id': 'api_spectrum_spectrum_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'spectrum_id',
                ],
                'required': [
                    'spectrum_id',
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
                    'spectrum_id':
                        (int,),
                },
                'attribute_map': {
                    'spectrum_id': 'spectrum_id',
                },
                'location_map': {
                    'spectrum_id': 'path',
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
            callable=__api_spectrum_spectrum_id_get
        )

        def __api_spectrum_spectrum_id_put(
            self,
            spectrum_id,
            **kwargs
        ):
            """api_spectrum_spectrum_id_put  # noqa: E501

            Update spectrum  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_spectrum_spectrum_id_put(spectrum_id, async_req=True)
            >>> result = thread.get()

            Args:
                spectrum_id (int):

            Keyword Args:
                spectrum_post (SpectrumPost): [optional]
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
            kwargs['spectrum_id'] = \
                spectrum_id
            return self.call_with_http_info(**kwargs)

        self.api_spectrum_spectrum_id_put = Endpoint(
            settings={
                'response_type': (Success,),
                'auth': [],
                'endpoint_path': '/api/spectrum/spectrum_id',
                'operation_id': 'api_spectrum_spectrum_id_put',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'spectrum_id',
                    'spectrum_post',
                ],
                'required': [
                    'spectrum_id',
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
                    'spectrum_id':
                        (int,),
                    'spectrum_post':
                        (SpectrumPost,),
                },
                'attribute_map': {
                    'spectrum_id': 'spectrum_id',
                },
                'location_map': {
                    'spectrum_id': 'path',
                    'spectrum_post': 'body',
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
            callable=__api_spectrum_spectrum_id_put
        )
