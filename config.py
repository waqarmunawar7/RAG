import os 
from pydantic_settings import BaseSettings
from typing import List , Tuple
from pydantic import Field


class Settings(BaseSettings):
    
    allowed_host: List[str] = []
    app_name: str
    auth_key: str 
    algorithm: str 
    port:int
    env: str
    ollama_host: str
    url: str
    llm_embeedings_model: str
    llm_model_name: str
    vectorstore: str
    vectorstore_path: str
    user_agent:  str
    org_name: str
    # topic_handling : List[str] = ["about_company", "services", "contact", "careers"]  
    topic_classification : bool
    intents: List[str] = ['contact_person' , 'others']
    
    mail_username : str
    mail_from : str
    mail_password : str
    mail_port : int 
    mail_server : str
    mail_starttls : bool
    mail_ssl_tls : bool
    
    inquiry_email : List[str]
    
    

    class Config():
        env_file = '.env'


setting = Settings()