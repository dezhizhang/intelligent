from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.mysql_db import get_db
from src.services.user_service import UserService

router = APIRouter(tags=["user"],prefix="/user")

@router.get("/")
async def get_all_user(db:AsyncSession = Depends(get_db())):
    user_service = UserService(db)
    await user_service.get_all()
    return []