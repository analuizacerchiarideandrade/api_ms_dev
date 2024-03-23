from sqlalchemy import create_engine
import sqlalchemy.orm
from db.config import settings
from fastapi import Depends
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL is ",SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# O mecanismo acima cria um objeto adaptado para PostgreSQL, bem como um objeto que estabelecerá um Conexão 


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    #3
