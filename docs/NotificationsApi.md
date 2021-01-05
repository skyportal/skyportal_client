# skyportal_client.NotificationsApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_source_notifications_post**](NotificationsApi.md#api_source_notifications_post) | **POST** /api/source_notifications | 


# **api_source_notifications_post**
> object api_source_notifications_post()



Send out a new source notification

### Example

```python
import time
import skyportal_client
from skyportal_client.api import notifications_api
from skyportal_client.model.inline_object12 import InlineObject12
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = notifications_api.NotificationsApi(api_client)
    inline_object12 = InlineObject12(
        additional_notes="additional_notes_example",
        group_ids=[
            1,
        ],
        source_id="source_id_example",
        level="level_example",
    ) # InlineObject12 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_source_notifications_post(inline_object12=inline_object12)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling NotificationsApi->api_source_notifications_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object12** | [**InlineObject12**](InlineObject12.md)|  | [optional]

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

