import logging
import chromadb
from chromadb.config import Settings


logging.basicConfig(filename='database.log', level=logging.INFO)

client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="db/"))
collection = client.create_collection(name="documents")


logging.info(f"Initialize Database")