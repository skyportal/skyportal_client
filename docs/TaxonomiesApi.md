# skyportal_client.TaxonomiesApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_taxonomy_get**](TaxonomiesApi.md#api_taxonomy_get) | **GET** /api/taxonomy | 
[**api_taxonomy_post**](TaxonomiesApi.md#api_taxonomy_post) | **POST** /api/taxonomy | 
[**api_taxonomy_taxonomy_id_delete**](TaxonomiesApi.md#api_taxonomy_taxonomy_id_delete) | **DELETE** /api/taxonomy/taxonomy_id | 
[**api_taxonomy_taxonomy_id_get**](TaxonomiesApi.md#api_taxonomy_taxonomy_id_get) | **GET** /api/taxonomy/taxonomy_id | 


# **api_taxonomy_get**
> ArrayOfTaxonomys api_taxonomy_get()



Get all the taxonomies

### Example

```python
import time
import skyportal_client
from skyportal_client.api import taxonomies_api
from skyportal_client.model.error import Error
from skyportal_client.model.array_of_taxonomys import ArrayOfTaxonomys
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = taxonomies_api.TaxonomiesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_taxonomy_get()
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling TaxonomiesApi->api_taxonomy_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArrayOfTaxonomys**](ArrayOfTaxonomys.md)

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

# **api_taxonomy_post**
> object api_taxonomy_post()



Post new taxonomy

### Example

```python
import time
import skyportal_client
from skyportal_client.api import taxonomies_api
from skyportal_client.model.inline_object18 import InlineObject18
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = taxonomies_api.TaxonomiesApi(api_client)
    inline_object18 = InlineObject18(
        name="name_example",
        hierarchy={},
        group_ids=[
            1,
        ],
        version="version_example",
        provenance="provenance_example",
        is_latest=True,
    ) # InlineObject18 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_taxonomy_post(inline_object18=inline_object18)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling TaxonomiesApi->api_taxonomy_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object18** | [**InlineObject18**](InlineObject18.md)|  | [optional]

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

# **api_taxonomy_taxonomy_id_delete**
> Success api_taxonomy_taxonomy_id_delete(taxonomy_id)



Delete a taxonomy

### Example

```python
import time
import skyportal_client
from skyportal_client.api import taxonomies_api
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
    api_instance = taxonomies_api.TaxonomiesApi(api_client)
    taxonomy_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_taxonomy_taxonomy_id_delete(taxonomy_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling TaxonomiesApi->api_taxonomy_taxonomy_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **int**|  |

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

# **api_taxonomy_taxonomy_id_get**
> SingleTaxonomy api_taxonomy_taxonomy_id_get(taxonomy_id)



Retrieve a taxonomy

### Example

```python
import time
import skyportal_client
from skyportal_client.api import taxonomies_api
from skyportal_client.model.single_taxonomy import SingleTaxonomy
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
    api_instance = taxonomies_api.TaxonomiesApi(api_client)
    taxonomy_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_taxonomy_taxonomy_id_get(taxonomy_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling TaxonomiesApi->api_taxonomy_taxonomy_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **int**|  |

### Return type

[**SingleTaxonomy**](SingleTaxonomy.md)

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

