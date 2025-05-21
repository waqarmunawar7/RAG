import re

def clean_document(text: str) -> str:
    # patterns = [
    #     r'Toggle Navigation.*?(?=Home|$)',  
    #     r'HomeAboutServicesContact Us.*?(?=\n|$)',  
    #     r'© Copyright.*?(?=\n|$)',  
    #     r'Go to Top', 
    #     r'Page load link',
    #     r'Skip to content'
    # ]
    # for pattern in patterns:
    #     text = re.sub(pattern, '', text, flags=re.DOTALL)

    text = re.sub(r'\n\s*\n+', '\n\n', text)

    return text.strip()

def preprocessing(doc):
        return clean_document(doc)
    
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
