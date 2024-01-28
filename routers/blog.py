from fastapi import APIRouter, Response, Body, Depends, Request
from fastapi.templating import Jinja2Templates

from core.models import Post, Posts
from core.storage import init_db
from bson.objectid import ObjectId

# =============================================================================

# --- create router ---
router = APIRouter()

# =============================================================================

# --- CRUD operations for blog posts ---

# (C)reate blog post
@router.post("/blog")
def create_blog(blog: Post):
    client, db = init_db()
    collection = db["blogs"]
    try:
        r = collection.insert_one(blog.model_dump())
        return {"status": "ok", "id": r.inserted_id}
    except Exception as e:
        return {"status": "error", "error": str(e)}
    
# =============================================================================

# (R)ead single blog
@router.get("/blog/id/{id}")
def read_blog_by_id(id: str):
    client, db = init_db()
    collection = db["blogs"]
    try:
        # Retrieve a single document
        document = collection.find_one({"_id": ObjectId(id)})
        if document:
            # Convert ObjectId to string and adapt document for Pydantic model
            document["_id"] = str(document["_id"])
            return Post(**document)
        else:
            return {"status": "not found"}
    except Exception as e:
        return {"status": "error", "error": str(e)}
    
@router.get("/blog/slug/{slug}")
def read_blog_by_slug(slug: str):
    client, db = init_db()
    collection = db["blogs"]
    try:
        # Retrieve a single document
        document = collection.find_one({"slug": slug})
        if document:
            # Convert ObjectId to string and adapt document for Pydantic model
            document["_id"] = str(document["_id"])
            return Post(**document)
        else:
            return {"status": "not found"}
    except Exception as e:
        return {"status": "error", "error": str(e)}
    
# (R)ead all blogs
@router.get("/blog")
def read_all_blogs():
    client, db = init_db()
    collection = db["blogs"]
    try:
        # Retrieve a single document
        documents = list(collection.find({}))
        posts_list = []
        for doc in documents:
            # Convert ObjectId to string
            doc['_id'] = str(doc['_id'])
            posts_list.append(Post(**doc))

        # Create and return the Posts object
        return Posts(posts=posts_list)

    except Exception as e:
        return {"status": "error", "error": str(e)}

# =============================================================================
    
# (U)pdate blog post
@router.put("/blog/{id}")
def update_blog(id: str, blog: Post):
    client, db = init_db()
    collection = db["blogs"]
    try:
        r = collection.update_one({"_id": ObjectId(id)}, {"$set": blog.model_dump()})
        return {"status": "ok", "matched_count": r.matched_count, "modified_count": r.modified_count}
    except Exception as e:
        return {"status": "error", "error": str(e)}

# =============================================================================
  
# (D)elete blog post
@router.delete("/blog/{id}")
def delete_blog(id: str):
    client, db = init_db()
    collection = db["blogs"]
    try:
        r = collection.delete_one({"_id": ObjectId(id)})
        return {"status": "ok", "deleted_count": r.deleted_count}
    except Exception as e:
        return {"status": "error", "error": str(e)}