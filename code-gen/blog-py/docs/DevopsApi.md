# openapi_client.DevopsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_unique_index_devops_indexes_collection_field_get**](DevopsApi.md#create_unique_index_devops_indexes_collection_field_get) | **GET** /devops/indexes/{collection}/{field} | Create Unique Index


# **create_unique_index_devops_indexes_collection_field_get**
> object create_unique_index_devops_indexes_collection_field_get(collection, field)

Create Unique Index

### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DevopsApi(api_client)
    collection = None # object | 
    field = None # object | 

    try:
        # Create Unique Index
        api_response = api_instance.create_unique_index_devops_indexes_collection_field_get(collection, field)
        print("The response of DevopsApi->create_unique_index_devops_indexes_collection_field_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevopsApi->create_unique_index_devops_indexes_collection_field_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | [**object**](.md)|  | 
 **field** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

