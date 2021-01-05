# skyportal_client.FollowupRequestsApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_followup_request_followup_request_id_get**](FollowupRequestsApi.md#api_followup_request_followup_request_id_get) | **GET** /api/followup_request/followup_request_id | 
[**api_followup_request_get**](FollowupRequestsApi.md#api_followup_request_get) | **GET** /api/followup_request | 
[**api_followup_request_post**](FollowupRequestsApi.md#api_followup_request_post) | **POST** /api/followup_request | 
[**api_followup_request_request_id_delete**](FollowupRequestsApi.md#api_followup_request_request_id_delete) | **DELETE** /api/followup_request/request_id | 
[**api_followup_request_request_id_put**](FollowupRequestsApi.md#api_followup_request_request_id_put) | **PUT** /api/followup_request/request_id | 


# **api_followup_request_followup_request_id_get**
> SingleFollowupRequest api_followup_request_followup_request_id_get(followup_request_id)



Retrieve a followup request

### Example

```python
import time
import skyportal_client
from skyportal_client.api import followup_requests_api
from skyportal_client.model.error import Error
from skyportal_client.model.single_followup_request import SingleFollowupRequest
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = followup_requests_api.FollowupRequestsApi(api_client)
    followup_request_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_followup_request_followup_request_id_get(followup_request_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling FollowupRequestsApi->api_followup_request_followup_request_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **followup_request_id** | **int**|  |

### Return type

[**SingleFollowupRequest**](SingleFollowupRequest.md)

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

# **api_followup_request_get**
> ArrayOfFollowupRequests api_followup_request_get()



Retrieve all followup requests

### Example

```python
import time
import skyportal_client
from skyportal_client.api import followup_requests_api
from skyportal_client.model.array_of_followup_requests import ArrayOfFollowupRequests
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
    api_instance = followup_requests_api.FollowupRequestsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_followup_request_get()
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling FollowupRequestsApi->api_followup_request_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArrayOfFollowupRequests**](ArrayOfFollowupRequests.md)

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

# **api_followup_request_post**
> object api_followup_request_post()



Submit follow-up request.

### Example

```python
import time
import skyportal_client
from skyportal_client.api import followup_requests_api
from skyportal_client.model.followup_request_post import FollowupRequestPost
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = followup_requests_api.FollowupRequestsApi(api_client)
    followup_request_post = FollowupRequestPost(
        target_group_ids=[
            1,
        ],
        payload=None,
        allocation_id=1,
        obj_id="obj_id_example",
        status="pending submission",
    ) # FollowupRequestPost |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_followup_request_post(followup_request_post=followup_request_post)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling FollowupRequestsApi->api_followup_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **followup_request_post** | [**FollowupRequestPost**](FollowupRequestPost.md)|  | [optional]

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

# **api_followup_request_request_id_delete**
> Success api_followup_request_request_id_delete(request_id)



Delete follow-up request.

### Example

```python
import time
import skyportal_client
from skyportal_client.api import followup_requests_api
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
    api_instance = followup_requests_api.FollowupRequestsApi(api_client)
    request_id = "request_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_followup_request_request_id_delete(request_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling FollowupRequestsApi->api_followup_request_request_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  |

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

# **api_followup_request_request_id_put**
> Success api_followup_request_request_id_put(request_id)



Update a follow-up request

### Example

```python
import time
import skyportal_client
from skyportal_client.api import followup_requests_api
from skyportal_client.model.error import Error
from skyportal_client.model.success import Success
from skyportal_client.model.followup_request_post import FollowupRequestPost
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = followup_requests_api.FollowupRequestsApi(api_client)
    request_id = "request_id_example" # str | 
    followup_request_post = FollowupRequestPost(
        target_group_ids=[
            1,
        ],
        payload=None,
        allocation_id=1,
        obj_id="obj_id_example",
        status="pending submission",
    ) # FollowupRequestPost |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_followup_request_request_id_put(request_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling FollowupRequestsApi->api_followup_request_request_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_followup_request_request_id_put(request_id, followup_request_post=followup_request_post)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling FollowupRequestsApi->api_followup_request_request_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  |
 **followup_request_post** | [**FollowupRequestPost**](FollowupRequestPost.md)|  | [optional]

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

