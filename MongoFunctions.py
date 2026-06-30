import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
load_dotenv(override=True)

# Set up MongoDB connection parameters from environment variables
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")

# Function to insert a document into MongoDB
def insert_document(document):
    """Insert a document into the MongoDB collection."""
    client = MongoClient(MONGO_URI)
    try:
        client[MONGO_DB_NAME][MONGO_COLLECTION_NAME].insert_one(document)
        print(f"Inserted into {MONGO_DB_NAME}.{MONGO_COLLECTION_NAME} successfully!")
    except ConnectionFailure:
        print("Failed to connect to MongoDB.")
    except OperationFailure as e:
        print(f"MongoDB operation failed: {e}")

# Function to find documents in MongoDB based on a query
def find_documents(query):
    """Find documents in the MongoDB collection based on a query."""
    client = MongoClient(MONGO_URI)
    try:
        results = client[MONGO_DB_NAME][MONGO_COLLECTION_NAME].find(query)
        return list(results)
    except ConnectionFailure:
        print("Failed to connect to MongoDB.")
        return []
    except OperationFailure as e:
        print(f"MongoDB operation failed: {e}")
        return []
    
# Function to update a document in MongoDB based on a query
def update_document(query, update):
    """Update a document in the MongoDB collection based on a query."""
    client = MongoClient(MONGO_URI)
    try:
        result = client[MONGO_DB_NAME][MONGO_COLLECTION_NAME].update_one(query, update)
        if result.matched_count > 0:
            print(f"Updated document in {MONGO_DB_NAME}.{MONGO_COLLECTION_NAME} successfully!")
        else:
            print("No matching document found to update.")
    except ConnectionFailure:
        print("Failed to connect to MongoDB.")
    except OperationFailure as e:
        print(f"MongoDB operation failed: {e}")

# Function to delete a document from MongoDB based on a query
def delete_document(query):
    """Delete a document from the MongoDB collection based on a query."""
    client = MongoClient(MONGO_URI)
    try:
        result = client[MONGO_DB_NAME][MONGO_COLLECTION_NAME].delete_one(query)
        if result.deleted_count > 0:
            print(f"Deleted document from {MONGO_DB_NAME}.{MONGO_COLLECTION_NAME} successfully!")
        else:
            print("No matching document found to delete.")
    except ConnectionFailure:
        print("Failed to connect to MongoDB.")
    except OperationFailure as e:
        print(f"MongoDB operation failed: {e}")

# Insert documents into MongoDB
def insert_documents(documents):
    """Insert multiple documents into the MongoDB collection."""
    client = MongoClient(MONGO_URI)
    try:
        client[MONGO_DB_NAME][MONGO_COLLECTION_NAME].insert_many(documents)
        print(f"Inserted multiple documents into {MONGO_DB_NAME}.{MONGO_COLLECTION_NAME} successfully!")
    except ConnectionFailure:
        print("Failed to connect to MongoDB.")
    except OperationFailure as e:
        print(f"MongoDB operation failed: {e}")