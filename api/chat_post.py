from fastapi import status
from config import setting
from service.VectorStore import create_vector_store
import traceback
from config import setting
import sys
from service.Retriver import Retriever
from service.topic_classification import classify_message
import os
from service.generate_answer import generate_answer , combine_context
import json
from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi import Request, status

user_sessions = {}

CHAT_DIR = "chat_data"
os.makedirs(CHAT_DIR, exist_ok=True)


def format_timestamp():
    return datetime.now().strftime("%Y-%m-%d")

def get_session_filename(session_id: str, date_str: str) -> str:
    safe_session = session_id.replace(":", "_")
    return os.path.join(CHAT_DIR, f"{safe_session}_{date_str}.json")


async def handle_post(request: Request):
    data = await request.json()
    query = data.get("message")

    origin = request.headers.get("origin")

    if setting.env != 'dev':
        if origin not in setting.allowed_host:
            return JSONResponse(
                content={"detail": "Origin not allowed"},
                status_code=status.HTTP_403_FORBIDDEN
            )

    if len(os.listdir(setting.vectorstore_path)) == 0:
        await create_vector_store(setting.org_name)

    client_host = request.client.host
    session_id = f"{client_host}" 

    date_str = format_timestamp()
    session_filename = get_session_filename(session_id, date_str)
    user_sessions.setdefault(session_id, [])

    retriever_instance = Retriever(classify_message(query))
    context = retriever_instance.vector_store_retriever(query)
    history = user_sessions[session_id]

    answer = await generate_answer(query, context, session_id, history)

    history.append({"role": "user", "content": query})
    history.append({"role": "assistant", "content": answer , "context": combine_context(context)})
    with open(session_filename, "w") as f:
        json.dump(history, f, indent=2)

    return JSONResponse(content={"message": answer})
