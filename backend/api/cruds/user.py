"""
This module provides functionalities to manage user.
"""

from sqlalchemy.orm import Session
from bcrypt import hashpw, gensalt
from fastapi.responses import JSONResponse
from fastapi import status

import api.models.user as user_model
import api.schemas.user as user_schema


def get_password_hash(password: str) -> str:
    return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")


def create_user(db: Session, user_create: user_schema.UserCreate) -> user_model.User:

    existing_user = (
        db.query(user_model.User)
        .filter(user_model.User.email == user_create.email)
        .first()
    )

    if existing_user:
        response_content = {
            "status": "error",
            "message": "duplicate",
        }
        return JSONResponse(
            content=response_content, status_code=status.HTTP_400_BAD_REQUEST
        )

    hashed_password = get_password_hash(user_create.password)
    user = user_model.User(
        name=user_create.name, email=user_create.email, password=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    response_content = {
        "status": "success",
        "message": "User registered successfully",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
        },
    }

    return JSONResponse(content=response_content, status_code=status.HTTP_201_CREATED)
