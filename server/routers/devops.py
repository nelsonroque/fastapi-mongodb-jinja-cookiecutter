from fastapi import APIRouter, Response, Body, Depends, Request
import datetime
from ..core.responses import PrettyJSONResponse
from ..core.storage import init_db, ASCENDING

# =============================================================================

# --- create router ---
router = APIRouter(prefix="/devops",
                   tags=["devops"],
                   responses={404: {"description": "Not found"}})

# =============================================================================

@router.get("/indexes/{collection}/{field}", status_code=200, response_class=PrettyJSONResponse)
async def create_unique_index(collection: str, field: str):
    client, db = init_db()

    # Creating a unique index
    try:
        collection = db[collection]
        collection.create_index([(field, ASCENDING)], unique=True)
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "error": str(e)}

# =============================================================================