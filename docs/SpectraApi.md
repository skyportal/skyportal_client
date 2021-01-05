# skyportal_client.SpectraApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sources_obj_id_spectra_get**](SpectraApi.md#api_sources_obj_id_spectra_get) | **GET** /api/sources/obj_id/spectra | 
[**api_spectrum_ascii_post**](SpectraApi.md#api_spectrum_ascii_post) | **POST** /api/spectrum/ascii | 
[**api_spectrum_parse_ascii_post**](SpectraApi.md#api_spectrum_parse_ascii_post) | **POST** /api/spectrum/parse/ascii | 
[**api_spectrum_post**](SpectraApi.md#api_spectrum_post) | **POST** /api/spectrum | 
[**api_spectrum_range_get**](SpectraApi.md#api_spectrum_range_get) | **GET** /api/spectrum/range | 
[**api_spectrum_spectrum_id_delete**](SpectraApi.md#api_spectrum_spectrum_id_delete) | **DELETE** /api/spectrum/spectrum_id | 
[**api_spectrum_spectrum_id_get**](SpectraApi.md#api_spectrum_spectrum_id_get) | **GET** /api/spectrum/spectrum_id | 
[**api_spectrum_spectrum_id_put**](SpectraApi.md#api_spectrum_spectrum_id_put) | **PUT** /api/spectrum/spectrum_id | 


# **api_sources_obj_id_spectra_get**
> object api_sources_obj_id_spectra_get(obj_id)



Retrieve all spectra associated with an Object

### Example

```python
import time
import skyportal_client
from skyportal_client.api import spectra_api
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
    api_instance = spectra_api.SpectraApi(api_client)
    obj_id = "obj_id_example" # str | ID of the object to retrieve spectra for
    normalization = "normalization_example" # str | what normalization is needed for the spectra (e.g., \"median\"). If omitted, returns the original spectrum. Options for normalization are: - median: normalize the flux to have median==1  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_sources_obj_id_spectra_get(obj_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SpectraApi->api_sources_obj_id_spectra_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_sources_obj_id_spectra_get(obj_id, normalization=normalization)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SpectraApi->api_sources_obj_id_spectra_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obj_id** | **str**| ID of the object to retrieve spectra for |
 **normalization** | **str**| what normalization is needed for the spectra (e.g., \&quot;median\&quot;). If omitted, returns the original spectrum. Options for normalization are: - median: normalize the flux to have median&#x3D;&#x3D;1  | [optional]

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

# **api_spectrum_ascii_post**
> object api_spectrum_ascii_post()



Upload spectrum from ASCII file

### Example

```python
import time
import skyportal_client
from skyportal_client.api import spectra_api
from skyportal_client.model.spectrum_ascii_file_post_json import SpectrumAsciiFilePostJSON
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
    api_instance = spectra_api.SpectraApi(api_client)
    spectrum_ascii_file_post_json = SpectrumAsciiFilePostJSON(
        instrument_id=1,
        reduced_by=[],
        filename="filename_example",
        assignment_id=1,
        fluxerr_column=1,
        observed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        group_ids=[
            1,
        ],
        followup_request_id=1,
        wave_column=0,
        obj_id="obj_id_example",
        observed_by=[],
        flux_column=1,
        ascii="ascii_example",
    ) # SpectrumAsciiFilePostJSON |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_spectrum_ascii_post(spectrum_ascii_file_post_json=spectrum_ascii_file_post_json)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SpectraApi->api_spectrum_ascii_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spectrum_ascii_file_post_json** | [**SpectrumAsciiFilePostJSON**](SpectrumAsciiFilePostJSON.md)|  | [optional]

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

# **api_spectrum_parse_ascii_post**
> SpectrumNoID api_spectrum_parse_ascii_post()



Parse spectrum from ASCII file

### Example

```python
import time
import skyportal_client
from skyportal_client.api import spectra_api
from skyportal_client.model.error import Error
from skyportal_client.model.spectrum_no_id import SpectrumNoID
from skyportal_client.model.spectrum_ascii_file_parse_json import SpectrumAsciiFileParseJSON
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = spectra_api.SpectraApi(api_client)
    spectrum_ascii_file_parse_json = SpectrumAsciiFileParseJSON(
        fluxerr_column=1,
        ascii="ascii_example",
        flux_column=1,
        wave_column=0,
    ) # SpectrumAsciiFileParseJSON |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_spectrum_parse_ascii_post(spectrum_ascii_file_parse_json=spectrum_ascii_file_parse_json)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SpectraApi->api_spectrum_parse_ascii_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spectrum_ascii_file_parse_json** | [**SpectrumAsciiFileParseJSON**](SpectrumAsciiFileParseJSON.md)|  | [optional]

### Return type

[**SpectrumNoID**](SpectrumNoID.md)

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

# **api_spectrum_post**
> object api_spectrum_post()



Upload spectrum

### Example

```python
import time
import skyportal_client
from skyportal_client.api import spectra_api
from skyportal_client.model.error import Error
from skyportal_client.model.spectrum_post import SpectrumPost
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = spectra_api.SpectraApi(api_client)
    spectrum_post = SpectrumPost(
        instrument_id=1,
        reduced_by=[],
        errors=[
            3.14,
        ],
        altdata=None,
        assignment_id=1,
        origin="origin_example",
        wavelengths=[
            3.14,
        ],
        observed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        group_ids=None,
        fluxes=[
            3.14,
        ],
        obj_id="obj_id_example",
        observed_by=[],
        followup_request_id=1,
    ) # SpectrumPost |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_spectrum_post(spectrum_post=spectrum_post)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SpectraApi->api_spectrum_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spectrum_post** | [**SpectrumPost**](SpectrumPost.md)|  | [optional]

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

# **api_spectrum_range_get**
> object api_spectrum_range_get()



Retrieve spectra for given instrument within date range

### Example

```python
import time
import skyportal_client
from skyportal_client.api import spectra_api
from skyportal_client.model.isoutc_date_string import ISOUTCDateString
from skyportal_client.model.error import Error
from skyportal_client.model.list_of_integers import ListOfIntegers
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = spectra_api.SpectraApi(api_client)
    instrument_ids =  # ListOfIntegers | Instrument id numbers of spectrum.  If None, retrieve for all instruments.  (optional)
    min_date =  # ISOUTCDateString | Minimum UTC date of range in ISOT format.  If None, open ended range.  (optional)
    max_date =  # ISOUTCDateString | Maximum UTC date of range in ISOT format. If None, open ended range.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_spectrum_range_get(instrument_ids=instrument_ids, min_date=min_date, max_date=max_date)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SpectraApi->api_spectrum_range_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_ids** | **ListOfIntegers**| Instrument id numbers of spectrum.  If None, retrieve for all instruments.  | [optional]
 **min_date** | **ISOUTCDateString**| Minimum UTC date of range in ISOT format.  If None, open ended range.  | [optional]
 **max_date** | **ISOUTCDateString**| Maximum UTC date of range in ISOT format. If None, open ended range.  | [optional]

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

# **api_spectrum_spectrum_id_delete**
> Success api_spectrum_spectrum_id_delete(spectrum_id)



Delete a spectrum

### Example

```python
import time
import skyportal_client
from skyportal_client.api import spectra_api
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
    api_instance = spectra_api.SpectraApi(api_client)
    spectrum_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_spectrum_spectrum_id_delete(spectrum_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SpectraApi->api_spectrum_spectrum_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spectrum_id** | **int**|  |

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

# **api_spectrum_spectrum_id_get**
> SingleSpectrum api_spectrum_spectrum_id_get(spectrum_id)



Retrieve a spectrum

### Example

```python
import time
import skyportal_client
from skyportal_client.api import spectra_api
from skyportal_client.model.error import Error
from skyportal_client.model.single_spectrum import SingleSpectrum
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = spectra_api.SpectraApi(api_client)
    spectrum_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_spectrum_spectrum_id_get(spectrum_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SpectraApi->api_spectrum_spectrum_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spectrum_id** | **int**|  |

### Return type

[**SingleSpectrum**](SingleSpectrum.md)

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

# **api_spectrum_spectrum_id_put**
> Success api_spectrum_spectrum_id_put(spectrum_id)



Update spectrum

### Example

```python
import time
import skyportal_client
from skyportal_client.api import spectra_api
from skyportal_client.model.error import Error
from skyportal_client.model.success import Success
from skyportal_client.model.spectrum_post import SpectrumPost
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = spectra_api.SpectraApi(api_client)
    spectrum_id = 1 # int | 
    spectrum_post = SpectrumPost(
        instrument_id=1,
        reduced_by=[],
        errors=[
            3.14,
        ],
        altdata=None,
        assignment_id=1,
        origin="origin_example",
        wavelengths=[
            3.14,
        ],
        observed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        group_ids=None,
        fluxes=[
            3.14,
        ],
        obj_id="obj_id_example",
        observed_by=[],
        followup_request_id=1,
    ) # SpectrumPost |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_spectrum_spectrum_id_put(spectrum_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SpectraApi->api_spectrum_spectrum_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_spectrum_spectrum_id_put(spectrum_id, spectrum_post=spectrum_post)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SpectraApi->api_spectrum_spectrum_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spectrum_id** | **int**|  |
 **spectrum_post** | [**SpectrumPost**](SpectrumPost.md)|  | [optional]

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

