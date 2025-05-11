import re

def clean_document(text: str) -> str:
    patterns = [
        r'Toggle Navigation.*?(?=Home|$)',  
        r'HomeAboutServicesContact Us.*?(?=\n|$)',  
        r'© Copyright.*?(?=\n|$)',  
        r'Go to Top', 
        r'Page load link',
        r'Skip to content'
    ]
    for pattern in patterns:
        text = re.sub(pattern, '', text, flags=re.DOTALL)

    text = re.sub(r'\n\s*\n+', '\n\n', text)

    return text.strip()

def preprocessing(doc):
        return clean_document(doc)