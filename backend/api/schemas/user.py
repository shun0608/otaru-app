from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


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
