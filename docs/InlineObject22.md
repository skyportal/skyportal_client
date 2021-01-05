# InlineObject22

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**contact_email** | **str** |  | [optional] 
**oauth_uid** | **str** |  | [optional] 
**contact_phone** | **str** |  | [optional] 
**roles** | **[str]** | List of user roles. Defaults to &#x60;[Full user]&#x60;. Will be overridden by &#x60;groupIDsAndAdmin&#x60; on a per-group basis.  | [optional] 
**group_i_ds_and_admin** | **[list]** | Array of 2-element arrays &#x60;[groupID, admin]&#x60; where &#x60;groupID&#x60; is the ID of a group that the new user will be added to and &#x60;admin&#x60; is a boolean indicating whether they will be an admin in that group, e.g. &#x60;[[group_id_1, true], [group_id_2, false]]&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


