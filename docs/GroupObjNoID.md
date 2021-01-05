# GroupObjNoID

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** |  | 
**obj_id** | **str** |  | 
**saved_by_id** | **int, none_type** | ID of the User that saved the Obj to its Group. | [optional] 
**saved_at** | **datetime** | ISO UTC time when the Obj was saved to its Group. | [optional] 
**active** | **bool, none_type** | Whether the Obj is still &#39;active&#39; as a Source in its Group. If this flag is set to False, the Source will not appear in the Group&#39;s sample. | [optional] 
**requested** | **bool, none_type** | True if the source has been shared with another Group, but not saved by the recipient Group. | [optional] 
**unsaved_by_id** | **int, none_type** | ID of the User who unsaved the Source. | [optional] 
**unsaved_at** | **datetime, none_type** | ISO UTC time when the Obj was unsaved from Group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


