# InlineObject2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_id** | **str** |  | 
**origin** | **str** | String describing the source of this information. Only one Annotation per origin is allowed, although each Annotation can have multiple fields. To add/change data, use the update method instead of trying to post another Annotation from this origin. Origin must be a non-empty string starting with an alphanumeric character or underscore. (it must match the regex: /^\\w+/)  | 
**data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**group_ids** | **[int]** | List of group IDs corresponding to which groups should be able to view annotation. Defaults to all of requesting user&#39;s groups.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


