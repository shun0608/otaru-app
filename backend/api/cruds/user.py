from sqlalchemy.orm import Session
from bcrypt import hashpw, gensalt

import api.models.user as user_model
import api.schemas.user as user_schema


def get_password_hash(password: str) -> str:
    return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")


def create_user(db: Session, user_create: user_schema.UserCreate) -> user_model.User:
    hashed_password = get_password_hash(user_create.password)
    user = user_model.User(
        name=user_create.name, email=user_create.email, password=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
