from pydantic import BaseModel
from fastapi_users import schemas


class UserRead(schemas.BaseUser):
    name: str


class UserCreate(schemas.BaseUserCreate):
    name: str


class UserUpdate(schemas.BaseUserUpdate):
    pass


class UserResponseData(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True


class UserCreateResponse(BaseModel):
    status: str
    message: str
    user: UserResponseData
