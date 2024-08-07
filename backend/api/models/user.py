"""
This module contains SQLAlchemy ORM definitions and setup for an application.
It includes the User and Post models and the database session configuration.
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime, timezone, timedelta

from api.db import Base

# 日本時間 (JST) は UTC+9
JST = timezone(timedelta(hours=9))


def jst_now():
    return datetime.now(JST)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=jst_now)
    updated_at = Column(DateTime(timezone=True), default=jst_now, onupdate=jst_now)
