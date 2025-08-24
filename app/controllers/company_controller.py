from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.schemas.company import CompanyResponse
from app.services.company_services import CompanyService


router = APIRouter()


@router.get("/companies", response_model=List[CompanyResponse])
def get_companies(db: Session = Depends(get_db)):

    service = CompanyService(db)
    companies = service.get_companies()
    return companies