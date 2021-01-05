# skyportal_client.GroupAdmissionRequestsApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_group_admission_requests_admission_request_id_delete**](GroupAdmissionRequestsApi.md#api_group_admission_requests_admission_request_id_delete) | **DELETE** /api/group_admission_requests/admission_request_id | 
[**api_group_admission_requests_admission_request_id_get**](GroupAdmissionRequestsApi.md#api_group_admission_requests_admission_request_id_get) | **GET** /api/group_admission_requests/admission_request_id | 
[**api_group_admission_requests_admission_request_id_patch**](GroupAdmissionRequestsApi.md#api_group_admission_requests_admission_request_id_patch) | **PATCH** /api/group_admission_requests/admission_request_id | 
[**api_group_admission_requests_get**](GroupAdmissionRequestsApi.md#api_group_admission_requests_get) | **GET** /api/group_admission_requests | 
[**api_group_admission_requests_post**](GroupAdmissionRequestsApi.md#api_group_admission_requests_post) | **POST** /api/group_admission_requests | 


# **api_group_admission_requests_admission_request_id_delete**
> Success api_group_admission_requests_admission_request_id_delete(admission_request_id)



Delete a group admission request

### Example

```python
import time
import skyportal_client
from skyportal_client.api import group_admission_requests_api
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
    api_instance = group_admission_requests_api.GroupAdmissionRequestsApi(api_client)
    admission_request_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_group_admission_requests_admission_request_id_delete(admission_request_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupAdmissionRequestsApi->api_group_admission_requests_admission_request_id_delete: %s\n" % e)
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
from skyportal_client.api import group_admission_requests_api
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
    api_instance = group_admission_requests_api.GroupAdmissionRequestsApi(api_client)
    admission_request_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_group_admission_requests_admission_request_id_get(admission_request_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupAdmissionRequestsApi->api_group_admission_requests_admission_request_id_get: %s\n" % e)
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
from skyportal_client.api import group_admission_requests_api
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
    api_instance = group_admission_requests_api.GroupAdmissionRequestsApi(api_client)
    admission_request_id = 1 # int | 
    inline_object7 = InlineObject7(
        status="status_example",
    ) # InlineObject7 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_group_admission_requests_admission_request_id_patch(admission_request_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupAdmissionRequestsApi->api_group_admission_requests_admission_request_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_group_admission_requests_admission_request_id_patch(admission_request_id, inline_object7=inline_object7)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupAdmissionRequestsApi->api_group_admission_requests_admission_request_id_patch: %s\n" % e)
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
from skyportal_client.api import group_admission_requests_api
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
    api_instance = group_admission_requests_api.GroupAdmissionRequestsApi(api_client)
    group_id = 1 # int | ID of group for which admission requests are desired (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_group_admission_requests_get(group_id=group_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling GroupAdmissionRequestsApi->api_group_admission_requests_get: %s\n" % e)
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
from skyportal_client.api import group_admission_requests_api
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
    api_instance = group_admission_requests_api.GroupAdmissionRequestsApi(api_client)
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
        print("Exception when calling GroupAdmissionRequestsApi->api_group_admission_requests_post: %s\n" % e)
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

