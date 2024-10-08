"""
This module provides functionality to reset the database by dropping \
all tables and recreating them.
"""

from sqlalchemy import create_engine

from api.models.base import Base

DB_URL = "postgresql://user:password@db:5432/otaru"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
