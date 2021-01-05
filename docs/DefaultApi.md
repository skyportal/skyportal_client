# skyportal_client.DefaultApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_alerts_ztf_object_id_aux_get**](DefaultApi.md#api_alerts_ztf_object_id_aux_get) | **GET** /api/alerts/ztf/objectId/aux | 
[**api_alerts_ztf_object_id_aux_post**](DefaultApi.md#api_alerts_ztf_object_id_aux_post) | **POST** /api/alerts/ztf/objectId/aux | 
[**api_alerts_ztf_object_id_cutout_post**](DefaultApi.md#api_alerts_ztf_object_id_cutout_post) | **POST** /api/alerts/ztf/objectId/cutout | 
[**api_alerts_ztf_object_id_get**](DefaultApi.md#api_alerts_ztf_object_id_get) | **GET** /api/alerts/ztf/objectId | 
[**api_alerts_ztf_object_id_post**](DefaultApi.md#api_alerts_ztf_object_id_post) | **POST** /api/alerts/ztf/objectId | 
[**api_filters_filter_id_v_delete**](DefaultApi.md#api_filters_filter_id_v_delete) | **DELETE** /api/filters/filter_id/v | 
[**api_filters_filter_id_v_get**](DefaultApi.md#api_filters_filter_id_v_get) | **GET** /api/filters/filter_id/v | 
[**api_filters_filter_id_v_patch**](DefaultApi.md#api_filters_filter_id_v_patch) | **PATCH** /api/filters/filter_id/v | 
[**api_filters_filter_id_v_post**](DefaultApi.md#api_filters_filter_id_v_post) | **POST** /api/filters/filter_id/v | 


# **api_alerts_ztf_object_id_aux_get**
> Success api_alerts_ztf_object_id_aux_get(object_id)



Retrieve aux data for an objectId from Kowalski

### Example

```python
import time
import skyportal_client
from skyportal_client.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    object_id = "objectId_example" # str | 
    include_prv_candidates = True # bool |  (optional)
    include_all_fields = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_alerts_ztf_object_id_aux_get(object_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling DefaultApi->api_alerts_ztf_object_id_aux_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_alerts_ztf_object_id_aux_get(object_id, include_prv_candidates=include_prv_candidates, include_all_fields=include_all_fields)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling DefaultApi->api_alerts_ztf_object_id_aux_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**|  |
 **include_prv_candidates** | **bool**|  | [optional]
 **include_all_fields** | **bool**|  | [optional]

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
**200** | retrieval failed |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_alerts_ztf_object_id_aux_post**
> Success api_alerts_ztf_object_id_aux_post()



Save ZTF objectId from Kowalski as source in SkyPortal

### Example

```python
import time
import skyportal_client
from skyportal_client.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    unknown_base_type =  # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_alerts_ztf_object_id_aux_post(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling DefaultApi->api_alerts_ztf_object_id_aux_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **api_alerts_ztf_object_id_cutout_post**
> Success api_alerts_ztf_object_id_cutout_post()



Save ZTF objectId from Kowalski as source in SkyPortal

### Example

```python
import time
import skyportal_client
from skyportal_client.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    unknown_base_type =  # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_alerts_ztf_object_id_cutout_post(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling DefaultApi->api_alerts_ztf_object_id_cutout_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **api_alerts_ztf_object_id_get**
> object api_alerts_ztf_object_id_get(object_id)



Retrieve a ZTF objectId from Kowalski

### Example

```python
import time
import skyportal_client
from skyportal_client.api import default_api
from skyportal_client.model.int import Int
from skyportal_client.model.error import Error
from skyportal_client.model.str import Str
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    object_id =  # Str | 
    candid =  # Int |  (optional)
    include_all_fields = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_alerts_ztf_object_id_get(object_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling DefaultApi->api_alerts_ztf_object_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_alerts_ztf_object_id_get(object_id, candid=candid, include_all_fields=include_all_fields)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling DefaultApi->api_alerts_ztf_object_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **Str**|  |
 **candid** | **Int**|  | [optional]
 **include_all_fields** | **bool**|  | [optional]

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
**200** | retrieved alert(s) |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_alerts_ztf_object_id_post**
> Success api_alerts_ztf_object_id_post()



Save ZTF objectId from Kowalski as source in SkyPortal

### Example

```python
import time
import skyportal_client
from skyportal_client.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    unknown_base_type =  # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_alerts_ztf_object_id_post(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling DefaultApi->api_alerts_ztf_object_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **api_filters_filter_id_v_delete**
> Success api_filters_filter_id_v_delete(filter_id)



Delete a filter

### Example

```python
import time
import skyportal_client
from skyportal_client.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    filter_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_filters_filter_id_v_delete(filter_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling DefaultApi->api_filters_filter_id_v_delete: %s\n" % e)
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

# **api_filters_filter_id_v_get**
> InlineResponse200 api_filters_filter_id_v_get(filter_id)



Retrieve a filter as stored on Kowalski

### Example

```python
import time
import skyportal_client
from skyportal_client.api import default_api
from skyportal_client.model.error import Error
from skyportal_client.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_filters_filter_id_v_get(filter_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling DefaultApi->api_filters_filter_id_v_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **int**|  |

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **api_filters_filter_id_v_patch**
> Success api_filters_filter_id_v_patch(filter_id)



Update a filter on Kowalski

### Example

```python
import time
import skyportal_client
from skyportal_client.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    filter_id = 1 # int | 
    unknown_base_type =  # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_filters_filter_id_v_patch(filter_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling DefaultApi->api_filters_filter_id_v_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_filters_filter_id_v_patch(filter_id, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling DefaultApi->api_filters_filter_id_v_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **int**|  |
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

# **api_filters_filter_id_v_post**
> object api_filters_filter_id_v_post()



POST a new filter version.

### Example

```python
import time
import skyportal_client
from skyportal_client.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    filter_no_id = FilterNoID(
        name="name_example",
        stream_id=1,
        group_id=1,
    ) # FilterNoID |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_filters_filter_id_v_post(filter_no_id=filter_no_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling DefaultApi->api_filters_filter_id_v_post: %s\n" % e)
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

