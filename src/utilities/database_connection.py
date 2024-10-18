import os

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

COLLECTIONS = {
    "get_manga_images": "MANGAIMAGES",
    "get_manga_chapters": "MANGACHAPTERS",
    "get_manga_metadata": "MANGAMETATDATA",
    "get_csv_links": "CSVLINKS",
}


def get_database_connection():
    """Creates a connection to the MongoDB database."""

    try:
        password = os.getenv("MONGODB_PASSWORD")
        username = os.getenv("MONGODB_USERNAME")
        dbname = os.getenv("MONGODB_DATABASE")
        cluster = os.getenv("MONGODB_CLUSTER")
        uri = f'mongodb+srv://{username}:{password}@{cluster}.xovcj.mongodb.net/?retryWrites=true&w=majority&appName={cluster}'
        client = MongoClient(uri)
        db = client[dbname]
        print("Successfully connected to MongoDB")
        return db
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        return None


def get_collection(collection_name: str = None, db=None):
    """Fetches a specific collection from the MongoDB database."""

    if db is None:
        db = get_database_connection()  # Ensure connection

    collection_name = COLLECTIONS.get(collection_name)  # Use direct mapping

    if collection_name:
        collection = db[collection_name]
        print(f"Retrieved collection: {collection_name}")
        return collection
    else:
        print(f"No Collection Found with the internal name: {collection_name}")
        raise ValueError(
            f"Invalid collection name. Please check the COLLECTIONS dictionary."
        )