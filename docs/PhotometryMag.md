# PhotometryMag

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **int** | ID of the instrument with which the observation was carried out. | 
**filter** | **str** | The bandpass of the observation. | 
**mjd** | **float** | MJD of the observation. | 
**limiting_mag** | **float** | Limiting magnitude of the image in the magnitude system &#x60;magsys&#x60;. | 
**obj_id** | **str** | ID of the Object to which the photometry will be attached. | 
**magsys** | **str** | The magnitude system to which the flux and the zeropoint are tied. | 
**ra** | **float, none_type** | ICRS Right Ascension of the centroid of the photometric aperture [deg]. | [optional] 
**dec_unc** | **float, none_type** | Uncertainty on dec [arcsec]. | [optional] 
**magerr** | **float, none_type** | Magnitude error of the observation in the magnitude system &#x60;magsys&#x60;. Can be null in the case of a non-detection. | [optional] 
**altdata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Misc. alternative metadata stored in JSON format, e.g. &#x60;{&#39;calibration&#39;: {&#39;source&#39;: &#39;ps1&#39;, &#39;color_term&#39;: 0.012}, &#39;photometry_method&#39;: &#39;allstar&#39;, &#39;method_reference&#39;: &#39;Masci et al. (2015)&#39;}&#x60; | [optional] 
**assignment_id** | **int, none_type** | ID of the classical assignment which generated the photometry | [optional] 
**mag** | **float, none_type** | Magnitude of the observation in the magnitude system &#x60;magsys&#x60;. Can be null in the case of a non-detection. | [optional] 
**dec** | **float, none_type** | ICRS Declination of the centroid of the photometric aperture [deg]. | [optional] 
**alert_id** | **int, none_type** | Corresponding alert ID. If a record is already present with identical alert ID, only the groups list will be updated (other alert data assumed identical). Defaults to None. | [optional] 
**ra_unc** | **float, none_type** | Uncertainty on RA [arcsec]. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


