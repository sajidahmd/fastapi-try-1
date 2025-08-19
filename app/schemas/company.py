from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class CompanyBase(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    address: Optional[str] = Field(None, max_length=255)
    admin_user_id: int = Field(..., description="ID of the admin user")


class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    address: Optional[str] = Field(None, max_length=255)
    admin_user_id: Optional[int] = None
