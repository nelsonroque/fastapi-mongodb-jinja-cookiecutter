from .utils import get_utc_timestamp
from .config import config
from .storage import insert_document


# TODO: move to pydantic

async def log_request_to_db(request, collection):
    # request_body = await request.json()
    request_headers = dict(request.headers)

    # Create a dictionary containing the request data
    request_data = {
        "timestamp": get_utc_timestamp(),
        "host": request.client.host,
        "method": request.method,
        "url": request.url._url,
        "headers": request_headers,
    }

    # log link clicks to database ---
    status = insert_document(collection, request_data)

    return status