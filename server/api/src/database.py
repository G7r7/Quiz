from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path

import os

SQLALCHEMY_DATABASE_URL = "postgresql://" + os.getenv('POSTGRES_USER') + ":" + os.getenv('POSTGRES_PASSWORD') + "@db/quiz"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()