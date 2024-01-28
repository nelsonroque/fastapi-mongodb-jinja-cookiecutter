# Import FastAPI and other modules ---
import fastapi
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

# Import custom modules ---
from .core.config import config
from .core.log import logger
from .core.middleware import log_requests

# Import routers ---
from .routers.ui import router as ui_router
from .routers.blog import router as blog_router
from .routers.health import router as healthcheck_router
from .routers.devops import router as devops_router

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

# =============================================================================

# --- Configure logging middleware ---
app.middleware("http")(log_requests)

# =============================================================================

# --- Mount static files and templates ---
app.mount("/static", StaticFiles(directory="static"), name="static")

# =============================================================================

# --- Routes ---
app.include_router(blog_router)
app.include_router(healthcheck_router)
app.include_router(ui_router)
app.include_router(devops_router)

# =============================================================================

@app.get("/")
async def root():
    return {"message": "Hello World"}

# =============================================================================