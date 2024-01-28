# DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateBlogBlogPost**](DefaultApi.md#CreateBlogBlogPost) | **POST** /blog | Create Blog
[**DeleteBlogBlogIdDelete**](DefaultApi.md#DeleteBlogBlogIdDelete) | **DELETE** /blog/{id} | Delete Blog
[**ReadAllBlogsBlogGet**](DefaultApi.md#ReadAllBlogsBlogGet) | **GET** /blog | Read All Blogs
[**ReadBlogByIdBlogIdIdGet**](DefaultApi.md#ReadBlogByIdBlogIdIdGet) | **GET** /blog/id/{id} | Read Blog By Id
[**ReadBlogBySlugBlogSlugSlugGet**](DefaultApi.md#ReadBlogBySlugBlogSlugSlugGet) | **GET** /blog/slug/{slug} | Read Blog By Slug
[**RootGet**](DefaultApi.md#RootGet) | **GET** / | Root
[**UpdateBlogBlogIdPut**](DefaultApi.md#UpdateBlogBlogIdPut) | **PUT** /blog/{id} | Update Blog


# **CreateBlogBlogPost**
> AnyType CreateBlogBlogPost(post)

Create Blog

### Example
```R
library(openapi)

# Create Blog
#
# prepare function argument(s)
var_post <- Post$new(TODO, TODO, TODO, TODO, TODO, TODO, TODO, TODO) # Post | 

api_instance <- DefaultApi$new()
# to save the result into a file, simply add the optional `data_file` parameter, e.g.
# result <- api_instance$CreateBlogBlogPost(var_postdata_file = "result.txt")
result <- api_instance$CreateBlogBlogPost(var_post)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post** | [**Post**](Post.md)|  | 

### Return type

[**AnyType**](AnyType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  -  |
| **503** | Service Unavailable |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |

# **DeleteBlogBlogIdDelete**
> AnyType DeleteBlogBlogIdDelete(id)

Delete Blog

### Example
```R
library(openapi)

# Delete Blog
#
# prepare function argument(s)
var_id <- TODO # AnyType | 

api_instance <- DefaultApi$new()
# to save the result into a file, simply add the optional `data_file` parameter, e.g.
# result <- api_instance$DeleteBlogBlogIdDelete(var_iddata_file = "result.txt")
result <- api_instance$DeleteBlogBlogIdDelete(var_id)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**AnyType**](.md)|  | 

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
| **503** | Service Unavailable |  -  |
| **422** | Validation Error |  -  |

# **ReadAllBlogsBlogGet**
> AnyType ReadAllBlogsBlogGet()

Read All Blogs

### Example
```R
library(openapi)

# Read All Blogs
#

api_instance <- DefaultApi$new()
# to save the result into a file, simply add the optional `data_file` parameter, e.g.
# result <- api_instance$ReadAllBlogsBlogGet(data_file = "result.txt")
result <- api_instance$ReadAllBlogsBlogGet()
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
| **503** | Service Unavailable |  -  |

# **ReadBlogByIdBlogIdIdGet**
> AnyType ReadBlogByIdBlogIdIdGet(id)

Read Blog By Id

### Example
```R
library(openapi)

# Read Blog By Id
#
# prepare function argument(s)
var_id <- "id_example" # character | 

api_instance <- DefaultApi$new()
# to save the result into a file, simply add the optional `data_file` parameter, e.g.
# result <- api_instance$ReadBlogByIdBlogIdIdGet(var_iddata_file = "result.txt")
result <- api_instance$ReadBlogByIdBlogIdIdGet(var_id)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**|  | 

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
| **503** | Service Unavailable |  -  |
| **422** | Validation Error |  -  |

# **ReadBlogBySlugBlogSlugSlugGet**
> AnyType ReadBlogBySlugBlogSlugSlugGet(slug)

Read Blog By Slug

### Example
```R
library(openapi)

# Read Blog By Slug
#
# prepare function argument(s)
var_slug <- TODO # AnyType | 

api_instance <- DefaultApi$new()
# to save the result into a file, simply add the optional `data_file` parameter, e.g.
# result <- api_instance$ReadBlogBySlugBlogSlugSlugGet(var_slugdata_file = "result.txt")
result <- api_instance$ReadBlogBySlugBlogSlugSlugGet(var_slug)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | [**AnyType**](.md)|  | 

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
| **503** | Service Unavailable |  -  |
| **422** | Validation Error |  -  |

# **RootGet**
> AnyType RootGet()

Root

### Example
```R
library(openapi)

# Root
#

api_instance <- DefaultApi$new()
# to save the result into a file, simply add the optional `data_file` parameter, e.g.
# result <- api_instance$RootGet(data_file = "result.txt")
result <- api_instance$RootGet()
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

# **UpdateBlogBlogIdPut**
> AnyType UpdateBlogBlogIdPut(id, post)

Update Blog

### Example
```R
library(openapi)

# Update Blog
#
# prepare function argument(s)
var_id <- TODO # AnyType | 
var_post <- Post$new(TODO, TODO, TODO, TODO, TODO, TODO, TODO, TODO) # Post | 

api_instance <- DefaultApi$new()
# to save the result into a file, simply add the optional `data_file` parameter, e.g.
# result <- api_instance$UpdateBlogBlogIdPut(var_id, var_postdata_file = "result.txt")
result <- api_instance$UpdateBlogBlogIdPut(var_id, var_post)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**AnyType**](.md)|  | 
 **post** | [**Post**](Post.md)|  | 

### Return type

[**AnyType**](AnyType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **503** | Service Unavailable |  -  |
| **422** | Validation Error |  -  |

