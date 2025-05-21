import ollama
from transformers import pipeline
from config import setting
from ollama import Client
import requests

def combine_context(docs):
    cleaned_contexts = []
    for doc in docs:
        text = doc.page_content.strip()
        if len(text) > 20:
            cleaned_contexts.append(text)
    
    combined_text = " ".join(cleaned_contexts)
    cleaned_context = combined_text.replace("\n", " ").replace("  ", " ").strip()

    return cleaned_context

def classify_intent(text, intent_tree):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    top_labels = list(intent_tree.keys())
    top_result = classifier(text, top_labels)
    top_intent = top_result['labels'][0]

    sub_labels = intent_tree[top_intent]
    sub_result = classifier(text, sub_labels)
    sub_intent = sub_result['labels'][0]

    return {
        "top_level_intent": top_intent,
        "sub_level_intent": sub_intent,
        "confidence_scores": {
            "top_intent_score": round(top_result['scores'][0], 3),
            "sub_intent_score": round(sub_result['scores'][0], 3)
        }
    }

async def generate_answer(query, context , session_id=None, history=[]):
    context = combine_context(context)
    # intents = classify_intent(query, setting.intents)
    if not context or len(context.strip()) < 20:
        context = "[NO CONTEXT PROVIDED]"
        
    history_text = ""
    for item in history[-5:]: 
        history_text += f"{item['role'].capitalize()}: {item['content']}\n"

        

    prompt = f"""
    You are a helpful and precise AI assistant. Follow these guidelines carefully:
    1. Respond ONLY using the information provided in the given context and conversation history
    2. If the context doesn't contain sufficient information to answer the question, respond: "I don't have enough information to answer this question. Could you please provide more details or clarify your request?"
    3. Be concise yet thorough when information is available
    4. Maintain a professional and friendly tone
    5. Do not use phrases like 'Based on the context' or 'According to the provided information'."

    Context:
    {context}

    Question:
    {query}

    Please provide your best response based on these instructions:
    """ 
    # ollama_client = Client(host=setting.ollama_host)
    
    # response = ollama_client.generate(
    #     model="llama3.2:1b",
    #     prompt=prompt,
    #     stream=False,
    #     keep_alive=-1
    # )
    
    payload = {
        "model": "llama3.2:latest",
        "prompt": prompt,
        "stream": False,
        "keep_alive": -1
    }

    response = requests.post("http://localhost:11434/api/generate", json=payload)
    response.raise_for_status()  # raise error if request failed

    return response.json()['response']
    
    # return response['response']