"""
This module contains a FastAPI application with two endpoints:
- `read_root`: Returns a welcome message.
- `read_item`: Returns an item with a specified ID and optional query string.
"""

from typing import Union

from fastapi import FastAPI

DATABASE_URL = "postgres://user:password@db/otaru"

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
