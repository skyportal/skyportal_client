# skyportal_client.UsersApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_group_admission_requests_admission_request_id_delete**](UsersApi.md#api_group_admission_requests_admission_request_id_delete) | **DELETE** /api/group_admission_requests/admission_request_id | 
[**api_group_admission_requests_admission_request_id_get**](UsersApi.md#api_group_admission_requests_admission_request_id_get) | **GET** /api/group_admission_requests/admission_request_id | 
[**api_group_admission_requests_admission_request_id_patch**](UsersApi.md#api_group_admission_requests_admission_request_id_patch) | **PATCH** /api/group_admission_requests/admission_request_id | 
[**api_group_admission_requests_get**](UsersApi.md#api_group_admission_requests_get) | **GET** /api/group_admission_requests | 
[**api_group_admission_requests_post**](UsersApi.md#api_group_admission_requests_post) | **POST** /api/group_admission_requests | 
[**api_groups_group_id_users_from_groups_ignored_args_post**](UsersApi.md#api_groups_group_id_users_from_groups_ignored_args_post) | **POST** /api/groups/group_id/usersFromGroups/ignored_args | 
[**api_groups_group_id_users_ignored_args_patch**](UsersApi.md#api_groups_group_id_users_ignored_args_patch) | **PATCH** /api/groups/group_id/users/ignored_args | 
[**api_groups_group_id_users_ignored_args_post**](UsersApi.md#api_groups_group_id_users_ignored_args_post) | **POST** /api/groups/group_id/users/ignored_args | 
[**api_groups_group_id_users_user_id_delete**](UsersApi.md#api_groups_group_id_users_user_id_delete) | **DELETE** /api/groups/group_id/users/user_id | 
[**api_streams_stream_id_users_ignored_args_post**](UsersApi.md#api_streams_stream_id_users_ignored_args_post) | **POST** /api/streams/stream_id/users/ignored_args | 
[**api_streams_stream_id_users_user_id_delete**](UsersApi.md#api_streams_stream_id_users_user_id_delete) | **DELETE** /api/streams/stream_id/users/user_id | 
[**api_user_get**](UsersApi.md#api_user_get) | **GET** /api/user | 
[**api_user_post**](UsersApi.md#api_user_post) | **POST** /api/user | 
[**api_user_user_id_delete**](UsersApi.md#api_user_user_id_delete) | **DELETE** /api/user/user_id | 
[**api_user_user_id_get**](UsersApi.md#api_user_user_id_get) | **GET** /api/user/user_id | 


# **api_group_admission_requests_admission_request_id_delete**
> Success api_group_admission_requests_admission_request_id_delete(admission_request_id)



Delete a group admission request

### Example

```python
import time
import skyportal_client
from skyportal_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    admission_request_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_group_admission_requests_admission_request_id_delete(admission_request_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_group_admission_requests_admission_request_id_delete: %s\n" % e)
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
from skyportal_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    admission_request_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_group_admission_requests_admission_request_id_get(admission_request_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_group_admission_requests_admission_request_id_get: %s\n" % e)
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
from skyportal_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    admission_request_id = 1 # int | 
    inline_object7 = InlineObject7(
        status="status_example",
    ) # InlineObject7 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_group_admission_requests_admission_request_id_patch(admission_request_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_group_admission_requests_admission_request_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_group_admission_requests_admission_request_id_patch(admission_request_id, inline_object7=inline_object7)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_group_admission_requests_admission_request_id_patch: %s\n" % e)
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
from skyportal_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    group_id = 1 # int | ID of group for which admission requests are desired (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_group_admission_requests_get(group_id=group_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_group_admission_requests_get: %s\n" % e)
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
from skyportal_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
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
        print("Exception when calling UsersApi->api_group_admission_requests_post: %s\n" % e)
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

# **api_groups_group_id_users_from_groups_ignored_args_post**
> Success api_groups_group_id_users_from_groups_ignored_args_post(group_id)



Add users from other group(s) to specified group

### Example

```python
import time
import skyportal_client
from skyportal_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
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
        print("Exception when calling UsersApi->api_groups_group_id_users_from_groups_ignored_args_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_groups_group_id_users_from_groups_ignored_args_post(group_id, inline_object6=inline_object6)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_groups_group_id_users_from_groups_ignored_args_post: %s\n" % e)
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
from skyportal_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
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
        print("Exception when calling UsersApi->api_groups_group_id_users_ignored_args_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_groups_group_id_users_ignored_args_patch(group_id, inline_object5=inline_object5)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_groups_group_id_users_ignored_args_patch: %s\n" % e)
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
from skyportal_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
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
        print("Exception when calling UsersApi->api_groups_group_id_users_ignored_args_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_groups_group_id_users_ignored_args_post(group_id, inline_object4=inline_object4)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_groups_group_id_users_ignored_args_post: %s\n" % e)
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
from skyportal_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    group_id = 1 # int | 
    user_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_groups_group_id_users_user_id_delete(group_id, user_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_groups_group_id_users_user_id_delete: %s\n" % e)
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

# **api_streams_stream_id_users_ignored_args_post**
> object api_streams_stream_id_users_ignored_args_post(stream_id)



Grant stream access to a user

### Example

```python
import time
import skyportal_client
from skyportal_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    stream_id = 1 # int | 
    inline_object15 = InlineObject15(
        user_id=1,
    ) # InlineObject15 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_streams_stream_id_users_ignored_args_post(stream_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_streams_stream_id_users_ignored_args_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_streams_stream_id_users_ignored_args_post(stream_id, inline_object15=inline_object15)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_streams_stream_id_users_ignored_args_post: %s\n" % e)
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
from skyportal_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    stream_id = 1 # int | 
    user_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_streams_stream_id_users_user_id_delete(stream_id, user_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_streams_stream_id_users_user_id_delete: %s\n" % e)
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

# **api_user_get**
> object api_user_get()



Retrieve all users

### Example

```python
import time
import skyportal_client
from skyportal_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    num_per_page = 1 # int | Number of candidates to return per paginated request. Defaults to all users  (optional)
    page_number = 1 # int | Page number for paginated query results. Defaults to 1 (optional)
    first_name = "firstName_example" # str | Get users whose first name contains this string. (optional)
    last_name = "lastName_example" # str | Get users whose last name contains this string. (optional)
    username = "username_example" # str | Get users whose username contains this string. (optional)
    email = "email_example" # str | Get users whose email contains this string. (optional)
    role = "role_example" # str | Get users with the role. (optional)
    acl = "acl_example" # str | Get users with this ACL. (optional)
    group = "group_example" # str | Get users part of the group with name given by this parameter. (optional)
    stream = "stream_example" # str | Get users with access to the stream with name given by this parameter. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_user_get(num_per_page=num_per_page, page_number=page_number, first_name=first_name, last_name=last_name, username=username, email=email, role=role, acl=acl, group=group, stream=stream)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_per_page** | **int**| Number of candidates to return per paginated request. Defaults to all users  | [optional]
 **page_number** | **int**| Page number for paginated query results. Defaults to 1 | [optional]
 **first_name** | **str**| Get users whose first name contains this string. | [optional]
 **last_name** | **str**| Get users whose last name contains this string. | [optional]
 **username** | **str**| Get users whose username contains this string. | [optional]
 **email** | **str**| Get users whose email contains this string. | [optional]
 **role** | **str**| Get users with the role. | [optional]
 **acl** | **str**| Get users with this ACL. | [optional]
 **group** | **str**| Get users part of the group with name given by this parameter. | [optional]
 **stream** | **str**| Get users with access to the stream with name given by this parameter. | [optional]

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

# **api_user_post**
> object api_user_post()



Add a new user

### Example

```python
import time
import skyportal_client
from skyportal_client.api import users_api
from skyportal_client.model.inline_object22 import InlineObject22
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    inline_object22 = InlineObject22(
        username="username_example",
        first_name="first_name_example",
        last_name="last_name_example",
        contact_email="contact_email_example",
        oauth_uid="oauth_uid_example",
        contact_phone="contact_phone_example",
        roles=[
            "roles_example",
        ],
        group_i_ds_and_admin=[
null,
        ],
    ) # InlineObject22 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_user_post(inline_object22=inline_object22)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object22** | [**InlineObject22**](InlineObject22.md)|  | [optional]

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

# **api_user_user_id_delete**
> Success api_user_user_id_delete(user_id)



Delete a user

### Example

```python
import time
import skyportal_client
from skyportal_client.api import users_api
from skyportal_client.model.error import Error
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
    api_instance = users_api.UsersApi(api_client)
    user_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_user_user_id_delete(user_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_user_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_user_user_id_get**
> SingleUser api_user_user_id_get(user_id)



Retrieve a user

### Example

```python
import time
import skyportal_client
from skyportal_client.api import users_api
from skyportal_client.model.single_user import SingleUser
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
    api_instance = users_api.UsersApi(api_client)
    user_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_user_user_id_get(user_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling UsersApi->api_user_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  |

### Return type

[**SingleUser**](SingleUser.md)

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

