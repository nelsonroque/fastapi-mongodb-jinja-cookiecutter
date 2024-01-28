import fastapi
from .storage import create_index
from .log import logger
from .utils import get_utc_timestamp, uuid

# TODO: log to database
async def log_requests(request: fastapi.Request, call_next):
    create_index("blogs", "slug")
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