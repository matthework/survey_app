from fastapi import FastAPI
from app.api.routes import survey, response
from app.core.config import settings

app = FastAPI(title="Survey App")

app.include_router(survey.router, prefix="/surveys", tags=["surveys"])
app.include_router(response.router, prefix="/responses", tags=["responses"])