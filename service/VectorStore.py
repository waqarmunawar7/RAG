# from .Loader import WebLoader
from langchain_community.document_loaders import WebBaseLoader 
from helper import get_urls
from helper import data_cleaning
from langchain.docstore.document import Document
from .DocSplitter import chunk_documents_from_txt
import os
from .Embeedings import embed_chunks
from langchain_community.vectorstores import FAISS
from config import setting
from typing import List


    
def store_chunks_to_faiss(chunks: List[Document], embeddings, index_name: str):
    vectorstore_path = os.path.join("knowledge_bases", index_name)
    os.makedirs(vectorstore_path, exist_ok=True)

    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(vectorstore_path)
    print(f"✅ Vector store saved at: {vectorstore_path}")

async def create_vector_store(index_name: str):
    urls = get_urls.Helper.get_all_valid_links(setting.url)
    
    if urls:
        print("URLs to be loaded:", urls)
        loader = WebBaseLoader(urls)
        docs = loader.load()
        output_file = f"sources/raw_docs.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            for i, doc in enumerate(docs, 1):
                f.write(f"--- Document {i} ---\n")
                f.write(doc.page_content + "\n\n")
        # if(setting.topic_classification):
        #     chunks = chunk_multiple_documents_from_txt(output_file)
        #     # embeddings = embed_chunks()
        #     # for index_name  in setting.topic_handling: 
        #     #     print(index_name)
        #     #     store_chunks_to_faiss(chunks[index_name], embeddings, index_name)
        # else: 
        chunks = chunk_documents_from_txt(output_file)
        embeddings = embed_chunks()
        store_chunks_to_faiss(chunks, embeddings, index_name)