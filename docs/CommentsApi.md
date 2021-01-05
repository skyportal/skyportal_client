# skyportal_client.CommentsApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_comment_comment_id_attachment_get**](CommentsApi.md#api_comment_comment_id_attachment_get) | **GET** /api/comment/comment_id/attachment | 
[**api_comment_comment_id_attachment_pdf_get**](CommentsApi.md#api_comment_comment_id_attachment_pdf_get) | **GET** /api/comment/comment_id/attachment.pdf | 
[**api_comment_comment_id_delete**](CommentsApi.md#api_comment_comment_id_delete) | **DELETE** /api/comment/comment_id | 
[**api_comment_comment_id_get**](CommentsApi.md#api_comment_comment_id_get) | **GET** /api/comment/comment_id | 
[**api_comment_comment_id_put**](CommentsApi.md#api_comment_comment_id_put) | **PUT** /api/comment/comment_id | 
[**api_comment_post**](CommentsApi.md#api_comment_post) | **POST** /api/comment | 


# **api_comment_comment_id_attachment_get**
> str api_comment_comment_id_attachment_get(comment_id)



Download comment attachment

### Example

```python
import time
import skyportal_client
from skyportal_client.api import comments_api
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = comments_api.CommentsApi(api_client)
    comment_id = 1 # int | 
    download = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_comment_comment_id_attachment_get(comment_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling CommentsApi->api_comment_comment_id_attachment_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_comment_comment_id_attachment_get(comment_id, download=download)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling CommentsApi->api_comment_comment_id_attachment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**|  |
 **download** | **bool**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_comment_comment_id_attachment_pdf_get**
> str api_comment_comment_id_attachment_pdf_get(comment_id)



Download comment attachment

### Example

```python
import time
import skyportal_client
from skyportal_client.api import comments_api
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = comments_api.CommentsApi(api_client)
    comment_id = 1 # int | 
    download = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_comment_comment_id_attachment_pdf_get(comment_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling CommentsApi->api_comment_comment_id_attachment_pdf_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_comment_comment_id_attachment_pdf_get(comment_id, download=download)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling CommentsApi->api_comment_comment_id_attachment_pdf_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**|  |
 **download** | **bool**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_comment_comment_id_delete**
> Success api_comment_comment_id_delete(comment_id)



Delete a comment

### Example

```python
import time
import skyportal_client
from skyportal_client.api import comments_api
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
    api_instance = comments_api.CommentsApi(api_client)
    comment_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_comment_comment_id_delete(comment_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling CommentsApi->api_comment_comment_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**|  |

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

# **api_comment_comment_id_get**
> SingleComment api_comment_comment_id_get(comment_id)



Retrieve a comment

### Example

```python
import time
import skyportal_client
from skyportal_client.api import comments_api
from skyportal_client.model.error import Error
from skyportal_client.model.single_comment import SingleComment
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = comments_api.CommentsApi(api_client)
    comment_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_comment_comment_id_get(comment_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling CommentsApi->api_comment_comment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**|  |

### Return type

[**SingleComment**](SingleComment.md)

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

# **api_comment_comment_id_put**
> Success api_comment_comment_id_put(comment_id)



Update a comment

### Example

```python
import time
import skyportal_client
from skyportal_client.api import comments_api
from skyportal_client.model.unknownbasetype import UNKNOWNBASETYPE
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
    api_instance = comments_api.CommentsApi(api_client)
    comment_id = 1 # int | 
    unknown_base_type =  # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_comment_comment_id_put(comment_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling CommentsApi->api_comment_comment_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_comment_comment_id_put(comment_id, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling CommentsApi->api_comment_comment_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**|  |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

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

# **api_comment_post**
> object api_comment_post()



Post a comment

### Example

```python
import time
import skyportal_client
from skyportal_client.api import comments_api
from skyportal_client.model.inline_object1 import InlineObject1
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = comments_api.CommentsApi(api_client)
    inline_object1 = InlineObject1(
        obj_id="obj_id_example",
        text="text_example",
        group_ids=[
            1,
        ],
        attachment=ApiCommentAttachment(
            body='YQ==',
            name="name_example",
        ),
    ) # InlineObject1 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_comment_post(inline_object1=inline_object1)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling CommentsApi->api_comment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | [optional]

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

