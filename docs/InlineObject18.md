# InlineObject18

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Short string to make this taxonomy memorable to end users.  | 
**hierarchy** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Nested JSON describing the taxonomy which should be validated against a schema before entry  | 
**version** | **str** | Semantic version of this taxonomy name  | 
**group_ids** | **[int]** | List of group IDs corresponding to which groups should be able to view comment. Defaults to all of requesting user&#39;s groups.  | [optional] 
**provenance** | **str** | Identifier (e.g., URL or git hash) that uniquely ties this taxonomy back to an origin or place of record  | [optional] 
**is_latest** | **bool** | Consider this version of the taxonomy with this name the latest? Defaults to True.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


