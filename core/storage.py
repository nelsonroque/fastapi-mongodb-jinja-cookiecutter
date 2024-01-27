import pymongo 
from .config import config

def init_db():
    # Connect to MongoDB
    client_srv = f"mongodb+srv://{config.mongodb_username}:{config.mongodb_password.get_secret_value()}@{config.mongodb_cluster_id.get_secret_value()}/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(client_srv)
    db = client[config.mongodb_db_name]
    return client, db
