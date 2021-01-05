# SpectrumPost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **int** | ID of the Instrument that acquired the Spectrum. | 
**wavelengths** | **[float]** | Wavelengths of the spectrum [Angstrom]. | 
**observed_at** | **datetime** | The ISO UTC time the spectrum was taken. | 
**fluxes** | **[float]** | Flux of the Spectrum [F_lambda, arbitrary units]. | 
**obj_id** | **str** | ID of this Spectrum&#39;s Obj. | 
**reduced_by** | **[int]** | IDs of the Users who reduced this Spectrum. | [optional]  if omitted the server will use the default value of []
**errors** | **[float]** | Errors on the fluxes of the spectrum [F_lambda, same units as &#x60;fluxes&#x60;.] | [optional] 
**altdata** | **bool, date, datetime, dict, float, int, list, str, none_type** | Miscellaneous alternative metadata. | [optional] 
**assignment_id** | **int** | ID of the classical assignment that generated this spectrum, if any. | [optional] 
**origin** | **str** | Origin of the spectrum. | [optional] 
**group_ids** | **bool, date, datetime, dict, float, int, list, str, none_type** | IDs of the Groups to share this spectrum with. Set to \&quot;all\&quot; to make this spectrum visible to all users. | [optional] 
**observed_by** | **[int]** | IDs of the Users who observed this Spectrum. | [optional]  if omitted the server will use the default value of []
**followup_request_id** | **int** | ID of the Followup request that generated this spectrum, if any. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


