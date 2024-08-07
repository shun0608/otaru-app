"""
This module sets up the SQLAlchemy engine and session for the application.
It includes the database URL configuration, engine creation, session setup,
and a function to provide a database session.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql://user:password@db:5432/otaru"

db_engine = create_engine(DB_URL, echo=True)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()


def get_db():
    """
    Provide a transactional scope around a series of operations.

    Yields:
        session (Session): SQLAlchemy session object.
    """
    with db_session() as session:
        yield session
