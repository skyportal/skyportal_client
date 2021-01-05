# skyportal_client.GroupsApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_group_admission_requests_admission_request_id_delete**](GroupsApi.md#api_group_admission_requests_admission_request_id_delete) | **DELETE** /api/group_admission_requests/admission_request_id | 
[**api_group_admission_requests_admission_request_id_get**](GroupsApi.md#api_group_admission_requests_admission_request_id_get) | **GET** /api/group_admission_requests/admission_request_id | 
[**api_group_admission_requests_admission_request_id_patch**](GroupsApi.md#api_group_admission_requests_admission_request_id_patch) | **PATCH** /api/group_admission_requests/admission_request_id | 
[**api_group_admission_requests_get**](GroupsApi.md#api_group_admission_requests_get) | **GET** /api/group_admission_requests | 
[**api_group_admission_requests_post**](GroupsApi.md#api_group_admission_requests_post) | **POST** /api/group_admission_requests | 
[**api_groups_get**](GroupsApi.md#api_groups_get) | **GET** /api/groups | 
[**api_groups_group_id_delete**](GroupsApi.md#api_groups_group_id_delete) | **DELETE** /api/groups/group_id | 
[**api_groups_group_id_get**](GroupsApi.md#api_groups_group_id_get) | **GET** /api/groups/group_id | 
[**api_groups_group_id_put**](GroupsApi.md#api_groups_group_id_put) | **PUT** /api/groups/group_id | 
[**api_groups_group_id_streams_ignored_args_post**](GroupsApi.md#api_groups_group_id_streams_ignored_args_post) | **POST** /api/groups/group_id/streams/ignored_args | 
[**api_groups_group_id_streams_stream_id_delete**](GroupsApi.md#api_groups_group_id_streams_stream_id_delete) | **DELETE** /api/groups/group_id/streams/stream_id | 
[**api_groups_group_id_users_from_groups_ignored_args_post**](GroupsApi.md#api_groups_group_id_users_from_groups_ignored_args_post) | **POST** /api/groups/group_id/usersFromGroups/ignored_args | 
[**api_groups_group_id_users_ignored_args_patch**](GroupsApi.md#api_groups_group_id_users_ignored_args_patch) | **PATCH** /api/groups/group_id/users/ignored_args | 
[**api_groups_group_id_users_ignored_args_post**](GroupsApi.md#api_groups_group_id_users_ignored_args_post) | **POST** /api/groups/group_id/users/ignored_args | 
[**api_groups_group_id_users_user_id_delete**](GroupsApi.md#api_groups_group_id_users_user_id_delete) | **DELETE** /api/groups/group_id/users/user_id | 
[**api_groups_post**](GroupsApi.md#api_groups_post) | **POST** /api/groups | 
[**api_groups_public_get**](GroupsApi.md#api_groups_public_get) | **GET** /api/groups/public | 
[**api_source_groups_obj_id_patch**](GroupsApi.md#api_source_groups_obj_id_patch) | **PATCH** /api/source_groups/obj_id | 
[**api_source_groups_post**](GroupsApi.md#api_source_groups_post) | **POST** /api/source_groups | 
[**api_sources_obj_id_groups_get**](GroupsApi.md#api_sources_obj_id_groups_get) | **GET** /api/sources/obj_id/groups | 


# **api_group_admission_requests_admission_request_id_delete**
> Success api_group_admission_requests_admission_request_id_delete(admission_request_id)



Delete a group admission request

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    admission_request_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_group_admission_requests_admission_request_id_delete(admission_request_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_group_admission_requests_admission_request_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admission_request_id** | **int**|  |

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

# **api_group_admission_requests_admission_request_id_get**
> SingleGroupAdmissionRequest api_group_admission_requests_admission_request_id_get(admission_request_id)



Retrieve a group admission request

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
from skyportal_client.model.error import Error
from skyportal_client.model.single_group_admission_request import SingleGroupAdmissionRequest
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    admission_request_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_group_admission_requests_admission_request_id_get(admission_request_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_group_admission_requests_admission_request_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admission_request_id** | **int**|  |

### Return type

[**SingleGroupAdmissionRequest**](SingleGroupAdmissionRequest.md)

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

# **api_group_admission_requests_admission_request_id_patch**
> Success api_group_admission_requests_admission_request_id_patch(admission_request_id)



Update a group admission request's status

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
from skyportal_client.model.inline_object7 import InlineObject7
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
    api_instance = groups_api.GroupsApi(api_client)
    admission_request_id = 1 # int | 
    inline_object7 = InlineObject7(
        status="status_example",
    ) # InlineObject7 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_group_admission_requests_admission_request_id_patch(admission_request_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_group_admission_requests_admission_request_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_group_admission_requests_admission_request_id_patch(admission_request_id, inline_object7=inline_object7)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_group_admission_requests_admission_request_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admission_request_id** | **int**|  |
 **inline_object7** | [**InlineObject7**](InlineObject7.md)|  | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_group_admission_requests_get**
> ArrayOfGroupAdmissionRequests api_group_admission_requests_get()



Retrieve all group admission requests

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
from skyportal_client.model.error import Error
from skyportal_client.model.array_of_group_admission_requests import ArrayOfGroupAdmissionRequests
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    group_id = 1 # int | ID of group for which admission requests are desired (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_group_admission_requests_get(group_id=group_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_group_admission_requests_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of group for which admission requests are desired | [optional]

### Return type

[**ArrayOfGroupAdmissionRequests**](ArrayOfGroupAdmissionRequests.md)

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

# **api_group_admission_requests_post**
> object api_group_admission_requests_post()



Create a new group admission request

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
from skyportal_client.model.inline_object8 import InlineObject8
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    inline_object8 = InlineObject8(
        group_id=1,
        user_id=1,
    ) # InlineObject8 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_group_admission_requests_post(inline_object8=inline_object8)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_group_admission_requests_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object8** | [**InlineObject8**](InlineObject8.md)|  | [optional]

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

# **api_groups_get**
> object api_groups_get()



Retrieve all groups

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
from skyportal_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    name = "name_example" # str | Fetch by name (exact match) (optional)
    include_single_user_groups = True # bool | Bool indicating whether to include single user groups. Defaults to false.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_groups_get(name=name, include_single_user_groups=include_single_user_groups)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Fetch by name (exact match) | [optional]
 **include_single_user_groups** | **bool**| Bool indicating whether to include single user groups. Defaults to false.  | [optional]

### Return type

**object**

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

# **api_groups_group_id_delete**
> Success api_groups_group_id_delete(group_id)



Delete a group

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_groups_group_id_delete(group_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_group_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  |

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

# **api_groups_group_id_get**
> object api_groups_group_id_get(group_id)



Retrieve a group

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
from skyportal_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    group_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_groups_group_id_get(group_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  |

### Return type

**object**

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

# **api_groups_group_id_put**
> Success api_groups_group_id_put(group_id)



Update a group

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
from skyportal_client.model.error import Error
from skyportal_client.model.group_no_id import GroupNoID
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = 1 # int | 
    group_no_id = GroupNoID(
        name="name_example",
        nickname="nickname_example",
        private=True,
        single_user_group=True,
    ) # GroupNoID |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_groups_group_id_put(group_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_group_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_groups_group_id_put(group_id, group_no_id=group_no_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_group_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  |
 **group_no_id** | [**GroupNoID**](GroupNoID.md)|  | [optional]

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

# **api_groups_group_id_streams_ignored_args_post**
> object api_groups_group_id_streams_ignored_args_post(group_id)



Add alert stream access to group

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = 1 # int | 
    inline_object3 = InlineObject3(
        stream_id=1,
    ) # InlineObject3 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_groups_group_id_streams_ignored_args_post(group_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_group_id_streams_ignored_args_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_groups_group_id_streams_ignored_args_post(group_id, inline_object3=inline_object3)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_group_id_streams_ignored_args_post: %s\n" % e)
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
from skyportal_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = 1 # int | 
    stream_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_groups_group_id_streams_stream_id_delete(group_id, stream_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_group_id_streams_stream_id_delete: %s\n" % e)
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

# **api_groups_group_id_users_from_groups_ignored_args_post**
> Success api_groups_group_id_users_from_groups_ignored_args_post(group_id)



Add users from other group(s) to specified group

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
from skyportal_client.model.inline_object6 import InlineObject6
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = 1 # int | 
    inline_object6 = InlineObject6(
        from_group_i_ds=[
            1,
        ],
    ) # InlineObject6 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_groups_group_id_users_from_groups_ignored_args_post(group_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_group_id_users_from_groups_ignored_args_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_groups_group_id_users_from_groups_ignored_args_post(group_id, inline_object6=inline_object6)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_group_id_users_from_groups_ignored_args_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  |
 **inline_object6** | [**InlineObject6**](InlineObject6.md)|  | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_groups_group_id_users_ignored_args_patch**
> Success api_groups_group_id_users_ignored_args_patch(group_id)



Update a group user's admin status

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
from skyportal_client.model.inline_object5 import InlineObject5
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = 1 # int | 
    inline_object5 = InlineObject5(
        user_id=1,
        admin=True,
    ) # InlineObject5 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_groups_group_id_users_ignored_args_patch(group_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_group_id_users_ignored_args_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_groups_group_id_users_ignored_args_patch(group_id, inline_object5=inline_object5)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_group_id_users_ignored_args_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  |
 **inline_object5** | [**InlineObject5**](InlineObject5.md)|  | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_groups_group_id_users_ignored_args_post**
> object api_groups_group_id_users_ignored_args_post(group_id)



Add a group user

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
from skyportal_client.model.inline_object4 import InlineObject4
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    group_id = 1 # int | 
    inline_object4 = InlineObject4(
        user_id=1,
        admin=True,
    ) # InlineObject4 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_groups_group_id_users_ignored_args_post(group_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_group_id_users_ignored_args_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_groups_group_id_users_ignored_args_post(group_id, inline_object4=inline_object4)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_group_id_users_ignored_args_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  |
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  | [optional]

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

# **api_groups_group_id_users_user_id_delete**
> Success api_groups_group_id_users_user_id_delete(group_id, user_id)



Delete a group user

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = 1 # int | 
    user_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_groups_group_id_users_user_id_delete(group_id, user_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_group_id_users_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  |
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

# **api_groups_post**
> object api_groups_post()



Create a new group

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
from skyportal_client.model.unknownbasetype import UNKNOWNBASETYPE
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    unknown_base_type =  # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_groups_post(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

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

# **api_groups_public_get**
> SingleGroup api_groups_public_get()



Retrieve the public group

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
from skyportal_client.model.single_group import SingleGroup
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_groups_public_get()
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_groups_public_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SingleGroup**](SingleGroup.md)

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

# **api_source_groups_obj_id_patch**
> Success api_source_groups_obj_id_patch(obj_id)



Update a Source table row

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
from skyportal_client.model.inline_object14 import InlineObject14
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
    api_instance = groups_api.GroupsApi(api_client)
    obj_id = 1 # int | 
    inline_object14 = InlineObject14(
        group_id=1,
        active=True,
        requested=True,
    ) # InlineObject14 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_source_groups_obj_id_patch(obj_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_source_groups_obj_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_source_groups_obj_id_patch(obj_id, inline_object14=inline_object14)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_source_groups_obj_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obj_id** | **int**|  |
 **inline_object14** | [**InlineObject14**](InlineObject14.md)|  | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_source_groups_post**
> Success api_source_groups_post()



Save or request group(s) to save source, and optionally unsave from group(s).

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
from skyportal_client.model.inline_object13 import InlineObject13
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
    api_instance = groups_api.GroupsApi(api_client)
    inline_object13 = InlineObject13(
        obj_id="obj_id_example",
        invite_group_ids=[
            1,
        ],
        unsave_group_ids=[
            1,
        ],
    ) # InlineObject13 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_source_groups_post(inline_object13=inline_object13)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_source_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object13** | [**InlineObject13**](InlineObject13.md)|  | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sources_obj_id_groups_get**
> ArrayOfGroups api_sources_obj_id_groups_get(obj_id)



Retrieve basic info on Groups that an Obj is saved to

### Example

```python
import time
import skyportal_client
from skyportal_client.api import groups_api
from skyportal_client.model.array_of_groups import ArrayOfGroups
from skyportal_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    obj_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_sources_obj_id_groups_get(obj_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupsApi->api_sources_obj_id_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obj_id** | **int**|  |

### Return type

[**ArrayOfGroups**](ArrayOfGroups.md)

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

