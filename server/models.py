from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
Base = declarative_base()
class Message(Base):
    __tablename__ = 'essages'
    id = Column(Integer, primary_key=True)
    body = Column(String)
    username = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())