# skyportal_client.TelescopesApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_telescope_get**](TelescopesApi.md#api_telescope_get) | **GET** /api/telescope | 
[**api_telescope_post**](TelescopesApi.md#api_telescope_post) | **POST** /api/telescope | 
[**api_telescope_telescope_id_delete**](TelescopesApi.md#api_telescope_telescope_id_delete) | **DELETE** /api/telescope/telescope_id | 
[**api_telescope_telescope_id_get**](TelescopesApi.md#api_telescope_telescope_id_get) | **GET** /api/telescope/telescope_id | 
[**api_telescope_telescope_id_put**](TelescopesApi.md#api_telescope_telescope_id_put) | **PUT** /api/telescope/telescope_id | 
[**api_weather_get**](TelescopesApi.md#api_weather_get) | **GET** /api/weather | 


# **api_telescope_get**
> ArrayOfTelescopes api_telescope_get()



Retrieve all telescopes

### Example

```python
import time
import skyportal_client
from skyportal_client.api import telescopes_api
from skyportal_client.model.array_of_telescopes import ArrayOfTelescopes
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
    api_instance = telescopes_api.TelescopesApi(api_client)
    name = "name_example" # str | Filter by name (exact match) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_telescope_get(name=name)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling TelescopesApi->api_telescope_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter by name (exact match) | [optional]

### Return type

[**ArrayOfTelescopes**](ArrayOfTelescopes.md)

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

# **api_telescope_post**
> object api_telescope_post()



Create telescopes

### Example

```python
import time
import skyportal_client
from skyportal_client.api import telescopes_api
from skyportal_client.model.error import Error
from skyportal_client.model.telescope_no_id import TelescopeNoID
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = telescopes_api.TelescopesApi(api_client)
    telescope_no_id = TelescopeNoID(
        name="name_example",
        nickname="nickname_example",
        lat=3.14,
        lon=3.14,
        elevation=3.14,
        diameter=3.14,
        skycam_link="skycam_link_example",
        robotic=True,
        fixed_location=True,
        weather=None,
        weather_retrieved_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        weather_link="weather_link_example",
    ) # TelescopeNoID |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_telescope_post(telescope_no_id=telescope_no_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling TelescopesApi->api_telescope_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telescope_no_id** | [**TelescopeNoID**](TelescopeNoID.md)|  | [optional]

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

# **api_telescope_telescope_id_delete**
> Success api_telescope_telescope_id_delete(telescope_id)



Delete a telescope

### Example

```python
import time
import skyportal_client
from skyportal_client.api import telescopes_api
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
    api_instance = telescopes_api.TelescopesApi(api_client)
    telescope_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_telescope_telescope_id_delete(telescope_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling TelescopesApi->api_telescope_telescope_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telescope_id** | **int**|  |

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

# **api_telescope_telescope_id_get**
> SingleTelescope api_telescope_telescope_id_get(telescope_id)



Retrieve a telescope

### Example

```python
import time
import skyportal_client
from skyportal_client.api import telescopes_api
from skyportal_client.model.error import Error
from skyportal_client.model.single_telescope import SingleTelescope
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = telescopes_api.TelescopesApi(api_client)
    telescope_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_telescope_telescope_id_get(telescope_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling TelescopesApi->api_telescope_telescope_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telescope_id** | **int**|  |

### Return type

[**SingleTelescope**](SingleTelescope.md)

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

# **api_telescope_telescope_id_put**
> Success api_telescope_telescope_id_put(telescope_id)



Update telescope

### Example

```python
import time
import skyportal_client
from skyportal_client.api import telescopes_api
from skyportal_client.model.error import Error
from skyportal_client.model.success import Success
from skyportal_client.model.telescope_no_id import TelescopeNoID
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = telescopes_api.TelescopesApi(api_client)
    telescope_id = 1 # int | 
    telescope_no_id = TelescopeNoID(
        name="name_example",
        nickname="nickname_example",
        lat=3.14,
        lon=3.14,
        elevation=3.14,
        diameter=3.14,
        skycam_link="skycam_link_example",
        robotic=True,
        fixed_location=True,
        weather=None,
        weather_retrieved_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        weather_link="weather_link_example",
    ) # TelescopeNoID |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_telescope_telescope_id_put(telescope_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling TelescopesApi->api_telescope_telescope_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_telescope_telescope_id_put(telescope_id, telescope_no_id=telescope_no_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling TelescopesApi->api_telescope_telescope_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telescope_id** | **int**|  |
 **telescope_no_id** | [**TelescopeNoID**](TelescopeNoID.md)|  | [optional]

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

# **api_weather_get**
> object api_weather_get()



Retrieve weather at the telescope site saved by user

### Example

```python
import time
import skyportal_client
from skyportal_client.api import telescopes_api
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = telescopes_api.TelescopesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_weather_get()
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling TelescopesApi->api_weather_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

