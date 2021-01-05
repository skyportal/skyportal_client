# skyportal_client.FiltersApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_filters_filter_id_delete**](FiltersApi.md#api_filters_filter_id_delete) | **DELETE** /api/filters/filter_id | 
[**api_filters_filter_id_get**](FiltersApi.md#api_filters_filter_id_get) | **GET** /api/filters/filter_id | 
[**api_filters_filter_id_patch**](FiltersApi.md#api_filters_filter_id_patch) | **PATCH** /api/filters/filter_id | 
[**api_filters_get**](FiltersApi.md#api_filters_get) | **GET** /api/filters | 
[**api_filters_post**](FiltersApi.md#api_filters_post) | **POST** /api/filters | 


# **api_filters_filter_id_delete**
> Success api_filters_filter_id_delete(filter_id)



Delete a filter

### Example

```python
import time
import skyportal_client
from skyportal_client.api import filters_api
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
    api_instance = filters_api.FiltersApi(api_client)
    filter_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_filters_filter_id_delete(filter_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling FiltersApi->api_filters_filter_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **int**|  |

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

# **api_filters_filter_id_get**
> SingleFilter api_filters_filter_id_get(filter_id)



Retrieve a filter

### Example

```python
import time
import skyportal_client
from skyportal_client.api import filters_api
from skyportal_client.model.error import Error
from skyportal_client.model.single_filter import SingleFilter
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = filters_api.FiltersApi(api_client)
    filter_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_filters_filter_id_get(filter_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling FiltersApi->api_filters_filter_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **int**|  |

### Return type

[**SingleFilter**](SingleFilter.md)

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

# **api_filters_filter_id_patch**
> Success api_filters_filter_id_patch(filter_id)



Update filter name

### Example

```python
import time
import skyportal_client
from skyportal_client.api import filters_api
from skyportal_client.model.error import Error
from skyportal_client.model.filter_no_id import FilterNoID
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
    api_instance = filters_api.FiltersApi(api_client)
    filter_id = 1 # int | 
    filter_no_id = FilterNoID(
        name="name_example",
        stream_id=1,
        group_id=1,
    ) # FilterNoID |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_filters_filter_id_patch(filter_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling FiltersApi->api_filters_filter_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_filters_filter_id_patch(filter_id, filter_no_id=filter_no_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling FiltersApi->api_filters_filter_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **int**|  |
 **filter_no_id** | [**FilterNoID**](FilterNoID.md)|  | [optional]

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

# **api_filters_get**
> ArrayOfFilters api_filters_get()



Retrieve all filters

### Example

```python
import time
import skyportal_client
from skyportal_client.api import filters_api
from skyportal_client.model.error import Error
from skyportal_client.model.array_of_filters import ArrayOfFilters
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = filters_api.FiltersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_filters_get()
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling FiltersApi->api_filters_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArrayOfFilters**](ArrayOfFilters.md)

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

# **api_filters_post**
> object api_filters_post()



POST a new filter.

### Example

```python
import time
import skyportal_client
from skyportal_client.api import filters_api
from skyportal_client.model.filter_no_id import FilterNoID
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = filters_api.FiltersApi(api_client)
    filter_no_id = FilterNoID(
        name="name_example",
        stream_id=1,
        group_id=1,
    ) # FilterNoID |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_filters_post(filter_no_id=filter_no_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling FiltersApi->api_filters_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_no_id** | [**FilterNoID**](FilterNoID.md)|  | [optional]

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

