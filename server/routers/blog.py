from fastapi import APIRouter, Response, Body, Depends, Request, status
from fastapi.templating import Jinja2Templates

from core.models import Post, Posts, Status
from core.storage import init_db, DuplicateKeyError
from bson.objectid import ObjectId

# =============================================================================

# --- create router ---
router = APIRouter()

# =============================================================================

# --- CRUD operations for blog posts ---


# (C)reate blog post
@router.post(
    "/blog",
    status_code=status.HTTP_201_CREATED,
    responses={503: {"description": "Service Unavailable"},
               409: {"description": "Conflict"}},
)
def create_blog(blog: Post, response: Response):
    client, db = init_db()
    collection = db["blogs"]
    try:
        r = collection.insert_one(blog.model_dump())
        return Status(**{"status": "ok"})
    except DuplicateKeyError as e:
        response.status_code = status.HTTP_409_CONFLICT
        return Status(**{"status": "error", "error": "Duplicate `slug`. Record not created."})
    except Exception as e:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return Status(**{"status": "error", "error": str(e)})


# =============================================================================


# (R)ead single blog
@router.get(
    "/blog/id/{id}",
    status_code=status.HTTP_200_OK,
    responses={503: {"description": "Service Unavailable"}},
)
def read_blog_by_id(id: str, response: Response):
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
            return Status(**{"status": "not found"})
    except Exception as e:
        return Status(**{"status": "error", "error": str(e)})


@router.get(
    "/blog/slug/{slug}",
    status_code=status.HTTP_200_OK,
    responses={503: {"description": "Service Unavailable"}},
)
def read_blog_by_slug(slug: str, response: Response):
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
            return Status(**{"status": "not found"})
    except Exception as e:
        return Status(**{"status": "error", "error": str(e)})


# (R)ead all blogs
@router.get(
    "/blog",
    status_code=status.HTTP_200_OK,
    responses={503: {"description": "Service Unavailable"}},
)
def read_all_blogs(response: Response):
    client, db = init_db()
    collection = db["blogs"]
    try:
        # Retrieve a single document
        documents = list(collection.find({}))
        posts_list = []
        for doc in documents:
            # Convert ObjectId to string
            doc["_id"] = str(doc["_id"])
            posts_list.append(Post(**doc))

        # Create and return the Posts object
        return Posts(posts=posts_list)

    except Exception as e:
        return Status(**{"status": "error", "error": str(e)})


# =============================================================================


# (U)pdate blog post
@router.put(
    "/blog/{id}",
    status_code=status.HTTP_200_OK,
    responses={503: {"description": "Service Unavailable"}},
)
def update_blog(id: str, blog: Post, response: Response):
    client, db = init_db()
    collection = db["blogs"]
    try:
        r = collection.update_one({"_id": ObjectId(id)}, {"$set": blog.model_dump()})
        return Status(
            **{
                "status": "ok",
                "matched_count": r.matched_count,
                "modified_count": r.modified_count,
            }
        )
    except Exception as e:
        return Status(**{"status": "error", "error": str(e)})


# =============================================================================


# (D)elete blog post
@router.delete(
    "/blog/{id}",
    status_code=status.HTTP_200_OK,
    responses={503: {"description": "Service Unavailable"}},
)
def delete_blog(id: str, response: Response):
    client, db = init_db()
    collection = db["blogs"]
    try:
        r = collection.delete_one({"_id": ObjectId(id)})
        return Status(**{"status": "ok", "deleted_count": r.deleted_count})
    except Exception as e:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return Status(**{"status": "error", "error": str(e)})
