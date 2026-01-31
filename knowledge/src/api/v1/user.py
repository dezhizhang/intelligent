from fastapi import APIRouter

from src.services.user_service import UserService

router = APIRouter(tags=["user"],prefix="/user")

@router.get("/")
def get_user():
    return UserService(db=AsyncSession)