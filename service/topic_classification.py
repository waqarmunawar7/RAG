from transformers import pipeline, Pipeline
from typing import List, Tuple
from config import setting
def load_classifier() -> Pipeline:
    model = "facebook/bart-large-mnli"
    return pipeline("zero-shot-classification", model=model)

classifier = load_classifier()

def classify_message(msg: str,) -> str:
    if not msg.strip():
        return ([], [])

    try:
        result = classifier(msg, setting.topic_handling )
        return result['labels'][0]
    except Exception as e:
        print(f"Error during classification: {e}")
        return ([], [])