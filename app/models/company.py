from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from app.config.database import Base

class Company(Base):
    __tablename__ = "companies"
