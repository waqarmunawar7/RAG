import os 
from pydantic_settings import BaseSettings
from typing import List , Dict

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
    topic_handling:List[str] = []
    intents: Dict[str, List[str]] = {
        'services': [
            "cloud",
            "devops",
            "infrastructure_management",
            "custom_software",
            "mobile_development",
            "staff_augmentation",
            "others"
        ],
        'company': [
            "about_us",
            "careers",
            "partners",
            "contact_us"
        ],
        'others': [
            "testimonials",
            "blog",
            "privacy_policy",
            "terms_conditions"
        ]
    }

    class Config():
        env_file = '.env'


setting = Settings()