from fastapi import APIRouter
from app.celery_app.tasks import compute_response_score

router = APIRouter()

@router.post("/")
async def submit_response():
    response_id = 1  # Placeholder
    compute_response_score.delay(response_id)
    return {"message": "Response submitted and scoring started."}