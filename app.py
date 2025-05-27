from fastapi import FastAPI 
from starlette.routing import Route
# from config import setting
# from starlette.routing import WebSocketRoute
# from api.web_socket import chat
from api.chat_post import handle_post
from api.handle_inquiry import inquiry
from fastapi.middleware.cors import CORSMiddleware
from profyle.fastapi import ProfyleMiddleware

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             
    allow_credentials=True,
    allow_methods=["*"],               
    allow_headers=["*"],               
)
# app.router.routes.append(WebSocketRoute('/ws/chat',endpoint=chat))
app.router.routes.append(Route("/chat/submit", endpoint=handle_post, methods=["POST"]))
app.router.routes.append(Route('/inquiry/submit', endpoint=inquiry , methods=['POST']))

