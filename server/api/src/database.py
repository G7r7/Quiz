from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pathlib import Path

import os

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

SQLALCHEMY_DATABASE_URL = "postgresql://" + os.getenv('POSTGRES_USER') + ":" + os.getenv('POSTGRES_PASSWORD') + "@db/quiz"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()