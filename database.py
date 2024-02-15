import logging
import chromadb
from chromadb.config import Settings


logging.basicConfig(filename='database.log', level=logging.INFO)

client = chromadb.PersistentClient(path="db/")
collection = client.get_or_create_collection(name="documents")


logging.info(f"Initialize Database")