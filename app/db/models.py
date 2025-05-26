# app/db/models.py

from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CaseTask(Base):
    __tablename__ = "case_tasks"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String, index=True)
    title = Column(String)
    summary = Column(Text)
    status = Column(String)
