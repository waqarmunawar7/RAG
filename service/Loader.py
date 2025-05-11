from langchain_community.document_loaders.sitemap import SitemapLoader
from helper import get_urls
import requests
from bs4 import BeautifulSoup
from langchain.schema import Document


class WebLoader(SitemapLoader):
    
    def __init__(self , url: str):
        
        return super().__init__(url)
    


