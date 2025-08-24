from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.config.database import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    address = Column(String(255), nullable=True)
    admin_user_id = Column(Integer, ForeignKey("admin_users.id", ondelete="CASCADE"), nullable=False, index=True)
    # admin_user_id = Column(Integer)
    created_at = Column(DateTime, nullable=True, default=func.now())
    updated_at = Column(DateTime, nullable=True, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)  # For soft deletes
    logo = Column(String(255), nullable=True)

    # Relationship to AdminUser (you'll need to create this model too)
    # admin_user = relationship("AdminUser", back_populates="companies")
    # Relationship to AdminUser
    admin_user = relationship("AdminUser", back_populates="companies")