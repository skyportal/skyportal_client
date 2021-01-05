# skyportal_client.ThumbnailsApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_thumbnail_post**](ThumbnailsApi.md#api_thumbnail_post) | **POST** /api/thumbnail | 
[**api_thumbnail_thumbnail_id_delete**](ThumbnailsApi.md#api_thumbnail_thumbnail_id_delete) | **DELETE** /api/thumbnail/thumbnail_id | 
[**api_thumbnail_thumbnail_id_get**](ThumbnailsApi.md#api_thumbnail_thumbnail_id_get) | **GET** /api/thumbnail/thumbnail_id | 
[**api_thumbnail_thumbnail_id_put**](ThumbnailsApi.md#api_thumbnail_thumbnail_id_put) | **PUT** /api/thumbnail/thumbnail_id | 


# **api_thumbnail_post**
> object api_thumbnail_post()



Upload thumbnails

### Example

```python
import time
import skyportal_client
from skyportal_client.api import thumbnails_api
from skyportal_client.model.error import Error
from skyportal_client.model.inline_object19 import InlineObject19
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = thumbnails_api.ThumbnailsApi(api_client)
    inline_object19 = InlineObject19(
        obj_id="obj_id_example",
        data='YQ==',
        ttype="ttype_example",
    ) # InlineObject19 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_thumbnail_post(inline_object19=inline_object19)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ThumbnailsApi->api_thumbnail_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object19** | [**InlineObject19**](InlineObject19.md)|  | [optional]

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
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_thumbnail_thumbnail_id_delete**
> Success api_thumbnail_thumbnail_id_delete(thumbnail_id)



Delete a thumbnail

### Example

```python
import time
import skyportal_client
from skyportal_client.api import thumbnails_api
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
    api_instance = thumbnails_api.ThumbnailsApi(api_client)
    thumbnail_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_thumbnail_thumbnail_id_delete(thumbnail_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ThumbnailsApi->api_thumbnail_thumbnail_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thumbnail_id** | **int**|  |

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

# **api_thumbnail_thumbnail_id_get**
> SingleThumbnail api_thumbnail_thumbnail_id_get(thumbnail_id)



Retrieve a thumbnail

### Example

```python
import time
import skyportal_client
from skyportal_client.api import thumbnails_api
from skyportal_client.model.single_thumbnail import SingleThumbnail
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
    api_instance = thumbnails_api.ThumbnailsApi(api_client)
    thumbnail_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_thumbnail_thumbnail_id_get(thumbnail_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ThumbnailsApi->api_thumbnail_thumbnail_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thumbnail_id** | **int**|  |

### Return type

[**SingleThumbnail**](SingleThumbnail.md)

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

# **api_thumbnail_thumbnail_id_put**
> Success api_thumbnail_thumbnail_id_put(thumbnail_id)



Update thumbnail

### Example

```python
import time
import skyportal_client
from skyportal_client.api import thumbnails_api
from skyportal_client.model.error import Error
from skyportal_client.model.success import Success
from skyportal_client.model.thumbnail_no_id import ThumbnailNoID
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = thumbnails_api.ThumbnailsApi(api_client)
    thumbnail_id = 1 # int | 
    thumbnail_no_id = ThumbnailNoID(
        type="new",
        file_uri="file_uri_example",
        public_url="public_url_example",
        origin="origin_example",
        obj_id="obj_id_example",
    ) # ThumbnailNoID |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_thumbnail_thumbnail_id_put(thumbnail_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ThumbnailsApi->api_thumbnail_thumbnail_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_thumbnail_thumbnail_id_put(thumbnail_id, thumbnail_no_id=thumbnail_no_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ThumbnailsApi->api_thumbnail_thumbnail_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thumbnail_id** | **int**|  |
 **thumbnail_no_id** | [**ThumbnailNoID**](ThumbnailNoID.md)|  | [optional]

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

