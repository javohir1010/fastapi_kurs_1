from fastapi import APIRouter

from users.crud import create_user
from users.schemas import CreateUser


router = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router.post("")
async def email_validator(user: CreateUser):
    return create_user(user_in=user)
