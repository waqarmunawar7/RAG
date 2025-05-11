import os 
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    allowed_host: List[str] = []
    app_name: str
    auth_key: str
    algorithm: str
    port:int
    env: str

    url: str
    llm_embeedings_model: str
    llm_model_name: str
    vectorstore: str
    vectorstore_path: str
    user_agent:  str



    class Config():
        env_file = '.env'



setting = Settings()