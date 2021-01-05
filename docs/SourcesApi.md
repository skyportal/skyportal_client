# skyportal_client.SourcesApi

All URIs are relative to *https://fritz.science*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_source_groups_obj_id_patch**](SourcesApi.md#api_source_groups_obj_id_patch) | **PATCH** /api/source_groups/obj_id | 
[**api_source_groups_post**](SourcesApi.md#api_source_groups_post) | **POST** /api/source_groups | 
[**api_sources_get**](SourcesApi.md#api_sources_get) | **GET** /api/sources | 
[**api_sources_obj_id_delete**](SourcesApi.md#api_sources_obj_id_delete) | **DELETE** /api/sources/obj_id | 
[**api_sources_obj_id_finder_get**](SourcesApi.md#api_sources_obj_id_finder_get) | **GET** /api/sources/obj_id/finder | 
[**api_sources_obj_id_get**](SourcesApi.md#api_sources_obj_id_get) | **GET** /api/sources/obj_id | 
[**api_sources_obj_id_groups_get**](SourcesApi.md#api_sources_obj_id_groups_get) | **GET** /api/sources/obj_id/groups | 
[**api_sources_obj_id_head**](SourcesApi.md#api_sources_obj_id_head) | **HEAD** /api/sources/obj_id | 
[**api_sources_obj_id_offsets_get**](SourcesApi.md#api_sources_obj_id_offsets_get) | **GET** /api/sources/obj_id/offsets | 
[**api_sources_obj_id_patch**](SourcesApi.md#api_sources_obj_id_patch) | **PATCH** /api/sources/obj_id | 
[**api_sources_post**](SourcesApi.md#api_sources_post) | **POST** /api/sources | 


# **api_source_groups_obj_id_patch**
> Success api_source_groups_obj_id_patch(obj_id)



Update a Source table row

### Example

```python
import time
import skyportal_client
from skyportal_client.api import sources_api
from skyportal_client.model.inline_object14 import InlineObject14
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
    api_instance = sources_api.SourcesApi(api_client)
    obj_id = 1 # int | 
    inline_object14 = InlineObject14(
        group_id=1,
        active=True,
        requested=True,
    ) # InlineObject14 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_source_groups_obj_id_patch(obj_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SourcesApi->api_source_groups_obj_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_source_groups_obj_id_patch(obj_id, inline_object14=inline_object14)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SourcesApi->api_source_groups_obj_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obj_id** | **int**|  |
 **inline_object14** | [**InlineObject14**](InlineObject14.md)|  | [optional]

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

# **api_source_groups_post**
> Success api_source_groups_post()



Save or request group(s) to save source, and optionally unsave from group(s).

### Example

```python
import time
import skyportal_client
from skyportal_client.api import sources_api
from skyportal_client.model.inline_object13 import InlineObject13
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
    api_instance = sources_api.SourcesApi(api_client)
    inline_object13 = InlineObject13(
        obj_id="obj_id_example",
        invite_group_ids=[
            1,
        ],
        unsave_group_ids=[
            1,
        ],
    ) # InlineObject13 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_source_groups_post(inline_object13=inline_object13)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SourcesApi->api_source_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object13** | [**InlineObject13**](InlineObject13.md)|  | [optional]

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

# **api_sources_get**
> object api_sources_get()



Retrieve all sources

### Example

```python
import time
import skyportal_client
from skyportal_client.api import sources_api
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
    api_instance = sources_api.SourcesApi(api_client)
    ra = 3.14 # float | RA for spatial filtering (optional)
    dec = 3.14 # float | Declination for spatial filtering (optional)
    radius = 3.14 # float | Radius for spatial filtering if ra & dec are provided (optional)
    source_id = "sourceID_example" # str | Portion of ID to filter on (optional)
    simbad_class = "simbadClass_example" # str | Simbad class to filter on (optional)
    has_tn_sname = True # bool | If true, return only those matches with TNS names (optional)
    num_per_page = 1 # int | Number of sources to return per paginated request. Defaults to 100. Max 1000.  (optional)
    page_number = 1 # int | Page number for paginated query results. Defaults to 1 (optional)
    total_matches = 1 # int | Used only in the case of paginating query results - if provided, this allows for avoiding a potentially expensive query.count() call.  (optional)
    start_date = "startDate_example" # str | Arrow-parseable date string (e.g. 2020-01-01). If provided, filter by last_detected >= startDate  (optional)
    end_date = "endDate_example" # str | Arrow-parseable date string (e.g. 2020-01-01). If provided, filter by last_detected <= endDate  (optional)
    group_ids = [
        1,
    ] # [int] | If provided, filter only sources saved to one of these group IDs.  (optional)
    include_photometry = True # bool | Boolean indicating whether to include associated photometry. Defaults to false.  (optional)
    include_requested = True # bool | Boolean indicating whether to include requested saves. Defaults to false.  (optional)
    pending_only = True # bool | Boolean indicating whether to only include requested/pending saves. Defaults to false.  (optional)
    saved_before = "savedBefore_example" # str | Only return sources that were saved before this UTC datetime.  (optional)
    saved_after = "savedAfter_example" # str | Only return sources that were saved after this UTC datetime.  (optional)
    save_summary = True # bool | Boolean indicating whether to only return the source save information in the response (defaults to false). If true, the response will contain a list of dicts with the following schema under `response['data']['sources']`: ```     {       \"group_id\": 2,       \"created_at\": \"2020-11-13T22:11:25.910271\",       \"saved_by_id\": 1,       \"saved_at\": \"2020-11-13T22:11:25.910271\",       \"requested\": false,       \"unsaved_at\": null,       \"modified\": \"2020-11-13T22:11:25.910271\",       \"obj_id\": \"16fil\",       \"active\": true,       \"unsaved_by_id\": null     } ```  (optional)
    sort_by = "sortBy_example" # str | The field to sort by. Currently allowed options are [\"id\", \"ra\", \"dec\", \"redshift\", \"saved_at\"]  (optional)
    sort_order = "sortOrder_example" # str | The sort order - either \"asc\" or \"desc\". Defaults to \"asc\"  (optional)
    include_comments = True # bool | Boolean indicating whether to include comment metadata in response. Defaults to false.  (optional)
    include_spectrum_exists = True # bool | Boolean indicating whether to return if a source has a spectra. Defaults to false.  (optional)
    classifications = [
        "classifications_example",
    ] # [str] | Comma-separated string of \"taxonomy: classification\" pair(s) to filter for sources matching that/those classification(s), i.e. \"Sitewide Taxonomy: Type II, Sitewide Taxonomy: AGN\"  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_sources_get(ra=ra, dec=dec, radius=radius, source_id=source_id, simbad_class=simbad_class, has_tn_sname=has_tn_sname, num_per_page=num_per_page, page_number=page_number, total_matches=total_matches, start_date=start_date, end_date=end_date, group_ids=group_ids, include_photometry=include_photometry, include_requested=include_requested, pending_only=pending_only, saved_before=saved_before, saved_after=saved_after, save_summary=save_summary, sort_by=sort_by, sort_order=sort_order, include_comments=include_comments, include_spectrum_exists=include_spectrum_exists, classifications=classifications)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SourcesApi->api_sources_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ra** | **float**| RA for spatial filtering | [optional]
 **dec** | **float**| Declination for spatial filtering | [optional]
 **radius** | **float**| Radius for spatial filtering if ra &amp; dec are provided | [optional]
 **source_id** | **str**| Portion of ID to filter on | [optional]
 **simbad_class** | **str**| Simbad class to filter on | [optional]
 **has_tn_sname** | **bool**| If true, return only those matches with TNS names | [optional]
 **num_per_page** | **int**| Number of sources to return per paginated request. Defaults to 100. Max 1000.  | [optional]
 **page_number** | **int**| Page number for paginated query results. Defaults to 1 | [optional]
 **total_matches** | **int**| Used only in the case of paginating query results - if provided, this allows for avoiding a potentially expensive query.count() call.  | [optional]
 **start_date** | **str**| Arrow-parseable date string (e.g. 2020-01-01). If provided, filter by last_detected &gt;&#x3D; startDate  | [optional]
 **end_date** | **str**| Arrow-parseable date string (e.g. 2020-01-01). If provided, filter by last_detected &lt;&#x3D; endDate  | [optional]
 **group_ids** | **[int]**| If provided, filter only sources saved to one of these group IDs.  | [optional]
 **include_photometry** | **bool**| Boolean indicating whether to include associated photometry. Defaults to false.  | [optional]
 **include_requested** | **bool**| Boolean indicating whether to include requested saves. Defaults to false.  | [optional]
 **pending_only** | **bool**| Boolean indicating whether to only include requested/pending saves. Defaults to false.  | [optional]
 **saved_before** | **str**| Only return sources that were saved before this UTC datetime.  | [optional]
 **saved_after** | **str**| Only return sources that were saved after this UTC datetime.  | [optional]
 **save_summary** | **bool**| Boolean indicating whether to only return the source save information in the response (defaults to false). If true, the response will contain a list of dicts with the following schema under &#x60;response[&#39;data&#39;][&#39;sources&#39;]&#x60;: &#x60;&#x60;&#x60;     {       \&quot;group_id\&quot;: 2,       \&quot;created_at\&quot;: \&quot;2020-11-13T22:11:25.910271\&quot;,       \&quot;saved_by_id\&quot;: 1,       \&quot;saved_at\&quot;: \&quot;2020-11-13T22:11:25.910271\&quot;,       \&quot;requested\&quot;: false,       \&quot;unsaved_at\&quot;: null,       \&quot;modified\&quot;: \&quot;2020-11-13T22:11:25.910271\&quot;,       \&quot;obj_id\&quot;: \&quot;16fil\&quot;,       \&quot;active\&quot;: true,       \&quot;unsaved_by_id\&quot;: null     } &#x60;&#x60;&#x60;  | [optional]
 **sort_by** | **str**| The field to sort by. Currently allowed options are [\&quot;id\&quot;, \&quot;ra\&quot;, \&quot;dec\&quot;, \&quot;redshift\&quot;, \&quot;saved_at\&quot;]  | [optional]
 **sort_order** | **str**| The sort order - either \&quot;asc\&quot; or \&quot;desc\&quot;. Defaults to \&quot;asc\&quot;  | [optional]
 **include_comments** | **bool**| Boolean indicating whether to include comment metadata in response. Defaults to false.  | [optional]
 **include_spectrum_exists** | **bool**| Boolean indicating whether to return if a source has a spectra. Defaults to false.  | [optional]
 **classifications** | **[str]**| Comma-separated string of \&quot;taxonomy: classification\&quot; pair(s) to filter for sources matching that/those classification(s), i.e. \&quot;Sitewide Taxonomy: Type II, Sitewide Taxonomy: AGN\&quot;  | [optional]

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

# **api_sources_obj_id_delete**
> Success api_sources_obj_id_delete(obj_id, group_id)



Delete a source

### Example

```python
import time
import skyportal_client
from skyportal_client.api import sources_api
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
    api_instance = sources_api.SourcesApi(api_client)
    obj_id = "obj_id_example" # str | 
    group_id = "group_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_sources_obj_id_delete(obj_id, group_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SourcesApi->api_sources_obj_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obj_id** | **str**|  |
 **group_id** | **str**|  |

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

# **api_sources_obj_id_finder_get**
> file_type api_sources_obj_id_finder_get(obj_id)



Generate a PDF/PNG finding chart to aid in spectroscopy

### Example

```python
import time
import skyportal_client
from skyportal_client.api import sources_api
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
    api_instance = sources_api.SourcesApi(api_client)
    obj_id = "obj_id_example" # str | 
    imsize =  # float | Image size in arcmin (square) (optional)
    facility = "Keck" # str |  (optional)
    image_source = "desi" # str | Source of the image used in the finding chart (optional)
    use_ztfref = True # bool | Use ZTFref catalog for offset star positions, otherwise DR2  (optional)
    obstime = "obstime_example" # str | datetime of observation in isoformat (e.g. 2020-12-30T12:34:10)  (optional)
    type = "png" # str | output type  (optional)
    num_offset_stars = 0 # int | output desired number of offset stars [0,5] (default: 3)  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_sources_obj_id_finder_get(obj_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SourcesApi->api_sources_obj_id_finder_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_sources_obj_id_finder_get(obj_id, imsize=imsize, facility=facility, image_source=image_source, use_ztfref=use_ztfref, obstime=obstime, type=type, num_offset_stars=num_offset_stars)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SourcesApi->api_sources_obj_id_finder_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obj_id** | **str**|  |
 **imsize** | **float**| Image size in arcmin (square) | [optional]
 **facility** | **str**|  | [optional]
 **image_source** | **str**| Source of the image used in the finding chart | [optional]
 **use_ztfref** | **bool**| Use ZTFref catalog for offset star positions, otherwise DR2  | [optional]
 **obstime** | **str**| datetime of observation in isoformat (e.g. 2020-12-30T12:34:10)  | [optional]
 **type** | **str**| output type  | [optional]
 **num_offset_stars** | **int**| output desired number of offset stars [0,5] (default: 3)  | [optional]

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, image/png, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A PDF/PNG finding chart file |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sources_obj_id_get**
> SingleObj api_sources_obj_id_get(obj_id)



Retrieve a source

### Example

```python
import time
import skyportal_client
from skyportal_client.api import sources_api
from skyportal_client.model.error import Error
from skyportal_client.model.single_obj import SingleObj
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sources_api.SourcesApi(api_client)
    obj_id = "obj_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_sources_obj_id_get(obj_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SourcesApi->api_sources_obj_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obj_id** | **str**|  |

### Return type

[**SingleObj**](SingleObj.md)

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

# **api_sources_obj_id_groups_get**
> ArrayOfGroups api_sources_obj_id_groups_get(obj_id)



Retrieve basic info on Groups that an Obj is saved to

### Example

```python
import time
import skyportal_client
from skyportal_client.api import sources_api
from skyportal_client.model.array_of_groups import ArrayOfGroups
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
    api_instance = sources_api.SourcesApi(api_client)
    obj_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_sources_obj_id_groups_get(obj_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SourcesApi->api_sources_obj_id_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obj_id** | **int**|  |

### Return type

[**ArrayOfGroups**](ArrayOfGroups.md)

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

# **api_sources_obj_id_head**
> Success api_sources_obj_id_head(obj_id)



Check if a Source exists

### Example

```python
import time
import skyportal_client
from skyportal_client.api import sources_api
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
    api_instance = sources_api.SourcesApi(api_client)
    obj_id = "obj_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_sources_obj_id_head(obj_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SourcesApi->api_sources_obj_id_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obj_id** | **str**|  |

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
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sources_obj_id_offsets_get**
> object api_sources_obj_id_offsets_get(obj_id)



Retrieve offset stars to aid in spectroscopy

### Example

```python
import time
import skyportal_client
from skyportal_client.api import sources_api
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
    api_instance = sources_api.SourcesApi(api_client)
    obj_id = "obj_id_example" # str | 
    facility = "Keck" # str | Which facility to generate the starlist for (optional)
    num_offset_stars = 0 # int | Requested number of offset stars (set to zero to get starlist of just the source itself)  (optional)
    obstime = "obstime_example" # str | datetime of observation in isoformat (e.g. 2020-12-30T12:34:10)  (optional)
    use_ztfref = True # bool | Use ZTFref catalog for offset star positions, otherwise Gaia DR2  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_sources_obj_id_offsets_get(obj_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SourcesApi->api_sources_obj_id_offsets_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_sources_obj_id_offsets_get(obj_id, facility=facility, num_offset_stars=num_offset_stars, obstime=obstime, use_ztfref=use_ztfref)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SourcesApi->api_sources_obj_id_offsets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obj_id** | **str**|  |
 **facility** | **str**| Which facility to generate the starlist for | [optional]
 **num_offset_stars** | **int**| Requested number of offset stars (set to zero to get starlist of just the source itself)  | [optional]
 **obstime** | **str**| datetime of observation in isoformat (e.g. 2020-12-30T12:34:10)  | [optional]
 **use_ztfref** | **bool**| Use ZTFref catalog for offset star positions, otherwise Gaia DR2  | [optional]

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

# **api_sources_obj_id_patch**
> Success api_sources_obj_id_patch(obj_id)



Update a source

### Example

```python
import time
import skyportal_client
from skyportal_client.api import sources_api
from skyportal_client.model.obj_no_id import ObjNoID
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
    api_instance = sources_api.SourcesApi(api_client)
    obj_id = "obj_id_example" # str | 
    obj_no_id = ObjNoID(
        ra=3.14,
        dec=3.14,
        ra_dis=3.14,
        dec_dis=3.14,
        ra_err=3.14,
        dec_err=3.14,
        offset=3.14,
        redshift=3.14,
        redshift_history=None,
        altdata=None,
        dist_nearest_source=3.14,
        mag_nearest_source=3.14,
        e_mag_nearest_source=3.14,
        transient=True,
        varstar=True,
        is_roid=True,
        score=3.14,
        origin="origin_example",
        internal_key="internal_key_example",
        detect_photometry_count=1,
    ) # ObjNoID |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_sources_obj_id_patch(obj_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SourcesApi->api_sources_obj_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_sources_obj_id_patch(obj_id, obj_no_id=obj_no_id)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SourcesApi->api_sources_obj_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obj_id** | **str**|  |
 **obj_no_id** | [**ObjNoID**](ObjNoID.md)|  | [optional]

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

# **api_sources_post**
> object api_sources_post()



Add a new source

### Example

```python
import time
import skyportal_client
from skyportal_client.api import sources_api
from skyportal_client.model.unknownbasetype import UNKNOWNBASETYPE
from pprint import pprint
# Defining the host is optional and defaults to https://fritz.science
# See configuration.py for a list of all supported configuration parameters.
configuration = skyportal_client.Configuration(
    host = "https://fritz.science"
)


# Enter a context with an instance of the API client
with skyportal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sources_api.SourcesApi(api_client)
    unknown_base_type =  # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_sources_post(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except skyportal_client.ApiException as e:
        print("Exception when calling SourcesApi->api_sources_post: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

