import streamlit as st
import logging

from loadLlama import generator
from validation import validate_file
from uploader import add_file_to_db

logging.basicConfig(filename='app.log', level=logging.INFO)

# App title
st.set_page_config(page_title="🦙💬 AI Chatbot")

with st.sidebar:
    st.title('🦙💬 AI Chatbot')    

    temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
    top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
    max_length = st.sidebar.slider('max_length', min_value=32, max_value=128, value=120, step=8)
    url = st.sidebar.text_input("Enter a URL")
    st_document = st.sidebar.file_uploader("Upload a File")
    st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-a-llama-2-chatbot/)!')

    validation_result, file_ext = validate_file(st, st_document)

    if validation_result:
            logging.info(f"Upload file is valid.")
            add_file_to_db(st,st_document, file_ext)
        
        

