# Annotation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **int** | ID of the Annotation author&#39;s User instance. | 
**origin** | **str** | What generated the annotation. This should generally map to a filter/group name. But since an annotation can be made accessible to multiple groups, the origin name does not necessarily have to map to a single group name. The important thing is to make the origin distinct and descriptive such that annotations from the same origin generally have the same metrics. One annotation with multiple fields from each origin is allowed. | 
**obj_id** | **str** | ID of the Annotation&#39;s Obj. | 
**id** | **int** | Unique object identifier. | [optional] 
**data** | **bool, date, datetime, dict, float, int, list, str, none_type** | Searchable data in JSON format | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


