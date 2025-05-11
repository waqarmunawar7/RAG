import os
import re
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from helper import data_cleaning



def chunk_documents_from_txt(file_path: str) -> List[Document]:
    with open(file_path, "r", encoding="utf-8") as f:
        raw = f.read()

    docs_raw = raw.split("--- Document")
    print(len(docs_raw))
    cleaned_docs = [data_cleaning.preprocessing(doc) for doc in docs_raw if doc.strip()]
    documents = [Document(page_content=doc) for doc in cleaned_docs]

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    return chunks