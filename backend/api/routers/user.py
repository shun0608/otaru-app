from fastapi import APIRouter, Depends

# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.user as user_crud
import api.schemas.user as user_schema
from api.db import get_async_session

router = APIRouter()


@router.post("/register", response_model=user_schema.UserCreateResponse)
async def create_user(
    user_body: user_schema.UserCreate, db: AsyncSession = Depends(get_async_session)
):
    return await user_crud.create_user(db, user_body)
