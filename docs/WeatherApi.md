# skyportal_client.WeatherApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_weather_get**](WeatherApi.md#api_weather_get) | **GET** /api/weather | 


# **api_weather_get**
> object api_weather_get()



Retrieve weather at the telescope site saved by user

### Example

```python
import time
import skyportal_client
from skyportal_client.api import weather_api
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = weather_api.WeatherApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_weather_get()
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling WeatherApi->api_weather_get: %s\n" % e)
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

