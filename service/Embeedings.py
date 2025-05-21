from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import List
from langchain.docstore.document import Document

def embed_chunks():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings