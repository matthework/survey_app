from sqlalchemy.orm import Session
from app.models.survey import Survey
from app.schemas.survey import SurveyCreate


def create_survey(db: Session, survey: SurveyCreate, owner_id: int):
    db_survey = Survey(**survey.dict(), owner_id=owner_id)
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey


def get_surveys(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Survey).offset(skip).limit(limit).all()
