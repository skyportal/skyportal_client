# skyportal_client.StreamsApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_groups_group_id_streams_ignored_args_post**](StreamsApi.md#api_groups_group_id_streams_ignored_args_post) | **POST** /api/groups/group_id/streams/ignored_args | 
[**api_groups_group_id_streams_stream_id_delete**](StreamsApi.md#api_groups_group_id_streams_stream_id_delete) | **DELETE** /api/groups/group_id/streams/stream_id | 
[**api_streams_get**](StreamsApi.md#api_streams_get) | **GET** /api/streams | 
[**api_streams_post**](StreamsApi.md#api_streams_post) | **POST** /api/streams | 
[**api_streams_stream_id_delete**](StreamsApi.md#api_streams_stream_id_delete) | **DELETE** /api/streams/stream_id | 
[**api_streams_stream_id_get**](StreamsApi.md#api_streams_stream_id_get) | **GET** /api/streams/stream_id | 
[**api_streams_stream_id_patch**](StreamsApi.md#api_streams_stream_id_patch) | **PATCH** /api/streams/stream_id | 
[**api_streams_stream_id_users_ignored_args_post**](StreamsApi.md#api_streams_stream_id_users_ignored_args_post) | **POST** /api/streams/stream_id/users/ignored_args | 
[**api_streams_stream_id_users_user_id_delete**](StreamsApi.md#api_streams_stream_id_users_user_id_delete) | **DELETE** /api/streams/stream_id/users/user_id | 


# **api_groups_group_id_streams_ignored_args_post**
> object api_groups_group_id_streams_ignored_args_post(group_id)



Add alert stream access to group

### Example

```python
import time
import skyportal_client
from skyportal_client.api import streams_api
from skyportal_client.model.inline_object3 import InlineObject3
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = streams_api.StreamsApi(api_client)
    group_id = 1 # int | 
    inline_object3 = InlineObject3(
        stream_id=1,
    ) # InlineObject3 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_groups_group_id_streams_ignored_args_post(group_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling StreamsApi->api_groups_group_id_streams_ignored_args_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_groups_group_id_streams_ignored_args_post(group_id, inline_object3=inline_object3)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling StreamsApi->api_groups_group_id_streams_ignored_args_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  |
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | [optional]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_groups_group_id_streams_stream_id_delete**
> Success api_groups_group_id_streams_stream_id_delete(group_id, stream_id)



Delete an alert stream from group

### Example

```python
import time
import skyportal_client
from skyportal_client.api import streams_api
from skyportal_client.model.success import Success
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = streams_api.StreamsApi(api_client)
    group_id = 1 # int | 
    stream_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_groups_group_id_streams_stream_id_delete(group_id, stream_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling StreamsApi->api_groups_group_id_streams_stream_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  |
 **stream_id** | **int**|  |

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_streams_get**
> ArrayOfStreams api_streams_get()



Retrieve all streams

### Example

```python
import time
import skyportal_client
from skyportal_client.api import streams_api
from skyportal_client.model.error import Error
from skyportal_client.model.array_of_streams import ArrayOfStreams
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = streams_api.StreamsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_streams_get()
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling StreamsApi->api_streams_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArrayOfStreams**](ArrayOfStreams.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_streams_post**
> object api_streams_post()



POST a new stream.

### Example

```python
import time
import skyportal_client
from skyportal_client.api import streams_api
from skyportal_client.model.inline_object17 import InlineObject17
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = streams_api.StreamsApi(api_client)
    inline_object17 = InlineObject17(
        name="name_example",
        altdata={},
    ) # InlineObject17 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_streams_post(inline_object17=inline_object17)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling StreamsApi->api_streams_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object17** | [**InlineObject17**](InlineObject17.md)|  | [optional]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_streams_stream_id_delete**
> Success api_streams_stream_id_delete(stream_id)



Delete a stream

### Example

```python
import time
import skyportal_client
from skyportal_client.api import streams_api
from skyportal_client.model.success import Success
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = streams_api.StreamsApi(api_client)
    stream_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_streams_stream_id_delete(stream_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling StreamsApi->api_streams_stream_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**|  |

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_streams_stream_id_get**
> SingleStream api_streams_stream_id_get(filter_id)



Retrieve a stream

### Example

```python
import time
import skyportal_client
from skyportal_client.api import streams_api
from skyportal_client.model.error import Error
from skyportal_client.model.single_stream import SingleStream
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = streams_api.StreamsApi(api_client)
    filter_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_streams_stream_id_get(filter_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling StreamsApi->api_streams_stream_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **int**|  |

### Return type

[**SingleStream**](SingleStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_streams_stream_id_patch**
> Success api_streams_stream_id_patch(stream_id)



Update a stream

### Example

```python
import time
import skyportal_client
from skyportal_client.api import streams_api
from skyportal_client.model.error import Error
from skyportal_client.model.inline_object16 import InlineObject16
from skyportal_client.model.success import Success
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = streams_api.StreamsApi(api_client)
    stream_id = 1 # int | 
    inline_object16 = InlineObject16(
        name="name_example",
        altdata={},
    ) # InlineObject16 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_streams_stream_id_patch(stream_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling StreamsApi->api_streams_stream_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_streams_stream_id_patch(stream_id, inline_object16=inline_object16)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling StreamsApi->api_streams_stream_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**|  |
 **inline_object16** | [**InlineObject16**](InlineObject16.md)|  | [optional]

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_streams_stream_id_users_ignored_args_post**
> object api_streams_stream_id_users_ignored_args_post(stream_id)



Grant stream access to a user

### Example

```python
import time
import skyportal_client
from skyportal_client.api import streams_api
from skyportal_client.model.inline_object15 import InlineObject15
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = streams_api.StreamsApi(api_client)
    stream_id = 1 # int | 
    inline_object15 = InlineObject15(
        user_id=1,
    ) # InlineObject15 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_streams_stream_id_users_ignored_args_post(stream_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling StreamsApi->api_streams_stream_id_users_ignored_args_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_streams_stream_id_users_ignored_args_post(stream_id, inline_object15=inline_object15)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling StreamsApi->api_streams_stream_id_users_ignored_args_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**|  |
 **inline_object15** | [**InlineObject15**](InlineObject15.md)|  | [optional]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_streams_stream_id_users_user_id_delete**
> Success api_streams_stream_id_users_user_id_delete(stream_id, user_id)



Delete a stream user (revoke stream access for user)

### Example

```python
import time
import skyportal_client
from skyportal_client.api import streams_api
from skyportal_client.model.success import Success
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = streams_api.StreamsApi(api_client)
    stream_id = 1 # int | 
    user_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_streams_stream_id_users_user_id_delete(stream_id, user_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling StreamsApi->api_streams_stream_id_users_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**|  |
 **user_id** | **int**|  |

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

