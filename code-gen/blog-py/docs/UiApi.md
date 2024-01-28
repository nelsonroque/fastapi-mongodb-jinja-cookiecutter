# openapi_client.UiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_blogs_ui_blog_get**](UiApi.md#get_all_blogs_ui_blog_get) | **GET** /ui/blog | Get All Blogs
[**render_frontend_ui_homepage_get**](UiApi.md#render_frontend_ui_homepage_get) | **GET** /ui/homepage | Render Frontend
[**render_frontend_ui_test_get**](UiApi.md#render_frontend_ui_test_get) | **GET** /ui/test | Render Frontend


# **get_all_blogs_ui_blog_get**
> object get_all_blogs_ui_blog_get()

Get All Blogs

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
    api_instance = openapi_client.UiApi(api_client)

    try:
        # Get All Blogs
        api_response = api_instance.get_all_blogs_ui_blog_get()
        print("The response of UiApi->get_all_blogs_ui_blog_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->get_all_blogs_ui_blog_get: %s\n" % e)
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

# **render_frontend_ui_homepage_get**
> object render_frontend_ui_homepage_get()

Render Frontend

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
    api_instance = openapi_client.UiApi(api_client)

    try:
        # Render Frontend
        api_response = api_instance.render_frontend_ui_homepage_get()
        print("The response of UiApi->render_frontend_ui_homepage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->render_frontend_ui_homepage_get: %s\n" % e)
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

# **render_frontend_ui_test_get**
> object render_frontend_ui_test_get()

Render Frontend

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
    api_instance = openapi_client.UiApi(api_client)

    try:
        # Render Frontend
        api_response = api_instance.render_frontend_ui_test_get()
        print("The response of UiApi->render_frontend_ui_test_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->render_frontend_ui_test_get: %s\n" % e)
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

