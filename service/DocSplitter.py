import os
import re
from typing import List , Dict
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from helper import data_cleaning
from collections import defaultdict
# class TopicDict(defaultdict):
#     def __init__(self):
#         super().__init__(list)
#         self.about: List[str] = []
#         self.services: List[str] = []
#         self.contact: List[str] = []
#         self.careers: List[str] = []

def chunk_documents_from_txt(file_path: str) -> List[Document]:
    with open(file_path, "r", encoding="utf-8") as f:
        raw = f.read()

    docs_raw = raw.split("--- Document")
    cleaned_docs = [data_cleaning.preprocessing(doc) for doc in docs_raw if doc.strip()]
    documents = [Document(page_content=doc) for doc in cleaned_docs]

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    return chunks

# def chunk_multiple_documents_from_txt(file_path: str) -> Dict:
#     with open(file_path , "r" , encoding="utf-8") as f:
#         raw = f.read()
#     topicDict = TopicDict()
#     docs_raw = raw.split("--- Document")
#     cleaned_docs = [preprocessing(doc) for doc in docs_raw if doc.strip()]
#     print(len(cleaned_docs))
#     splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
#     for doc in cleaned_docs:
#         with open('doc.txt','a') as f:
#             f.write( classify_message(doc) + " --> " + doc)
#             f.write("\n")
#             f.write("\n")
#             f.write("\n")
#         topicDict[classify_message(doc)].append(doc)
#     print(topicDict.keys())
#     # topic_chunks = TopicDict()
#     # for topic  , clean_docs in topicDict.items():
#     #     documents = [Document(page_content=doc) for doc in clean_docs]
#     #     chunks = splitter.split_documents(documents)
#     #     topic_chunks[topic].append(chunks)
#     # print(topic_chunks.keys())
#     # return topic_chunks
        
        
        
    