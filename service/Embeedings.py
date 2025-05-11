from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import List
from langchain.docstore.document import Document

def embed_chunks(chunks: List[Document]):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    print('this is emndljkshadflakj')
    return embeddings