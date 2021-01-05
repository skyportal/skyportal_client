# skyportal_client.PhotometryApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_photometry_bulk_delete_upload_id_delete**](PhotometryApi.md#api_photometry_bulk_delete_upload_id_delete) | **DELETE** /api/photometry/bulk_delete/upload_id | 
[**api_photometry_photometry_id_delete**](PhotometryApi.md#api_photometry_photometry_id_delete) | **DELETE** /api/photometry/photometry_id | 
[**api_photometry_photometry_id_get**](PhotometryApi.md#api_photometry_photometry_id_get) | **GET** /api/photometry/photometry_id | 
[**api_photometry_photometry_id_patch**](PhotometryApi.md#api_photometry_photometry_id_patch) | **PATCH** /api/photometry/photometry_id | 
[**api_photometry_post**](PhotometryApi.md#api_photometry_post) | **POST** /api/photometry | 
[**api_photometry_put**](PhotometryApi.md#api_photometry_put) | **PUT** /api/photometry | 
[**api_photometry_range_get**](PhotometryApi.md#api_photometry_range_get) | **GET** /api/photometry/range | 
[**api_sources_obj_id_photometry_get**](PhotometryApi.md#api_sources_obj_id_photometry_get) | **GET** /api/sources/obj_id/photometry | 


# **api_photometry_bulk_delete_upload_id_delete**
> Success api_photometry_bulk_delete_upload_id_delete(upload_id)



Delete bulk-uploaded photometry set

### Example

```python
import time
import skyportal_client
from skyportal_client.api import photometry_api
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
    api_instance = photometry_api.PhotometryApi(api_client)
    upload_id = "upload_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_photometry_bulk_delete_upload_id_delete(upload_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling PhotometryApi->api_photometry_bulk_delete_upload_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  |

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

# **api_photometry_photometry_id_delete**
> Success api_photometry_photometry_id_delete(photometry_id)



Delete photometry

### Example

```python
import time
import skyportal_client
from skyportal_client.api import photometry_api
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
    api_instance = photometry_api.PhotometryApi(api_client)
    photometry_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_photometry_photometry_id_delete(photometry_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling PhotometryApi->api_photometry_photometry_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **photometry_id** | **int**|  |

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

# **api_photometry_photometry_id_get**
> object api_photometry_photometry_id_get(photometry_id)



Retrieve photometry

### Example

```python
import time
import skyportal_client
from skyportal_client.api import photometry_api
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
    api_instance = photometry_api.PhotometryApi(api_client)
    photometry_id = 1 # int | 
    format = "mag" # str | Return the photometry in flux or magnitude space? If a value for this query parameter is not provided, the result will be returned in magnitude space. (optional)
    magsys = "jla1" # str | The magnitude or zeropoint system of the output. (Default AB) (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_photometry_photometry_id_get(photometry_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling PhotometryApi->api_photometry_photometry_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_photometry_photometry_id_get(photometry_id, format=format, magsys=magsys)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling PhotometryApi->api_photometry_photometry_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **photometry_id** | **int**|  |
 **format** | **str**| Return the photometry in flux or magnitude space? If a value for this query parameter is not provided, the result will be returned in magnitude space. | [optional]
 **magsys** | **str**| The magnitude or zeropoint system of the output. (Default AB) | [optional]

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

# **api_photometry_photometry_id_patch**
> Success api_photometry_photometry_id_patch(photometry_id)



Update photometry

### Example

```python
import time
import skyportal_client
from skyportal_client.api import photometry_api
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
    api_instance = photometry_api.PhotometryApi(api_client)
    photometry_id = 1 # int | 
    unknown_base_type =  # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_photometry_photometry_id_patch(photometry_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling PhotometryApi->api_photometry_photometry_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_photometry_photometry_id_patch(photometry_id, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling PhotometryApi->api_photometry_photometry_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **photometry_id** | **int**|  |
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

# **api_photometry_post**
> object api_photometry_post()



Upload photometry

### Example

```python
import time
import skyportal_client
from skyportal_client.api import photometry_api
from skyportal_client.model.unknownbasetype import UNKNOWNBASETYPE
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = photometry_api.PhotometryApi(api_client)
    unknown_base_type =  # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_photometry_post(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling PhotometryApi->api_photometry_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

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

# **api_photometry_put**
> object api_photometry_put()



Update and/or upload photometry, resolving potential duplicates

### Example

```python
import time
import skyportal_client
from skyportal_client.api import photometry_api
from skyportal_client.model.unknownbasetype import UNKNOWNBASETYPE
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = photometry_api.PhotometryApi(api_client)
    unknown_base_type =  # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_photometry_put(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling PhotometryApi->api_photometry_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

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

# **api_photometry_range_get**
> object api_photometry_range_get()



Get photometry taken by specific instruments over a date range

### Example

```python
import time
import skyportal_client
from skyportal_client.api import photometry_api
from skyportal_client.model.error import Error
from skyportal_client.model.photometry_range_query import PhotometryRangeQuery
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = photometry_api.PhotometryApi(api_client)
    format = "mag" # str | Return the photometry in flux or magnitude space? If a value for this query parameter is not provided, the result will be returned in magnitude space. (optional)
    magsys = "jla1" # str | The magnitude or zeropoint system of the output. (Default AB) (optional)
    photometry_range_query = PhotometryRangeQuery(
        instrument_ids=[
            1,
        ],
        max_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        min_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # PhotometryRangeQuery |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_photometry_range_get(format=format, magsys=magsys, photometry_range_query=photometry_range_query)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling PhotometryApi->api_photometry_range_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Return the photometry in flux or magnitude space? If a value for this query parameter is not provided, the result will be returned in magnitude space. | [optional]
 **magsys** | **str**| The magnitude or zeropoint system of the output. (Default AB) | [optional]
 **photometry_range_query** | [**PhotometryRangeQuery**](PhotometryRangeQuery.md)|  | [optional]

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

# **api_sources_obj_id_photometry_get**
> object api_sources_obj_id_photometry_get(obj_id)



Retrieve all photometry associated with an Object

### Example

```python
import time
import skyportal_client
from skyportal_client.api import photometry_api
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
    api_instance = photometry_api.PhotometryApi(api_client)
    obj_id = "obj_id_example" # str | ID of the object to retrieve photometry for
    format = "mag" # str | Return the photometry in flux or magnitude space? If a value for this query parameter is not provided, the result will be returned in magnitude space. (optional)
    magsys = "jla1" # str | The magnitude or zeropoint system of the output. (Default AB) (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_sources_obj_id_photometry_get(obj_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling PhotometryApi->api_sources_obj_id_photometry_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_sources_obj_id_photometry_get(obj_id, format=format, magsys=magsys)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling PhotometryApi->api_sources_obj_id_photometry_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obj_id** | **str**| ID of the object to retrieve photometry for |
 **format** | **str**| Return the photometry in flux or magnitude space? If a value for this query parameter is not provided, the result will be returned in magnitude space. | [optional]
 **magsys** | **str**| The magnitude or zeropoint system of the output. (Default AB) | [optional]

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

