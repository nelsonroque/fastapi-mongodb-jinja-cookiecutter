from fastapi import APIRouter, Response, Body, Depends, Request
import datetime
from core.responses import PrettyJSONResponse

# =============================================================================

# --- create router ---
router = APIRouter(prefix="/health",
                   tags=["health"],
                   responses={404: {"description": "Not found"}})

# =============================================================================

@router.get("/", status_code=200, response_class=PrettyJSONResponse)
async def check_health(request: Request):
    return {
        "status": "up",
        "request_url_port": request.url.port,
        "request_client_port": request.client.port,
        "client": str(request.client),
        "datetime": str(datetime.datetime.now().isoformat()),
        # TODO: add start and end time from request (may require middleware)
        "headers": dict(request.headers),  # Convert headers to a dictionary
        "path_params": dict(request.path_params),  # Convert path params to a dictionary
        "query": dict(request.query_params),  # Convert query params to a dictionary
    }

# =============================================================================