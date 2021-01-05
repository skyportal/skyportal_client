# skyportal_client.ClassificationsApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_classification_classification_id_delete**](ClassificationsApi.md#api_classification_classification_id_delete) | **DELETE** /api/classification/classification_id | 
[**api_classification_classification_id_get**](ClassificationsApi.md#api_classification_classification_id_get) | **GET** /api/classification/classification_id | 
[**api_classification_classification_id_put**](ClassificationsApi.md#api_classification_classification_id_put) | **PUT** /api/classification/classification_id | 
[**api_classification_post**](ClassificationsApi.md#api_classification_post) | **POST** /api/classification | 
[**api_sources_obj_id_classifications_get**](ClassificationsApi.md#api_sources_obj_id_classifications_get) | **GET** /api/sources/obj_id/classifications | 


# **api_classification_classification_id_delete**
> Success api_classification_classification_id_delete(classification_id)



Delete a classification

### Example

```python
import time
import skyportal_client
from skyportal_client.api import classifications_api
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
    api_instance = classifications_api.ClassificationsApi(api_client)
    classification_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_classification_classification_id_delete(classification_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ClassificationsApi->api_classification_classification_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification_id** | **int**|  |

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

# **api_classification_classification_id_get**
> SingleClassification api_classification_classification_id_get(classification_id)



Retrieve a classification

### Example

```python
import time
import skyportal_client
from skyportal_client.api import classifications_api
from skyportal_client.model.single_classification import SingleClassification
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
    api_instance = classifications_api.ClassificationsApi(api_client)
    classification_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_classification_classification_id_get(classification_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ClassificationsApi->api_classification_classification_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification_id** | **int**|  |

### Return type

[**SingleClassification**](SingleClassification.md)

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

# **api_classification_classification_id_put**
> Success api_classification_classification_id_put(classification)



Update a classification

### Example

```python
import time
import skyportal_client
from skyportal_client.api import classifications_api
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
    api_instance = classifications_api.ClassificationsApi(api_client)
    classification = 1 # int | 
    unknown_base_type =  # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_classification_classification_id_put(classification)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ClassificationsApi->api_classification_classification_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_classification_classification_id_put(classification, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ClassificationsApi->api_classification_classification_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification** | **int**|  |
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

# **api_classification_post**
> object api_classification_post()



Post a classification

### Example

```python
import time
import skyportal_client
from skyportal_client.api import classifications_api
from skyportal_client.model.inline_object import InlineObject
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = classifications_api.ClassificationsApi(api_client)
    inline_object = InlineObject(
        obj_id="obj_id_example",
        classification="classification_example",
        taxonomy_id=1,
null,
        group_ids=[
            1,
        ],
    ) # InlineObject |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_classification_post(inline_object=inline_object)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ClassificationsApi->api_classification_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional]

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

# **api_sources_obj_id_classifications_get**
> ArrayOfClassifications api_sources_obj_id_classifications_get(obj_id)



Retrieve an object's classifications

### Example

```python
import time
import skyportal_client
from skyportal_client.api import classifications_api
from skyportal_client.model.error import Error
from skyportal_client.model.array_of_classifications import ArrayOfClassifications
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = classifications_api.ClassificationsApi(api_client)
    obj_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_sources_obj_id_classifications_get(obj_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ClassificationsApi->api_sources_obj_id_classifications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obj_id** | **int**|  |

### Return type

[**ArrayOfClassifications**](ArrayOfClassifications.md)

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

