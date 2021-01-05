# skyportal_client.AssignmentsApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_assignment_assignment_id_delete**](AssignmentsApi.md#api_assignment_assignment_id_delete) | **DELETE** /api/assignment/assignment_id | 
[**api_assignment_assignment_id_get**](AssignmentsApi.md#api_assignment_assignment_id_get) | **GET** /api/assignment/assignment_id | 
[**api_assignment_assignment_id_put**](AssignmentsApi.md#api_assignment_assignment_id_put) | **PUT** /api/assignment/assignment_id | 
[**api_assignment_get**](AssignmentsApi.md#api_assignment_get) | **GET** /api/assignment | 
[**api_assignment_post**](AssignmentsApi.md#api_assignment_post) | **POST** /api/assignment | 


# **api_assignment_assignment_id_delete**
> Success api_assignment_assignment_id_delete(assignment_id)



Delete assignment.

### Example

```python
import time
import skyportal_client
from skyportal_client.api import assignments_api
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
    api_instance = assignments_api.AssignmentsApi(api_client)
    assignment_id = "assignment_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_assignment_assignment_id_delete(assignment_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AssignmentsApi->api_assignment_assignment_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**|  |

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

# **api_assignment_assignment_id_get**
> SingleClassicalAssignment api_assignment_assignment_id_get(assignment_id)



Retrieve an observing run assignment

### Example

```python
import time
import skyportal_client
from skyportal_client.api import assignments_api
from skyportal_client.model.error import Error
from skyportal_client.model.single_classical_assignment import SingleClassicalAssignment
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = assignments_api.AssignmentsApi(api_client)
    assignment_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_assignment_assignment_id_get(assignment_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AssignmentsApi->api_assignment_assignment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **int**|  |

### Return type

[**SingleClassicalAssignment**](SingleClassicalAssignment.md)

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

# **api_assignment_assignment_id_put**
> Success api_assignment_assignment_id_put(assignment_id)



Update an assignment

### Example

```python
import time
import skyportal_client
from skyportal_client.api import assignments_api
from skyportal_client.model.error import Error
from skyportal_client.model.classical_assignment_no_id import ClassicalAssignmentNoID
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
    api_instance = assignments_api.AssignmentsApi(api_client)
    assignment_id = 1 # int | 
    classical_assignment_no_id = ClassicalAssignmentNoID(
        requester_id=1,
        obj_id="obj_id_example",
        comment="comment_example",
        status="status_example",
        priority="1",
        run_id=1,
    ) # ClassicalAssignmentNoID |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_assignment_assignment_id_put(assignment_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AssignmentsApi->api_assignment_assignment_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_assignment_assignment_id_put(assignment_id, classical_assignment_no_id=classical_assignment_no_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AssignmentsApi->api_assignment_assignment_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **int**|  |
 **classical_assignment_no_id** | [**ClassicalAssignmentNoID**](ClassicalAssignmentNoID.md)|  | [optional]

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

# **api_assignment_get**
> ArrayOfClassicalAssignments api_assignment_get()



Retrieve all observing run assignments

### Example

```python
import time
import skyportal_client
from skyportal_client.api import assignments_api
from skyportal_client.model.error import Error
from skyportal_client.model.array_of_classical_assignments import ArrayOfClassicalAssignments
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = assignments_api.AssignmentsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_assignment_get()
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AssignmentsApi->api_assignment_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArrayOfClassicalAssignments**](ArrayOfClassicalAssignments.md)

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

# **api_assignment_post**
> object api_assignment_post()



Post new target assignment to observing run

### Example

```python
import time
import skyportal_client
from skyportal_client.api import assignments_api
from skyportal_client.model.assignment_schema import AssignmentSchema
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = assignments_api.AssignmentsApi(api_client)
    assignment_schema = AssignmentSchema(
        run_id=1,
        comment="comment_example",
        priority="1",
        obj_id="obj_id_example",
        status="status_example",
    ) # AssignmentSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_assignment_post(assignment_schema=assignment_schema)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling AssignmentsApi->api_assignment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_schema** | [**AssignmentSchema**](AssignmentSchema.md)|  | [optional]

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

