from pydantic import BaseModel, Field
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserCreateResponse(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_admin: bool = Field(False)
    created_at: datetime
    updated_at: datetime
