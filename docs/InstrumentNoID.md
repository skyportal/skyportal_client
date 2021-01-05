# InstrumentNoID

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Instrument name. | 
**type** | **str** | Instrument type, one of Imager, Spectrograph, or Imaging Spectrograph. | 
**telescope_id** | **int** | The ID of the Telescope that hosts the Instrument. | 
**band** | **str, none_type** | The spectral band covered by the instrument (e.g., Optical, IR). | [optional] 
**filters** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | List of filters on the instrument (if any). | [optional] 
**api_classname** | **str, none_type** | Name of the instrument&#39;s API class. | [optional]  if omitted the server will use the default value of "SEDMAPI"
**listener_classname** | **str, none_type** | Name of the instrument&#39;s listener class. | [optional]  if omitted the server will use the default value of "SEDMListener"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


