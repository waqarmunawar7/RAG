from fastapi import FastAPI 
from starlette.routing import Route
# from config import setting
# from starlette.routing import WebSocketRoute
# from api.web_socket import chat
from api.chat_post import handle_post
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
    # add other origins like production URL if needed
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             # Or ["*"] to allow all origins (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],               # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],               # Allow all headers
)
# app.router.routes.append(WebSocketRoute('/ws/chat',endpoint=chat))
app.router.routes.append(Route("/chat/submit", endpoint=handle_post, methods=["POST"]))