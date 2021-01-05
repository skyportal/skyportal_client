# Spectrum

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wavelengths** | **[float]** | Wavelengths of the spectrum [Angstrom]. | 
**fluxes** | **[float]** | Flux of the Spectrum [F_lambda, arbitrary units]. | 
**obj_id** | **str** | ID of this Spectrum&#39;s Obj. | 
**observed_at** | **datetime** | Median UTC ISO time stamp of the exposure or exposures in which the Spectrum was acquired. | 
**instrument_id** | **int** | ID of the Instrument that acquired the Spectrum. | 
**owner_id** | **int** | ID of the User who uploaded the spectrum. | 
**id** | **int** | Unique object identifier. | [optional] 
**errors** | **[float], none_type** | Errors on the fluxes of the spectrum [F_lambda, same units as &#x60;fluxes&#x60;.] | [optional] 
**origin** | **str, none_type** | Origin of the spectrum. | [optional] 
**followup_request_id** | **int, none_type** |  | [optional] 
**assignment_id** | **int, none_type** |  | [optional] 
**altdata** | **bool, date, datetime, dict, float, int, list, str, none_type** | Miscellaneous alternative metadata. | [optional] 
**original_file_string** | **str, none_type** | Content of original file that was passed to upload the spectrum. | [optional] 
**original_file_filename** | **str, none_type** | Original file name that was passed to upload the spectrum. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


