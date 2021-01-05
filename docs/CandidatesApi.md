# skyportal_client.CandidatesApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_candidates_candidate_id_delete**](CandidatesApi.md#api_candidates_candidate_id_delete) | **DELETE** /api/candidates/candidate_id | 
[**api_candidates_get**](CandidatesApi.md#api_candidates_get) | **GET** /api/candidates | 
[**api_candidates_obj_id_get**](CandidatesApi.md#api_candidates_obj_id_get) | **GET** /api/candidates/obj_id | 
[**api_candidates_obj_id_head**](CandidatesApi.md#api_candidates_obj_id_head) | **HEAD** /api/candidates/obj_id | 
[**api_candidates_post**](CandidatesApi.md#api_candidates_post) | **POST** /api/candidates | 


# **api_candidates_candidate_id_delete**
> Success api_candidates_candidate_id_delete(candidate_id)



Delete a candidate

### Example

```python
import time
import skyportal_client
from skyportal_client.api import candidates_api
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
    api_instance = candidates_api.CandidatesApi(api_client)
    candidate_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_candidates_candidate_id_delete(candidate_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling CandidatesApi->api_candidates_candidate_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **candidate_id** | **int**|  |

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

# **api_candidates_get**
> object api_candidates_get()



Retrieve all candidates

### Example

```python
import time
import skyportal_client
from skyportal_client.api import candidates_api
from skyportal_client.model.list import List
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
    api_instance = candidates_api.CandidatesApi(api_client)
    num_per_page = 1 # int | Number of candidates to return per paginated request. Defaults to 25  (optional)
    page_number = 1 # int | Page number for paginated query results. Defaults to 1 (optional)
    total_matches = 1 # int | Used only in the case of paginating query results - if provided, this allows for avoiding a potentially expensive query.count() call.  (optional)
    unsaved_only = True # bool | Boolean indicating whether to return only unsaved candidates (optional)
    start_date = "startDate_example" # str | Arrow-parseable date string (e.g. 2020-01-01). If provided, filter by Candidate.passed_at >= startDate  (optional)
    end_date = "endDate_example" # str | Arrow-parseable date string (e.g. 2020-01-01). If provided, filter by Candidate.passed_at <= endDate  (optional)
    group_i_ds = [
        1,
    ] # [int] | Comma-separated string of group IDs (e.g. \"1,2\"). Defaults to all of user's groups if filterIDs is not provided.  (optional)
    filter_i_ds = [
        1,
    ] # [int] | Comma-separated string of filter IDs (e.g. \"1,2\"). Defaults to all of user's groups' filters if groupIDs is not provided.  (optional)
    sort_by_annotation_origin = "sortByAnnotationOrigin_example" # str | The origin of the Annotation to sort by  (optional)
    sort_by_annotation_key = "sortByAnnotationKey_example" # str | The key of the Annotation data value to sort by  (optional)
    sort_by_annotation_order = "sortByAnnotationOrder_example" # str | The sort order for annotations - either \"asc\" or \"desc\". Defaults to \"asc\".  (optional)
    annotation_filter_list = [
        "annotationFilterList_example",
    ] # [str] | Comma-separated string of JSON objects representing annotation filters. Filter objects are expected to have keys { origin, key, value } for non-numeric value types, or { origin, key, min, max } for numeric values.  (optional)
    include_photometry = True # bool | Boolean indicating whether to include associated photometry. Defaults to false.  (optional)
    classifications = [
        "classifications_example",
    ] # [str] | Comma-separated string of classification(s) to filter for candidates matching that/those classification(s).  (optional)
    redshift_range =  # List | lowest and highest redshift to return, e.g. \"(0,0.5)\"  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_candidates_get(num_per_page=num_per_page, page_number=page_number, total_matches=total_matches, unsaved_only=unsaved_only, start_date=start_date, end_date=end_date, group_i_ds=group_i_ds, filter_i_ds=filter_i_ds, sort_by_annotation_origin=sort_by_annotation_origin, sort_by_annotation_key=sort_by_annotation_key, sort_by_annotation_order=sort_by_annotation_order, annotation_filter_list=annotation_filter_list, include_photometry=include_photometry, classifications=classifications, redshift_range=redshift_range)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling CandidatesApi->api_candidates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_per_page** | **int**| Number of candidates to return per paginated request. Defaults to 25  | [optional]
 **page_number** | **int**| Page number for paginated query results. Defaults to 1 | [optional]
 **total_matches** | **int**| Used only in the case of paginating query results - if provided, this allows for avoiding a potentially expensive query.count() call.  | [optional]
 **unsaved_only** | **bool**| Boolean indicating whether to return only unsaved candidates | [optional]
 **start_date** | **str**| Arrow-parseable date string (e.g. 2020-01-01). If provided, filter by Candidate.passed_at &gt;&#x3D; startDate  | [optional]
 **end_date** | **str**| Arrow-parseable date string (e.g. 2020-01-01). If provided, filter by Candidate.passed_at &lt;&#x3D; endDate  | [optional]
 **group_i_ds** | **[int]**| Comma-separated string of group IDs (e.g. \&quot;1,2\&quot;). Defaults to all of user&#39;s groups if filterIDs is not provided.  | [optional]
 **filter_i_ds** | **[int]**| Comma-separated string of filter IDs (e.g. \&quot;1,2\&quot;). Defaults to all of user&#39;s groups&#39; filters if groupIDs is not provided.  | [optional]
 **sort_by_annotation_origin** | **str**| The origin of the Annotation to sort by  | [optional]
 **sort_by_annotation_key** | **str**| The key of the Annotation data value to sort by  | [optional]
 **sort_by_annotation_order** | **str**| The sort order for annotations - either \&quot;asc\&quot; or \&quot;desc\&quot;. Defaults to \&quot;asc\&quot;.  | [optional]
 **annotation_filter_list** | **[str]**| Comma-separated string of JSON objects representing annotation filters. Filter objects are expected to have keys { origin, key, value } for non-numeric value types, or { origin, key, min, max } for numeric values.  | [optional]
 **include_photometry** | **bool**| Boolean indicating whether to include associated photometry. Defaults to false.  | [optional]
 **classifications** | **[str]**| Comma-separated string of classification(s) to filter for candidates matching that/those classification(s).  | [optional]
 **redshift_range** | **List**| lowest and highest redshift to return, e.g. \&quot;(0,0.5)\&quot;  | [optional]

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

# **api_candidates_obj_id_get**
> SingleObj api_candidates_obj_id_get(obj_id)



Retrieve a candidate

### Example

```python
import time
import skyportal_client
from skyportal_client.api import candidates_api
from skyportal_client.model.error import Error
from skyportal_client.model.single_obj import SingleObj
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = candidates_api.CandidatesApi(api_client)
    obj_id = "obj_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_candidates_obj_id_get(obj_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling CandidatesApi->api_candidates_obj_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obj_id** | **str**|  |

### Return type

[**SingleObj**](SingleObj.md)

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

# **api_candidates_obj_id_head**
> Success api_candidates_obj_id_head(obj_id)



Check if a Candidate exists

### Example

```python
import time
import skyportal_client
from skyportal_client.api import candidates_api
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
    api_instance = candidates_api.CandidatesApi(api_client)
    obj_id = "obj_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_candidates_obj_id_head(obj_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling CandidatesApi->api_candidates_obj_id_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obj_id** | **str**|  |

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
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_candidates_post**
> object api_candidates_post()



Create new candidate(s) (one per filter).

### Example

```python
import time
import skyportal_client
from skyportal_client.api import candidates_api
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
    api_instance = candidates_api.CandidatesApi(api_client)
    unknown_base_type =  # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_candidates_post(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling CandidatesApi->api_candidates_post: %s\n" % e)
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

