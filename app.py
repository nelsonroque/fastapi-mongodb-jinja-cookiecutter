# Import FastAPI and other modules ---
import fastapi
from fastapi.staticfiles import StaticFiles
import uvicorn
from uvicorn.config import LOGGING_CONFIG
from contextlib import asynccontextmanager

# Import custom modules ---
from core.config import config
from core.utils import get_utc_timestamp

# Import routers ---
from routers.ui import router as ui_router
from routers.blog import router as blog_router
from routers.health import router as healthcheck_router
from routers.devops import router as devops_router

# =============================================================================

# add lifecycle event handler ---
@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    print("Startup event", get_utc_timestamp())
    yield
    print("Startup event", get_utc_timestamp())
    # TODO: add timestamp to request state and uuid
    # request.state.start_time = get_utc_timestamp()
    # yield
    # request.state.end_time = get_utc_timestamp()

# =============================================================================


# --- load FastAPI app ---
app = fastapi.FastAPI(
    debug=True,
    title=config.app_name,
    description=config.app_description,
    version=config.app_version,
    lifespan=lifespan
    # docs_url=None, # in case you want to hide the default Swagger OpenAPI docs
    # redoc_url=None, # in case you want to hide the default redoc docs
)

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

# --- Run the server ---
if __name__ == "__main__":
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = "[%(asctime)s] [%(name)s] [%(levelprefix)s] [%(funcName)s] [%(lineno)d] [%(message)s]"
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")

# =============================================================================
