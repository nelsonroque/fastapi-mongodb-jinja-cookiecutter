import requests

url = "http://0.0.0.0:8000/blog"

# generate 1000 posts
for i in range(1, 1000):
    payload = {
        "title": "string_{}".format(i),
        "description": "string",
        "body": "string",
        "author_id": "string",
        "slug": "string_{}".format(i),
        "tags": ["string"],
        "published": True
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)