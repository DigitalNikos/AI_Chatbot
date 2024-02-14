from langchain.vectorstores import FAISS

vector_dim = 384 # Dimension for sentence-transformers/all-MiniLM-L6-v2 model
db = FAISS(vector_dim=vector_dim)