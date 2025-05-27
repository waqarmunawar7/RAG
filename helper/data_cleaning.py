import re
import unicodedata
import spacy

nlp = spacy.load("en_core_web_lg")

def remove_named_entities(text: str) -> str:
    doc = nlp(text)
    tokens = [
        token.text for token in doc
        if not token.ent_type_  
    ]
    return ' '.join(tokens)

import re
import unicodedata

def clean_and_preprocess_text(text: str) -> str:
    patterns = [
        r'Toggle Navigation.*?talk',
        r'HomeAboutServices.*?(?=(Data Engineering|Cloud Services|Custom Software|$))',
        r'HomeAboutServicesContact Us\+?\d{1,3}.*?(?=\n|$)',


        r'©.*?(All Rights Reserved|$)',
        r'Send your inquiry',
        r'Page load link',
        r'Go to Top',
        r'Get in touch',
        r'^\s*\d+\s*---\s*Content:',
        r'Lambda Logics',
        r'Skip to content',
        r'let’s talk',
        r'Schedule a Consultation Now',


        r'\+?\d[\d\s\-]{7,}',  
        r'\bContact Us\b',

        r'\b(Home|About|Services|Careers|Contact Us|Mobile App Development|Cloud Services and DevOps|Custom Software Development|Data Engineering|Information Security Services|Staff Augmentation Services)\b',
    ]

    for pattern in patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE | re.DOTALL)

    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r'<[^>]+>', '', text)

    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)

    text = re.sub(r'\n\s*\n+', '\n\n', text)
    text = re.sub(r'^\s*[-•*]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'[^\w\s.,;:?!\'"-]', '', text)

    text = re.sub(r'\s+', ' ', text).strip()
    text = remove_named_entities(text)
    
    return text.strip()


def preprocessing(doc):
        return clean_and_preprocess_text(doc)
    
import re

def clean_response(text: str) -> str:
    patterns = [
        r"(?i)^based on the provided context,.*?:\s*",  
        r"(?i)^according to the provided context,?\s*",
        r"(?i)^here (is|are) (a|the)? ?(concise|brief)? ?(answer|summary):?\s*",
    ]
    
    for pattern in patterns:
        text = re.sub(pattern, "", text.strip())
    return text.strip()
