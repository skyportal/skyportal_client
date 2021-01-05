# PhotometryFlux

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **int** | ID of the instrument with which the observation was carried out. | 
**filter** | **str** | The bandpass of the observation. | 
**fluxerr** | **float** | Gaussian error on the flux in counts. | 
**mjd** | **float** | MJD of the observation. | 
**zp** | **float** | Magnitude zeropoint, given by &#x60;ZP&#x60; in the equation m &#x3D; -2.5 log10(flux) + &#x60;ZP&#x60;. m is the magnitude of the object in the magnitude system &#x60;magsys&#x60;. | 
**obj_id** | **str** | ID of the Object to which the photometry will be attached. | 
**magsys** | **str** | The magnitude system to which the flux and the zeropoint are tied. | 
**ra** | **float, none_type** | ICRS Right Ascension of the centroid of the photometric aperture [deg]. | [optional] 
**dec_unc** | **float, none_type** | Uncertainty on dec [arcsec]. | [optional] 
**altdata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Misc. alternative metadata stored in JSON format, e.g. &#x60;{&#39;calibration&#39;: {&#39;source&#39;: &#39;ps1&#39;, &#39;color_term&#39;: 0.012}, &#39;photometry_method&#39;: &#39;allstar&#39;, &#39;method_reference&#39;: &#39;Masci et al. (2015)&#39;}&#x60; | [optional] 
**assignment_id** | **int, none_type** | ID of the classical assignment which generated the photometry | [optional] 
**flux** | **float, none_type** | Flux of the observation in counts. Can be null to accommodate upper limits from ZTF1, where no flux is measured for non-detections. If flux is null, the flux error is used to derive a limiting magnitude. | [optional] 
**dec** | **float, none_type** | ICRS Declination of the centroid of the photometric aperture [deg]. | [optional] 
**alert_id** | **int, none_type** | Corresponding alert ID. If a record is already present with identical alert ID, only the groups list will be updated (other alert data assumed identical). Defaults to None. | [optional] 
**ra_unc** | **float, none_type** | Uncertainty on RA [arcsec]. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


