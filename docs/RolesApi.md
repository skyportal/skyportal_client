# skyportal_client.RolesApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_roles_get**](RolesApi.md#api_roles_get) | **GET** /api/roles | 
[**api_user_user_id_roles_ignored_args_post**](RolesApi.md#api_user_user_id_roles_ignored_args_post) | **POST** /api/user/user_id/roles/ignored_args | 
[**api_user_user_id_roles_role_id_delete**](RolesApi.md#api_user_user_id_roles_role_id_delete) | **DELETE** /api/user/user_id/roles/role_id | 


# **api_roles_get**
> object api_roles_get()



Retrieve list of all Role IDs (strings)

### Example

```python
import time
import skyportal_client
from skyportal_client.api import roles_api
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = roles_api.RolesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_roles_get()
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling RolesApi->api_roles_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_user_user_id_roles_ignored_args_post**
> Success api_user_user_id_roles_ignored_args_post(user_id)



Grant new Role(s) to a user

### Example

```python
import time
import skyportal_client
from skyportal_client.api import roles_api
from skyportal_client.model.inline_object21 import InlineObject21
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
    api_instance = roles_api.RolesApi(api_client)
    user_id = 1 # int | 
    inline_object21 = InlineObject21(
        role_ids=[
            "role_ids_example",
        ],
    ) # InlineObject21 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_user_user_id_roles_ignored_args_post(user_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling RolesApi->api_user_user_id_roles_ignored_args_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_user_user_id_roles_ignored_args_post(user_id, inline_object21=inline_object21)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling RolesApi->api_user_user_id_roles_ignored_args_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  |
 **inline_object21** | [**InlineObject21**](InlineObject21.md)|  | [optional]

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

# **api_user_user_id_roles_role_id_delete**
> Success api_user_user_id_roles_role_id_delete(user_id, role_id)



Delete user role

### Example

```python
import time
import skyportal_client
from skyportal_client.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    user_id = 1 # int | 
    role_id = "role_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_user_user_id_roles_role_id_delete(user_id, role_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling RolesApi->api_user_user_id_roles_role_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  |
 **role_id** | **str**|  |

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

