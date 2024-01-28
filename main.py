import uvicorn
from uvicorn.config import LOGGING_CONFIG

# --- Run the server ---
if __name__ == "__main__":
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = "[%(asctime)s] [%(name)s] [%(levelprefix)s] [%(funcName)s] [%(lineno)d] [%(message)s]"
    uvicorn.run("server.api:app", host="0.0.0.0", port=8001, log_level="info")