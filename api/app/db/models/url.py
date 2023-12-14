from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    address = Column(String, index=True, unique=True)
    shorted = Column(String, index=True, unique=True)
    clicks = Column(Integer, default=0, nullable=True)
