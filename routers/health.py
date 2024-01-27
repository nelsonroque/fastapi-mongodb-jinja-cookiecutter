from fastapi import APIRouter, Response, Body, Depends, Request
import datetime
from core.responses import PrettyJSONResponse

# =============================================================================

# --- create router ---
router = APIRouter()

# =============================================================================

@router.get("/health", status_code=200, response_class=PrettyJSONResponse)
async def check_health(request: Request):
    return {
        "status": "up",
        "request_url_port": request.url.port,
        "request_client_port": request.client.port,
        "client": str(request.client),
        "datetime": str(datetime.datetime.now().isoformat()),
        # "state_start": request.state.start_time,
        # "state_end": request.state.end_time,
        "headers": dict(request.headers),  # Convert headers to a dictionary
        "path_params": dict(request.path_params),  # Convert path params to a dictionary
        "query": dict(request.query_params),  # Convert query params to a dictionary
    }

# =============================================================================