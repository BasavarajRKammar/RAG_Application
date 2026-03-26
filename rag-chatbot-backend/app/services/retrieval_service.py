from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
# def get_vectorDb():
#     embeddings = HuggingFaceEmbeddings()
#     vector_db = Chroma(
#          persist_directory="db",
#             embedding_function=embeddings
#     )
#     return vector_db
def get_vectorDb():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-mpnet-base-v2"
    )

    # Load existing vector DB from disk
    
    vector_db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    return vector_db
    # docs = vector_db.similarity_search("What is attention mechanism?")
    # for doc in docs:
    #  print(doc.page_content)
    