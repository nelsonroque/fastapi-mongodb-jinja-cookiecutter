import requests
import uuid

url = "http://0.0.0.0:8001/blog"

# generate 1000 posts
# TODO: add loreum ipsum support (or faker)
for i in range(1, 1000):
    payload = {
        "title": str(uuid.uuid4()),
        "description": "string",
        "body": "string",
        "author_id": "string",
        "slug": str(uuid.uuid4()),
        "tags": ["string"],
        "published": True
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)