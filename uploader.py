import logging
import fitz  # PyMuPDF
import io

from docx import Document
from database import collection
from embedding import embedding_model
from langchain.text_splitter import CharacterTextSplitter

logging.basicConfig(filename='uploader.log', level=logging.INFO)

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

def extract_text_pdf(file_content):
    logging.info(f"Extract .pdf")
    with fitz.open(stream=file_content, filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
        logging.info(f"PDF content: {text}")    
        return text

def extract_text_txt(file_content):
    logging.info(f"Extract .txt")
    # Assuming file_content is a BytesIO object
    text = file_content.getvalue().decode('utf-8')
    logging.info(f"TXT content: {text}")
    return text

def extract_text_docx(file_content):
    logging.info(f"Extract docx")
    doc = Document(file_content)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    logging.info(f"DOCX content: {text}")    
    return text

def add_file_to_db(st,st_document, file_ext):
    logging.info(f"add_file_to_db()")

    # Convert the uploaded file to a bytes stream
    file_content = io.BytesIO(st_document.getvalue())
    
    if file_ext == '.pdf':
        logging.info(f"File type: .pdf")
        text = extract_text_pdf(file_content)
        docs = text_splitter.split_documents(text)
    elif file_ext == '.txt':
        logging.info(f"File type: .txt")
        text = extract_text_txt(file_content)
        docs = text_splitter.split_documents(text)
    elif file_ext == '.docx':
        logging.info(f"File type: .docx")
        text = extract_text_docx(file_content)
        docs = text_splitter.split_documents(text)
    else:
        st.error("Unsupported file type.")
        return
    
    logging.info(f"Docs value: {docs}")
    
    logging.info(f"Add docs successfull to DB")