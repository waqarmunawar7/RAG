from fastapi import FastAPI
from config import setting
from starlette.routing import WebSocketRoute
from api.web_socket import chat

import secrets



app = FastAPI()
app.router.routes.append(WebSocketRoute('/ws/chat',endpoint=chat))
