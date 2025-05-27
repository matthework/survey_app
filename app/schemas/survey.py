from pydantic import BaseModel
from typing import Optional


class SurveyBase(BaseModel):
    title: str
    description: Optional[str] = None


class SurveyCreate(SurveyBase):
    pass


class SurveyOut(SurveyBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
