from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import Settings

db = Settings().database

SQLALCHEMY_DATABASE_URL = f'postgresql://{db.user}:{db.password}@{db.host}:{db.port}/{db.schema}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
