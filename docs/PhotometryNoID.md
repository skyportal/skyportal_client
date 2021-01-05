# PhotometryNoID

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mjd** | **float** | MJD of the observation. | 
**fluxerr** | **float** | Gaussian error on the flux in µJy. | 
**filter** | **str** | Filter with which the observation was taken. | 
**obj_id** | **str** | ID of the Photometry&#39;s Obj. | 
**instrument_id** | **int** | ID of the Instrument that took this Photometry. | 
**ra** | **float, none_type** |  | [optional] 
**dec** | **float, none_type** |  | [optional] 
**flux** | **float** | Flux of the observation in µJy. Corresponds to an AB Zeropoint of 23.9 in all filters. | [optional] 
**ra_unc** | **float, none_type** | Uncertainty of ra position [arcsec] | [optional] 
**dec_unc** | **float, none_type** | Uncertainty of dec position [arcsec] | [optional] 
**original_user_data** | **bool, date, datetime, dict, float, int, list, str, none_type** | Original data passed by the user through the PhotometryHandler.POST API or the PhotometryHandler.PUT API. The schema of this JSON validates under either schema.PhotometryFlux or schema.PhotometryMag (depending on how the data was passed). | [optional] 
**altdata** | **bool, date, datetime, dict, float, int, list, str, none_type** | Arbitrary metadata in JSON format.. | [optional] 
**upload_id** | **str** | ID of the batch in which this Photometry was uploaded (for bulk deletes). | [optional] 
**origin** | **str** | Origin from which this Photometry was extracted (if any). | [optional] 
**followup_request_id** | **int, none_type** |  | [optional] 
**assignment_id** | **int, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


