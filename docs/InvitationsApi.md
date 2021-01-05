# skyportal_client.InvitationsApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_invitations_get**](InvitationsApi.md#api_invitations_get) | **GET** /api/invitations | 
[**api_invitations_invitation_id_delete**](InvitationsApi.md#api_invitations_invitation_id_delete) | **DELETE** /api/invitations/invitation_id | 
[**api_invitations_invitation_id_patch**](InvitationsApi.md#api_invitations_invitation_id_patch) | **PATCH** /api/invitations/invitation_id | 
[**api_invitations_post**](InvitationsApi.md#api_invitations_post) | **POST** /api/invitations | 


# **api_invitations_get**
> object api_invitations_get()



Retrieve invitations

### Example

```python
import time
import skyportal_client
from skyportal_client.api import invitations_api
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = invitations_api.InvitationsApi(api_client)
    include_used = True # bool | Bool indicating whether to include used invitations. Defaults to false.  (optional)
    num_per_page = 1 # int | Number of candidates to return per paginated request. Defaults to 25  (optional)
    page_number = 1 # int | Page number for paginated query results. Defaults to 1 (optional)
    email = "email_example" # str | Get invitations whose email contains this string. (optional)
    group = "group_example" # str | Get invitations part of the group with name given by this parameter. (optional)
    stream = "stream_example" # str | Get invitations with access to the stream with name given by this parameter. (optional)
    invited_by = "invitedBy_example" # str | Get invitations invited by users whose username contains this string. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_invitations_get(include_used=include_used, num_per_page=num_per_page, page_number=page_number, email=email, group=group, stream=stream, invited_by=invited_by)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling InvitationsApi->api_invitations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_used** | **bool**| Bool indicating whether to include used invitations. Defaults to false.  | [optional]
 **num_per_page** | **int**| Number of candidates to return per paginated request. Defaults to 25  | [optional]
 **page_number** | **int**| Page number for paginated query results. Defaults to 1 | [optional]
 **email** | **str**| Get invitations whose email contains this string. | [optional]
 **group** | **str**| Get invitations part of the group with name given by this parameter. | [optional]
 **stream** | **str**| Get invitations with access to the stream with name given by this parameter. | [optional]
 **invited_by** | **str**| Get invitations invited by users whose username contains this string. | [optional]

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

# **api_invitations_invitation_id_delete**
> Success api_invitations_invitation_id_delete(invitation_id)



Delete an invitation

### Example

```python
import time
import skyportal_client
from skyportal_client.api import invitations_api
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
    api_instance = invitations_api.InvitationsApi(api_client)
    invitation_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_invitations_invitation_id_delete(invitation_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling InvitationsApi->api_invitations_invitation_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **int**|  |

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

# **api_invitations_invitation_id_patch**
> Success api_invitations_invitation_id_patch()



Update a pending invitation

### Example

```python
import time
import skyportal_client
from skyportal_client.api import invitations_api
from skyportal_client.model.inline_object10 import InlineObject10
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
    api_instance = invitations_api.InvitationsApi(api_client)
    inline_object10 = InlineObject10(
        group_i_ds=[
            1,
        ],
        stream_i_ds=[
            1,
        ],
    ) # InlineObject10 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_invitations_invitation_id_patch(inline_object10=inline_object10)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling InvitationsApi->api_invitations_invitation_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object10** | [**InlineObject10**](InlineObject10.md)|  | [optional]

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

# **api_invitations_post**
> Success api_invitations_post()



Invite a new user

### Example

```python
import time
import skyportal_client
from skyportal_client.api import invitations_api
from skyportal_client.model.inline_object9 import InlineObject9
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
    api_instance = invitations_api.InvitationsApi(api_client)
    inline_object9 = InlineObject9(
        user_email="user_email_example",
        stream_i_ds=[
            1,
        ],
        group_i_ds=[
            1,
        ],
        group_admin=[
            True,
        ],
    ) # InlineObject9 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_invitations_post(inline_object9=inline_object9)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling InvitationsApi->api_invitations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object9** | [**InlineObject9**](InlineObject9.md)|  | [optional]

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

