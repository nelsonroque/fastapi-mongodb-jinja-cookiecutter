import uuid
from ..server.core.storage import init_db

url = "http://0.0.0.0:8000/blog"

# generate 1000 posts
# TODO: add loreum ipsum support (or faker)
load = []
for i in range(1, 1000):
    payload = {
        "title": f"string_{str(uuid.uuid4())}",
        "description": "string",
        "body": "string",
        "author_id": "string",
        "slug": str(uuid.uuid4()),
        "tags": ["string"],
        "published": True
    }
    load.append(payload)

# push to db
client, db = init_db()
collection = db["blogs"]
collection.insert_many(load)