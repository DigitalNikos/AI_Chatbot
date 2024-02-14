import logging
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

logging.basicConfig(filename='embedding.log', level=logging.INFO)

# Embedding Model for converting text to numerical representations
embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
logging.info(f"Initialize Embedding model")