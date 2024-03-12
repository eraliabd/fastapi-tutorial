from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./fastdb.db"

SQLALCHEMY_DATABASE_URL = "postgresql://test:test123@localhost:5432/sql_app"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    # `check_same_thread` is an argument specific to sqlite
    # SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
