# skyportal_client.AnnotationsApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_annotation_annotation_id_delete**](AnnotationsApi.md#api_annotation_annotation_id_delete) | **DELETE** /api/annotation/annotation_id | 
[**api_annotation_annotation_id_get**](AnnotationsApi.md#api_annotation_annotation_id_get) | **GET** /api/annotation/annotation_id | 
[**api_annotation_annotation_id_put**](AnnotationsApi.md#api_annotation_annotation_id_put) | **PUT** /api/annotation/annotation_id | 
[**api_annotation_post**](AnnotationsApi.md#api_annotation_post) | **POST** /api/annotation | 


# **api_annotation_annotation_id_delete**
> Success api_annotation_annotation_id_delete(annotation_id)



Delete an annotation

### Example

```python
import time
import skyportal_client
from skyportal_client.api import annotations_api
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
    api_instance = annotations_api.AnnotationsApi(api_client)
    annotation_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_annotation_annotation_id_delete(annotation_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AnnotationsApi->api_annotation_annotation_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_id** | **int**|  |

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

# **api_annotation_annotation_id_get**
> SingleAnnotation api_annotation_annotation_id_get(annotation_id)



Retrieve an annotation

### Example

```python
import time
import skyportal_client
from skyportal_client.api import annotations_api
from skyportal_client.model.error import Error
from skyportal_client.model.single_annotation import SingleAnnotation
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotations_api.AnnotationsApi(api_client)
    annotation_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_annotation_annotation_id_get(annotation_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AnnotationsApi->api_annotation_annotation_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_id** | **int**|  |

### Return type

[**SingleAnnotation**](SingleAnnotation.md)

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

# **api_annotation_annotation_id_put**
> Success api_annotation_annotation_id_put(annotation_id)



Update an annotation

### Example

```python
import time
import skyportal_client
from skyportal_client.api import annotations_api
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
    api_instance = annotations_api.AnnotationsApi(api_client)
    annotation_id = 1 # int | 
    unknown_base_type =  # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_annotation_annotation_id_put(annotation_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AnnotationsApi->api_annotation_annotation_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_annotation_annotation_id_put(annotation_id, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AnnotationsApi->api_annotation_annotation_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_id** | **int**|  |
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

# **api_annotation_post**
> object api_annotation_post()



Post an annotation

### Example

```python
import time
import skyportal_client
from skyportal_client.api import annotations_api
from skyportal_client.model.inline_object2 import InlineObject2
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotations_api.AnnotationsApi(api_client)
    inline_object2 = InlineObject2(
        obj_id="obj_id_example",
        origin="origin_example",
        data={},
        group_ids=[
            1,
        ],
    ) # InlineObject2 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_annotation_post(inline_object2=inline_object2)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AnnotationsApi->api_annotation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | [optional]

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

