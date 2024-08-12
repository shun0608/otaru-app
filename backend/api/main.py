"""
This module contains a FastAPI application with two endpoints:
- `read_root`: Returns a welcome message.
- `read_item`: Returns an item with a specified ID and optional query string.
"""

from typing import Union

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.db import User
from api.schemas.user import UserCreate, UserRead, UserUpdate
from api.services.user_service import auth_backend, current_active_user, fastapi_users

# from api.routers import auth, user

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

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
