# skyportal_client.AclsApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_user_user_id_acls_acl_id_delete**](AclsApi.md#api_user_user_id_acls_acl_id_delete) | **DELETE** /api/user/user_id/acls/acl_id | 
[**api_user_user_id_acls_ignored_args_post**](AclsApi.md#api_user_user_id_acls_ignored_args_post) | **POST** /api/user/user_id/acls/ignored_args | 


# **api_user_user_id_acls_acl_id_delete**
> Success api_user_user_id_acls_acl_id_delete(user_id, acl_id)



Remove ACL from user permissions

### Example

```python
import time
import skyportal_client
from skyportal_client.api import acls_api
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
    api_instance = acls_api.AclsApi(api_client)
    user_id = 1 # int | 
    acl_id = "acl_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_user_user_id_acls_acl_id_delete(user_id, acl_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AclsApi->api_user_user_id_acls_acl_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  |
 **acl_id** | **str**|  |

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

# **api_user_user_id_acls_ignored_args_post**
> Success api_user_user_id_acls_ignored_args_post(user_id)



Grant new ACL(s) to a user

### Example

```python
import time
import skyportal_client
from skyportal_client.api import acls_api
from skyportal_client.model.inline_object20 import InlineObject20
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
    api_instance = acls_api.AclsApi(api_client)
    user_id = 1 # int | 
    inline_object20 = InlineObject20(
        acl_ids=[
            "acl_ids_example",
        ],
    ) # InlineObject20 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_user_user_id_acls_ignored_args_post(user_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AclsApi->api_user_user_id_acls_ignored_args_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_user_user_id_acls_ignored_args_post(user_id, inline_object20=inline_object20)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AclsApi->api_user_user_id_acls_ignored_args_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  |
 **inline_object20** | [**InlineObject20**](InlineObject20.md)|  | [optional]

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

