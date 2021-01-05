# skyportal_client.LabApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_alerts_ztf_object_id_cutout_get**](LabApi.md#api_alerts_ztf_object_id_cutout_get) | **GET** /api/alerts/ztf/objectId/cutout | Serve ZTF alert cutout as fits or png


# **api_alerts_ztf_object_id_cutout_get**
> file_type api_alerts_ztf_object_id_cutout_get(candid, cutout, file_format)

Serve ZTF alert cutout as fits or png

### Example

```python
import time
import skyportal_client
from skyportal_client.api import lab_api
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
    api_instance = lab_api.LabApi(api_client)
    candid = 1 # int | ZTF alert candid
    cutout = "science" # str | retrieve science, template, or difference cutout image?
    file_format = "fits" # str | response file format: original loss-less FITS or rendered png
    interval = "min_max" # str | Interval to use when rendering png (optional)
    stretch = "linear" # str | Stretch to use when rendering png (optional)
    cmap = "bone" # str | Color map to use when rendering png (optional)

    # example passing only required values which don't have defaults set
    try:
        # Serve ZTF alert cutout as fits or png
        api_response = api_instance.api_alerts_ztf_object_id_cutout_get(candid, cutout, file_format)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling LabApi->api_alerts_ztf_object_id_cutout_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Serve ZTF alert cutout as fits or png
        api_response = api_instance.api_alerts_ztf_object_id_cutout_get(candid, cutout, file_format, interval=interval, stretch=stretch, cmap=cmap)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling LabApi->api_alerts_ztf_object_id_cutout_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **candid** | **int**| ZTF alert candid |
 **cutout** | **str**| retrieve science, template, or difference cutout image? |
 **file_format** | **str**| response file format: original loss-less FITS or rendered png |
 **interval** | **str**| Interval to use when rendering png | [optional]
 **stretch** | **str**| Stretch to use when rendering png | [optional]
 **cmap** | **str**| Color map to use when rendering png | [optional]

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/fits, image/png, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | retrieved cutout |  -  |
**400** | retrieval failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

