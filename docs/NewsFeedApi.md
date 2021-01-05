# skyportal_client.NewsFeedApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_newsfeed_get**](NewsFeedApi.md#api_newsfeed_get) | **GET** /api/newsfeed | 


# **api_newsfeed_get**
> object api_newsfeed_get()



Retrieve summary of recent activity

### Example

```python
import time
import skyportal_client
from skyportal_client.api import news_feed_api
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
    api_instance = news_feed_api.NewsFeedApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_newsfeed_get()
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling NewsFeedApi->api_newsfeed_get: %s\n" % e)
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
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

