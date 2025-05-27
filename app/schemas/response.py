from pydantic import BaseModel
from typing import Optional


class ResponseBase(BaseModel):
    content: str


class ResponseCreate(ResponseBase):
    survey_id: int


class ResponseOut(ResponseBase):
    id: int
    score: Optional[int] = None

    class Config:
        orm_mode = True
