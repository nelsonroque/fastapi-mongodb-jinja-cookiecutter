#from .models import Log


# TODO: move to pydantic

# async def log_request_to_db(request, collection):

#     # Create a dictionary containing the request data
#     request_data = Log({
#         "timestamp": get_utc_timestamp(),
#         "host": request.client.host,
#         "method": request.method,
#         "url": request.url._url,
#         "headers": dict(request.headers),
#     })

#     # log link clicks to database ---
#     client, db = init_db()
#     collection = db["logs"]
#     status = collection.insert_one(collection, request_data)
#     client.close()
#     return 1
