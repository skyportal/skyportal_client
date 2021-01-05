# skyportal_client.InstrumentsApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_instrument_get**](InstrumentsApi.md#api_instrument_get) | **GET** /api/instrument | 
[**api_instrument_instrument_id_delete**](InstrumentsApi.md#api_instrument_instrument_id_delete) | **DELETE** /api/instrument/instrument_id | 
[**api_instrument_instrument_id_get**](InstrumentsApi.md#api_instrument_instrument_id_get) | **GET** /api/instrument/instrument_id | 
[**api_instrument_instrument_id_put**](InstrumentsApi.md#api_instrument_instrument_id_put) | **PUT** /api/instrument/instrument_id | 
[**api_instrument_post**](InstrumentsApi.md#api_instrument_post) | **POST** /api/instrument | 


# **api_instrument_get**
> ArrayOfInstruments api_instrument_get()



Retrieve all instruments

### Example

```python
import time
import skyportal_client
from skyportal_client.api import instruments_api
from skyportal_client.model.error import Error
from skyportal_client.model.array_of_instruments import ArrayOfInstruments
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instruments_api.InstrumentsApi(api_client)
    name = "name_example" # str | Filter by name (exact match) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_instrument_get(name=name)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling InstrumentsApi->api_instrument_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter by name (exact match) | [optional]

### Return type

[**ArrayOfInstruments**](ArrayOfInstruments.md)

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

# **api_instrument_instrument_id_delete**
> Success api_instrument_instrument_id_delete(instrument_id)



Delete an instrument

### Example

```python
import time
import skyportal_client
from skyportal_client.api import instruments_api
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
    api_instance = instruments_api.InstrumentsApi(api_client)
    instrument_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_instrument_instrument_id_delete(instrument_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling InstrumentsApi->api_instrument_instrument_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_id** | **int**|  |

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

# **api_instrument_instrument_id_get**
> SingleInstrument api_instrument_instrument_id_get(instrument_id)



Retrieve an instrument

### Example

```python
import time
import skyportal_client
from skyportal_client.api import instruments_api
from skyportal_client.model.error import Error
from skyportal_client.model.single_instrument import SingleInstrument
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instruments_api.InstrumentsApi(api_client)
    instrument_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_instrument_instrument_id_get(instrument_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling InstrumentsApi->api_instrument_instrument_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_id** | **int**|  |

### Return type

[**SingleInstrument**](SingleInstrument.md)

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

# **api_instrument_instrument_id_put**
> Success api_instrument_instrument_id_put(instrument_id)



Update instrument

### Example

```python
import time
import skyportal_client
from skyportal_client.api import instruments_api
from skyportal_client.model.error import Error
from skyportal_client.model.success import Success
from skyportal_client.model.instrument_no_id import InstrumentNoID
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instruments_api.InstrumentsApi(api_client)
    instrument_id = 1 # int | 
    instrument_no_id = InstrumentNoID(
        name="name_example",
        type="imager",
        band="band_example",
        telescope_id=1,
        filters=[
            None,
        ],
        api_classname="SEDMAPI",
        listener_classname="SEDMListener",
    ) # InstrumentNoID |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_instrument_instrument_id_put(instrument_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling InstrumentsApi->api_instrument_instrument_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_instrument_instrument_id_put(instrument_id, instrument_no_id=instrument_no_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling InstrumentsApi->api_instrument_instrument_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_id** | **int**|  |
 **instrument_no_id** | [**InstrumentNoID**](InstrumentNoID.md)|  | [optional]

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

# **api_instrument_post**
> object api_instrument_post()



Add a new instrument

### Example

```python
import time
import skyportal_client
from skyportal_client.api import instruments_api
from skyportal_client.model.unknownbasetype import UNKNOWNBASETYPE
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
    api_instance = instruments_api.InstrumentsApi(api_client)
    unknown_base_type =  # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_instrument_post(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling InstrumentsApi->api_instrument_post: %s\n" % e)
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
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

