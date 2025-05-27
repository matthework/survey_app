from fastapi import APIRouter, Depends
from app.core.auth0 import get_role_user

router = APIRouter()

@router.post("/", dependencies=[Depends(get_role_user(["admin"]))])
async def create_survey():
    return {"message": "Survey created"}