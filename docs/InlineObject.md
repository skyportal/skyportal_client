# InlineObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_id** | **str** |  | 
**classification** | **str** |  | 
**taxonomy_id** | **int** |  | 
**probability** | **float, none_type** | User-assigned probability of this classification on this taxonomy. If multiple classifications are given for the same source by the same user, the sum of the classifications ought to equal unity. Only individual probabilities are checked.  | [optional] 
**group_ids** | **[int]** | List of group IDs corresponding to which groups should be able to view classification. Defaults to all of requesting user&#39;s groups.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


