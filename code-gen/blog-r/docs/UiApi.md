# UiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetAllBlogsUiBlogGet**](UiApi.md#GetAllBlogsUiBlogGet) | **GET** /ui/blog | Get All Blogs
[**RenderFrontendUiHomepageGet**](UiApi.md#RenderFrontendUiHomepageGet) | **GET** /ui/homepage | Render Frontend
[**RenderFrontendUiTestGet**](UiApi.md#RenderFrontendUiTestGet) | **GET** /ui/test | Render Frontend


# **GetAllBlogsUiBlogGet**
> AnyType GetAllBlogsUiBlogGet()

Get All Blogs

### Example
```R
library(openapi)

# Get All Blogs
#

api_instance <- UiApi$new()
# to save the result into a file, simply add the optional `data_file` parameter, e.g.
# result <- api_instance$GetAllBlogsUiBlogGet(data_file = "result.txt")
result <- api_instance$GetAllBlogsUiBlogGet()
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

# **RenderFrontendUiHomepageGet**
> AnyType RenderFrontendUiHomepageGet()

Render Frontend

### Example
```R
library(openapi)

# Render Frontend
#

api_instance <- UiApi$new()
# to save the result into a file, simply add the optional `data_file` parameter, e.g.
# result <- api_instance$RenderFrontendUiHomepageGet(data_file = "result.txt")
result <- api_instance$RenderFrontendUiHomepageGet()
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

# **RenderFrontendUiTestGet**
> AnyType RenderFrontendUiTestGet()

Render Frontend

### Example
```R
library(openapi)

# Render Frontend
#

api_instance <- UiApi$new()
# to save the result into a file, simply add the optional `data_file` parameter, e.g.
# result <- api_instance$RenderFrontendUiTestGet(data_file = "result.txt")
result <- api_instance$RenderFrontendUiTestGet()
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

