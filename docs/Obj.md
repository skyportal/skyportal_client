# Obj

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Name of the object. | 
**ra** | **float, none_type** |  | [optional] 
**dec** | **float, none_type** |  | [optional] 
**ra_dis** | **float, none_type** | J2000 Right Ascension at discovery time [deg]. | [optional] 
**dec_dis** | **float, none_type** | J2000 Declination at discovery time [deg]. | [optional] 
**ra_err** | **float, none_type** | Error on J2000 Right Ascension at discovery time [deg]. | [optional] 
**dec_err** | **float, none_type** | Error on J2000 Declination at discovery time [deg]. | [optional] 
**offset** | **float, none_type** | Offset from nearest static object [arcsec]. | [optional] 
**redshift** | **float, none_type** | Redshift. | [optional] 
**redshift_history** | **bool, date, datetime, dict, float, int, list, str, none_type** | Record of who set which redshift values and when. | [optional] 
**altdata** | **bool, date, datetime, dict, float, int, list, str, none_type** | Misc. alternative metadata stored in JSON format, e.g. &#x60;{&#39;gaia&#39;: {&#39;info&#39;: {&#39;Teff&#39;: 5780}}}&#x60; | [optional] 
**dist_nearest_source** | **float, none_type** | Distance to the nearest Obj [arcsec]. | [optional] 
**mag_nearest_source** | **float, none_type** | Magnitude of the nearest Obj [AB]. | [optional] 
**e_mag_nearest_source** | **float, none_type** | Error on magnitude of the nearest Obj [mag]. | [optional] 
**transient** | **bool, none_type** | Boolean indicating whether the object is an astrophysical transient. | [optional] 
**varstar** | **bool, none_type** | Boolean indicating whether the object is a variable star. | [optional] 
**is_roid** | **bool, none_type** | Boolean indicating whether the object is a moving object. | [optional] 
**score** | **float, none_type** | Machine learning score. | [optional] 
**origin** | **str, none_type** | Origin of the object. | [optional] 
**internal_key** | **str** | Internal key used for secure websocket messaging. | [optional] 
**detect_photometry_count** | **int, none_type** | How many times the object was detected above :math:&#x60;S/N &#x3D; 5&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


