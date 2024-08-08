"""
This module contains a FastAPI application with two endpoints:
- `read_root`: Returns a welcome message.
- `read_item`: Returns an item with a specified ID and optional query string.
"""

from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import login, user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],  # 許可するオリジンをリストで指定
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router)
app.include_router(user.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
