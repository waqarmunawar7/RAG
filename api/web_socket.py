from fastapi import WebSocket , WebSocketDisconnect , status
from config import setting
from service.VectorStore import create_vector_store
import traceback
from config import setting
import sys
from service.Retriver import Retriever
from service.topic_classification import classify_message
import os
from service.generate_answer import generate_answer
import json
from datetime import datetime


user_sessions = {}

CHAT_DIR = "chat_data"
os.makedirs(CHAT_DIR, exist_ok=True)



def format_timestamp():
    return datetime.now().strftime("%Y-%m-%d")

def get_session_filename(session_id: str, date_str: str) -> str:
    safe_session = session_id.replace(":", "_")
    return os.path.join(CHAT_DIR, f"{safe_session}_{date_str}.json")





async def chat(websocket:WebSocket):
    try:
        if setting.env != 'dev':
            origin = websocket.headers.get('origin')
            if origin in setting.allowed_host:
                pass
            else:
                await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
                return
            
        if len(os.listdir(setting.vectorstore_path))==0:
            await create_vector_store(setting.org_name)
            
            
        await websocket.accept()
        session_id = f"{websocket.client.host}:{websocket.client.port}"
        date_str = format_timestamp()
        session_filename = get_session_filename(session_id, date_str)
        user_sessions.setdefault(session_id, [])
        
        while True:
            query = await websocket.receive_text()
            retriever_instance = Retriever(classify_message(query))
            context = retriever_instance.vector_store_retriever(query)
            history = user_sessions[session_id]
            answer = await generate_answer(query,context,session_id,history)
            
            
            history.append({"role": "user", "content": query})
            history.append({"role": "assistant", "content": answer})
            with open(session_filename, "w") as f:
                json.dump(history, f, indent=2)
                
            await websocket.send_text(json.dumps({'message': answer}))
            
    except WebSocketDisconnect:
        print('client disconnected')
        
    except Exception as e:
        print('Error type:', e.__class__.__name__)
        print('Error message:', str(e))
        exc_type, exc_value, exc_tb = sys.exc_info()
        tb = traceback.extract_tb(exc_tb)
        for line in tb:
            print(f"File: {line.filename}, Line: {line.lineno}, in {line.name}")
            print(f"  Code: {line.line}")
        await websocket.close()
