from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from loadLlama import generator
from database import db

# Load LLM into LangChain
llm = HuggingFacePipeline(pipeline=generator)

# RAG Pipeline
rag = RetrievalQA.from_chain_type(
    llm=llm, chain_type='stuff',
    retriever=db.as_retriever()
)