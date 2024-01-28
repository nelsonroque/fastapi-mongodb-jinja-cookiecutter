# Import FastAPI and other modules ---
import fastapi
from fastapi.staticfiles import StaticFiles
import uvicorn
from uvicorn.config import LOGGING_CONFIG
from contextlib import asynccontextmanager

# Import custom modules ---
from core.config import config
from core.utils import get_utc_timestamp
from core.log import logger

# Import routers ---
from routers.ui import router as ui_router
from routers.blog import router as blog_router
from routers.health import router as healthcheck_router
from routers.devops import router as devops_router

# =============================================================================


# --- load FastAPI app ---
app = fastapi.FastAPI(
    debug=True,
    title=config.app_name,
    description=config.app_description,
    version=config.app_version,
    # docs_url=None, # in case you want to hide the default Swagger OpenAPI docs
    # redoc_url=None, # in case you want to hide the default redoc docs
)

@app.middleware("http")
# TODO: log to database
async def log_requests(request: fastapi.Request, call_next):
    import uuid
    request_id = uuid.uuid4()
    request_start_time = get_utc_timestamp()

    logger.info(f"Request ID: {request_id} - Start: {request_start_time}")
    logger.info(f"Request: {request.method} {request.url}")

    response = await call_next(request)
    
    request_end_time = get_utc_timestamp()
    time_elapsed = request_end_time - request_start_time

    logger.info(f"Request ID: {request_id} - End: {request_end_time}")
    logger.info(f"Response: {response.status_code} for Request ID: {request_id}")

    # Example: Adding custom headers (you can also modify the response body if needed)
    response.headers['X-Request-Start-Time'] = str(request_start_time)
    response.headers['X-Request-End-Time'] = str(request_end_time)
    response.headers['X-Time-Elapsed-Seconds'] = f"{time_elapsed}"


    return response

# =============================================================================

# --- Mount static files and templates ---
app.mount("/static", StaticFiles(directory="static"), name="static")

# =============================================================================

# --- Routes ---
app.include_router(blog_router)
app.include_router(healthcheck_router)
app.include_router(ui_router)
app.include_router(devops_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# =============================================================================

# --- Run the server ---
if __name__ == "__main__":
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = "[%(asctime)s] [%(name)s] [%(levelprefix)s] [%(funcName)s] [%(lineno)d] [%(message)s]"
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="info")

# =============================================================================
