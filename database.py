import logging

from langchain.vectorstores import FAISS

logging.basicConfig(filename='database.log', level=logging.INFO)

vector_dim = 384 # Dimension for sentence-transformers/all-MiniLM-L6-v2 model
db = FAISS(vector_dim=vector_dim)
logging.info(f"Initialize Database")