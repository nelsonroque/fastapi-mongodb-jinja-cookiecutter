# HealthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CheckHealthHealthGet**](HealthApi.md#CheckHealthHealthGet) | **GET** /health/ | Check Health


# **CheckHealthHealthGet**
> AnyType CheckHealthHealthGet()

Check Health

### Example
```R
library(openapi)

# Check Health
#

api_instance <- HealthApi$new()
# to save the result into a file, simply add the optional `data_file` parameter, e.g.
# result <- api_instance$CheckHealthHealthGet(data_file = "result.txt")
result <- api_instance$CheckHealthHealthGet()
dput(result)
```

### Parameters
This endpoint does not need any parameter.

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

