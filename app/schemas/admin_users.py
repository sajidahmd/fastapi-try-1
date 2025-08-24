from typing import Optional

from pydantic import BaseModel


class AdminUserInfo(BaseModel):
    id: int
    name: str


    class Config:
        from_attributes = True