import logging
import fitz  # PyMuPDF
import io

from docx import Document
from database import db
from embedding import embedding_model
from langchain.text_splitter import CharacterTextSplitter

logging.basicConfig(filename='laodfiles.log', level=logging.INFO)

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

def extract_text_pdf(file_content):
    with fitz.open(stream=file_content, filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
        return text

def extract_text_txt(file_content):
    # Assuming file_content is a BytesIO object
    text = file_content.getvalue().decode('utf-8')
    return text

def extract_text_docx(file_content):
    doc = Document(file_content)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def add_file_to_db(st,st_document, file_ext):
    # Convert the uploaded file to a bytes stream
    file_content = io.BytesIO(st_document.getvalue())
    
    if file_ext == '.pdf':
        text = extract_text_pdf(file_content)
        docs = text_splitter.split_documents(text)
    elif file_ext == '.txt':
        text = extract_text_txt(file_content)
        docs = text_splitter.split_documents(text)
    elif file_ext == '.docx':
        text = extract_text_docx(file_content)
        docs = text_splitter.split_documents(text)
    else:
        st.error("Unsupported file type.")
        return
    
    db.from_texts(docs, embedding_model)