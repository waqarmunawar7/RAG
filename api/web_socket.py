from fastapi import WebSocket , WebSocketDisconnect , status
from config import setting
from service.VectorStore import create_vector_store
import traceback
import sys


import os

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
            await create_vector_store('lambdalogics')
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            print('Data -> ' , data)
            await websocket.send_text(f"You said: {data}")
    except WebSocketDisconnect:
        print('client disconnected')
    except Exception as e:
        print('Error type:', e.__class__.__name__)
        exc_type, exc_value, exc_tb = sys.exc_info()
        tb = traceback.extract_tb(exc_tb)
        for line in tb:
            print(f"File: {line.filename}, Line: {line.lineno}, in {line.name}")
            print(f"  Code: {line.line}")
        await websocket.close()
