# skyportal_client.AllocationsApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_allocation_allocation_id_delete**](AllocationsApi.md#api_allocation_allocation_id_delete) | **DELETE** /api/allocation/allocation_id | 
[**api_allocation_allocation_id_get**](AllocationsApi.md#api_allocation_allocation_id_get) | **GET** /api/allocation/allocation_id | 
[**api_allocation_allocation_id_put**](AllocationsApi.md#api_allocation_allocation_id_put) | **PUT** /api/allocation/allocation_id | 
[**api_allocation_get**](AllocationsApi.md#api_allocation_get) | **GET** /api/allocation | 
[**api_allocation_post**](AllocationsApi.md#api_allocation_post) | **POST** /api/allocation | 


# **api_allocation_allocation_id_delete**
> Success api_allocation_allocation_id_delete(allocation_id)



Delete allocation.

### Example

```python
import time
import skyportal_client
from skyportal_client.api import allocations_api
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
    api_instance = allocations_api.AllocationsApi(api_client)
    allocation_id = "allocation_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_allocation_allocation_id_delete(allocation_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AllocationsApi->api_allocation_allocation_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocation_id** | **str**|  |

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

# **api_allocation_allocation_id_get**
> SingleAllocation api_allocation_allocation_id_get(allocation_id)



Retrieve an allocation

### Example

```python
import time
import skyportal_client
from skyportal_client.api import allocations_api
from skyportal_client.model.error import Error
from skyportal_client.model.single_allocation import SingleAllocation
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = allocations_api.AllocationsApi(api_client)
    allocation_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_allocation_allocation_id_get(allocation_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AllocationsApi->api_allocation_allocation_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocation_id** | **int**|  |

### Return type

[**SingleAllocation**](SingleAllocation.md)

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

# **api_allocation_allocation_id_put**
> Success api_allocation_allocation_id_put(allocation_id)



Update an allocation on a robotic instrument

### Example

```python
import time
import skyportal_client
from skyportal_client.api import allocations_api
from skyportal_client.model.error import Error
from skyportal_client.model.allocation_no_id import AllocationNoID
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
    api_instance = allocations_api.AllocationsApi(api_client)
    allocation_id = 1 # int | 
    allocation_no_id = AllocationNoID(
        pi="pi_example",
        proposal_id="proposal_id_example",
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        hours_allocated=3.14,
        group_id=1,
        instrument_id=1,
    ) # AllocationNoID |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_allocation_allocation_id_put(allocation_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AllocationsApi->api_allocation_allocation_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_allocation_allocation_id_put(allocation_id, allocation_no_id=allocation_no_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AllocationsApi->api_allocation_allocation_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocation_id** | **int**|  |
 **allocation_no_id** | [**AllocationNoID**](AllocationNoID.md)|  | [optional]

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

# **api_allocation_get**
> ArrayOfAllocations api_allocation_get()



Retrieve all allocations

### Example

```python
import time
import skyportal_client
from skyportal_client.api import allocations_api
from skyportal_client.model.array_of_allocations import ArrayOfAllocations
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
    api_instance = allocations_api.AllocationsApi(api_client)
    instrument_id = 3.14 # float | Instrument ID to retrieve allocations for (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_allocation_get(instrument_id=instrument_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AllocationsApi->api_allocation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_id** | **float**| Instrument ID to retrieve allocations for | [optional]

### Return type

[**ArrayOfAllocations**](ArrayOfAllocations.md)

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

# **api_allocation_post**
> object api_allocation_post()



Post new allocation on a robotic instrument

### Example

```python
import time
import skyportal_client
from skyportal_client.api import allocations_api
from skyportal_client.model.allocation_no_id import AllocationNoID
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = allocations_api.AllocationsApi(api_client)
    allocation_no_id = AllocationNoID(
        pi="pi_example",
        proposal_id="proposal_id_example",
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        hours_allocated=3.14,
        group_id=1,
        instrument_id=1,
    ) # AllocationNoID |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_allocation_post(allocation_no_id=allocation_no_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AllocationsApi->api_allocation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocation_no_id** | [**AllocationNoID**](AllocationNoID.md)|  | [optional]

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

