import pymongo 
from .config import config
from pymongo import ASCENDING
from pymongo.errors import DuplicateKeyError

def init_db():
    # Connect to MongoDB
    client_srv = f"mongodb+srv://{config.mongodb_username}:{config.mongodb_password.get_secret_value()}@{config.mongodb_cluster_id.get_secret_value()}/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(client_srv)
    db = client[config.mongodb_db_name]
    return client, db

def create_index(collection, field):
    client, db = init_db()
    collection = db[collection]
    collection.create_index([(field, ASCENDING)], unique=True)
    return {"status": "ok"}