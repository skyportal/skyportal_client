# InlineObject9

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_email** | **str** |  | 
**group_i_ds** | **[int]** | List of IDs of groups invited user will be added to. If &#x60;streamIDs&#x60; is not provided, invited user will be given accesss to all streams associated with the groups specified by this field.  | 
**stream_i_ds** | **[int]** | List of IDs of streams invited user will be given access to. If not provided, user will be granted access to all streams associated with the groups specified by &#x60;groupIDs&#x60;.  | [optional] 
**group_admin** | **[bool]** | List of booleans indicating whether user should be granted admin status for respective specified group(s).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


