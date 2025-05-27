from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from config import setting
class Retriever:
    def __init__(self):
        embeddings_model = HuggingFaceEmbeddings(model_name=setting.llm_embeedings_model)
        self.vectorstore = FAISS.load_local('knowledge_bases/' + setting.org_name , embeddings=embeddings_model, index_name="index", allow_dangerous_deserialization=True)
        
        
    def vector_store_retriever(self,query):
        retriver = self.vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 3, "fetch_k": 20})
        # retriver = self.vectorstore.as_retriever( search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.65})
        return retriver.invoke(query)