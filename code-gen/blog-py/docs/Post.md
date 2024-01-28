# Post


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_utc** | **object** |  | [optional] 
**title** | **object** |  | 
**description** | **object** |  | 
**body** | **object** |  | 
**author_id** | **object** |  | 
**slug** | **object** |  | 
**tags** | **object** |  | 
**published** | **object** |  | 

## Example

```python
from openapi_client.models.post import Post

# TODO update the JSON string below
json = "{}"
# create an instance of Post from a JSON string
post_instance = Post.from_json(json)
# print the JSON string representation of the object
print Post.to_json()

# convert the object into a dict
post_dict = post_instance.to_dict()
# create an instance of Post from a dict
post_form_dict = post.from_dict(post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


