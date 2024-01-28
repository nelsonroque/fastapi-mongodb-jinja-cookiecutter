# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_blog_blog_post**](DefaultApi.md#create_blog_blog_post) | **POST** /blog | Create Blog
[**delete_blog_blog_id_delete**](DefaultApi.md#delete_blog_blog_id_delete) | **DELETE** /blog/{id} | Delete Blog
[**read_all_blogs_blog_get**](DefaultApi.md#read_all_blogs_blog_get) | **GET** /blog | Read All Blogs
[**read_blog_by_id_blog_id_id_get**](DefaultApi.md#read_blog_by_id_blog_id_id_get) | **GET** /blog/id/{id} | Read Blog By Id
[**read_blog_by_slug_blog_slug_slug_get**](DefaultApi.md#read_blog_by_slug_blog_slug_slug_get) | **GET** /blog/slug/{slug} | Read Blog By Slug
[**root_get**](DefaultApi.md#root_get) | **GET** / | Root
[**update_blog_blog_id_put**](DefaultApi.md#update_blog_blog_id_put) | **PUT** /blog/{id} | Update Blog


# **create_blog_blog_post**
> object create_blog_blog_post(post)

Create Blog

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.post import Post
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
    api_instance = openapi_client.DefaultApi(api_client)
    post = openapi_client.Post() # Post | 

    try:
        # Create Blog
        api_response = api_instance.create_blog_blog_post(post)
        print("The response of DefaultApi->create_blog_blog_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_blog_blog_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post** | [**Post**](Post.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**503** | Service Unavailable |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_blog_blog_id_delete**
> object delete_blog_blog_id_delete(id)

Delete Blog

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
    api_instance = openapi_client.DefaultApi(api_client)
    id = None # object | 

    try:
        # Delete Blog
        api_response = api_instance.delete_blog_blog_id_delete(id)
        print("The response of DefaultApi->delete_blog_blog_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_blog_blog_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_all_blogs_blog_get**
> object read_all_blogs_blog_get()

Read All Blogs

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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Read All Blogs
        api_response = api_instance.read_all_blogs_blog_get()
        print("The response of DefaultApi->read_all_blogs_blog_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->read_all_blogs_blog_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_blog_by_id_blog_id_id_get**
> object read_blog_by_id_blog_id_id_get(id)

Read Blog By Id

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
    api_instance = openapi_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Read Blog By Id
        api_response = api_instance.read_blog_by_id_blog_id_id_get(id)
        print("The response of DefaultApi->read_blog_by_id_blog_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->read_blog_by_id_blog_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_blog_by_slug_blog_slug_slug_get**
> object read_blog_by_slug_blog_slug_slug_get(slug)

Read Blog By Slug

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
    api_instance = openapi_client.DefaultApi(api_client)
    slug = None # object | 

    try:
        # Read Blog By Slug
        api_response = api_instance.read_blog_by_slug_blog_slug_slug_get(slug)
        print("The response of DefaultApi->read_blog_by_slug_blog_slug_slug_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->read_blog_by_slug_blog_slug_slug_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | [**object**](.md)|  | 

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
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> object root_get()

Root

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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Root
        api_response = api_instance.root_get()
        print("The response of DefaultApi->root_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_blog_blog_id_put**
> object update_blog_blog_id_put(id, post)

Update Blog

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.post import Post
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
    api_instance = openapi_client.DefaultApi(api_client)
    id = None # object | 
    post = openapi_client.Post() # Post | 

    try:
        # Update Blog
        api_response = api_instance.update_blog_blog_id_put(id, post)
        print("The response of DefaultApi->update_blog_blog_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_blog_blog_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **post** | [**Post**](Post.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

