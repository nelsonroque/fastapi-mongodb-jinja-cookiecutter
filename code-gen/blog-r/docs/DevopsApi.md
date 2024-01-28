# DevopsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateUniqueIndexDevopsIndexesCollectionFieldGet**](DevopsApi.md#CreateUniqueIndexDevopsIndexesCollectionFieldGet) | **GET** /devops/indexes/{collection}/{field} | Create Unique Index


# **CreateUniqueIndexDevopsIndexesCollectionFieldGet**
> AnyType CreateUniqueIndexDevopsIndexesCollectionFieldGet(collection, field)

Create Unique Index

### Example
```R
library(openapi)

# Create Unique Index
#
# prepare function argument(s)
var_collection <- TODO # AnyType | 
var_field <- TODO # AnyType | 

api_instance <- DevopsApi$new()
# to save the result into a file, simply add the optional `data_file` parameter, e.g.
# result <- api_instance$CreateUniqueIndexDevopsIndexesCollectionFieldGet(var_collection, var_fielddata_file = "result.txt")
result <- api_instance$CreateUniqueIndexDevopsIndexesCollectionFieldGet(var_collection, var_field)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | [**AnyType**](.md)|  | 
 **field** | [**AnyType**](.md)|  | 

### Return type

[**AnyType**](AnyType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **404** | Not found |  -  |
| **422** | Validation Error |  -  |

