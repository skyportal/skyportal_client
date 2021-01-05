# skyportal_client.ObservingRunsApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_observing_run_get**](ObservingRunsApi.md#api_observing_run_get) | **GET** /api/observing_run | 
[**api_observing_run_post**](ObservingRunsApi.md#api_observing_run_post) | **POST** /api/observing_run | 
[**api_observing_run_run_id_delete**](ObservingRunsApi.md#api_observing_run_run_id_delete) | **DELETE** /api/observing_run/run_id | 
[**api_observing_run_run_id_get**](ObservingRunsApi.md#api_observing_run_run_id_get) | **GET** /api/observing_run/run_id | 
[**api_observing_run_run_id_put**](ObservingRunsApi.md#api_observing_run_run_id_put) | **PUT** /api/observing_run/run_id | 


# **api_observing_run_get**
> ArrayOfObservingRuns api_observing_run_get()



Retrieve all observing runs

### Example

```python
import time
import skyportal_client
from skyportal_client.api import observing_runs_api
from skyportal_client.model.array_of_observing_runs import ArrayOfObservingRuns
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
    api_instance = observing_runs_api.ObservingRunsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_observing_run_get()
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ObservingRunsApi->api_observing_run_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArrayOfObservingRuns**](ArrayOfObservingRuns.md)

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

# **api_observing_run_post**
> object api_observing_run_post()



Add a new observing run

### Example

```python
import time
import skyportal_client
from skyportal_client.api import observing_runs_api
from skyportal_client.model.observing_run_post import ObservingRunPost
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
    api_instance = observing_runs_api.ObservingRunsApi(api_client)
    observing_run_post = ObservingRunPost(
        instrument_id=1,
        group_id=1,
        observers="observers_example",
        pi="pi_example",
        calendar_date=dateutil_parser('1970-01-01').date(),
    ) # ObservingRunPost |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_observing_run_post(observing_run_post=observing_run_post)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ObservingRunsApi->api_observing_run_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observing_run_post** | [**ObservingRunPost**](ObservingRunPost.md)|  | [optional]

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

# **api_observing_run_run_id_delete**
> Success api_observing_run_run_id_delete(run_id)



Delete an observing run

### Example

```python
import time
import skyportal_client
from skyportal_client.api import observing_runs_api
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
    api_instance = observing_runs_api.ObservingRunsApi(api_client)
    run_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_observing_run_run_id_delete(run_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ObservingRunsApi->api_observing_run_run_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **int**|  |

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

# **api_observing_run_run_id_get**
> SingleObservingRunGetWithAssignments api_observing_run_run_id_get(run_id)



Retrieve an observing run

### Example

```python
import time
import skyportal_client
from skyportal_client.api import observing_runs_api
from skyportal_client.model.error import Error
from skyportal_client.model.single_observing_run_get_with_assignments import SingleObservingRunGetWithAssignments
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = observing_runs_api.ObservingRunsApi(api_client)
    run_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_observing_run_run_id_get(run_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ObservingRunsApi->api_observing_run_run_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **int**|  |

### Return type

[**SingleObservingRunGetWithAssignments**](SingleObservingRunGetWithAssignments.md)

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

# **api_observing_run_run_id_put**
> Success api_observing_run_run_id_put(run_id)



Update observing run

### Example

```python
import time
import skyportal_client
from skyportal_client.api import observing_runs_api
from skyportal_client.model.observing_run_post import ObservingRunPost
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
    api_instance = observing_runs_api.ObservingRunsApi(api_client)
    run_id = 1 # int | 
    observing_run_post = ObservingRunPost(
        instrument_id=1,
        group_id=1,
        observers="observers_example",
        pi="pi_example",
        calendar_date=dateutil_parser('1970-01-01').date(),
    ) # ObservingRunPost |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_observing_run_run_id_put(run_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ObservingRunsApi->api_observing_run_run_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_observing_run_run_id_put(run_id, observing_run_post=observing_run_post)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling ObservingRunsApi->api_observing_run_run_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **int**|  |
 **observing_run_post** | [**ObservingRunPost**](ObservingRunPost.md)|  | [optional]

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

