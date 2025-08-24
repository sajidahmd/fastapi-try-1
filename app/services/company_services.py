from fastapi import HTTPException, status
from sqlalchemy.orm import Session, joinedload

from app.models.company import Company


class CompanyService:
    def __init__(self,db:Session):
        self.db = db

    def get_companies(self):
        return self.db.query(Company).options(joinedload(Company.admin_user)).all()