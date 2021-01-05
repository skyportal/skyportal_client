# skyportal_client.DataSharingApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sharing_post**](DataSharingApi.md#api_sharing_post) | **POST** /api/sharing | 


# **api_sharing_post**
> Success api_sharing_post()



Share data with additional groups/users

### Example

```python
import time
import skyportal_client
from skyportal_client.api import data_sharing_api
from skyportal_client.model.success import Success
from skyportal_client.model.inline_object11 import InlineObject11
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_sharing_api.DataSharingApi(api_client)
    inline_object11 = InlineObject11(
        photometry_i_ds=[
            1,
        ],
        spectrum_i_ds=[
            1,
        ],
        group_i_ds=[
            1,
        ],
    ) # InlineObject11 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_sharing_post(inline_object11=inline_object11)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling DataSharingApi->api_sharing_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object11** | [**InlineObject11**](InlineObject11.md)|  | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

