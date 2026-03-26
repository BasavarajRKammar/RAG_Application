from langchain_openai import OpenAIEmbeddings
import os
from langchain_groq import ChatGroq
from fastapi import UploadFile,File
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')
os.environ['langchain_api_key'] = os.getenv('langchain_api_key')
def get_document(filepath: str):
    docs = PyPDFLoader(filepath)
    print('File path is=')
    print(filepath)
    docs_load = docs.load()
    rec_text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs_text_splitter = rec_text_splitter.split_documents(docs_load)
#     print(docs_text_splitter)
#     print(type(docs_text_splitter[0])) 
    embedding = HuggingFaceEmbeddings()
    vectorDB = Chroma.from_documents(
         documents=docs_text_splitter,
         embedding=embedding,
         persist_directory='db'
    )
    vectorDB.persist()
    print('Vector Db is created successfull')
    return vectorDB
    # collection = vectordb._collection

    # print("Vector count:", collection.count())
    # retriver = vectorDB.as_retriever()
    # print(retriver)
    # print('Retrieved succesfully')


    
    




