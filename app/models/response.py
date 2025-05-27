from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Response(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    score = Column(Integer, nullable=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"))

    survey = relationship("Survey", back_populates="responses")
