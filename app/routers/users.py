from fastapi import APIRouter, Depends
from ..dependencies import get_current_user
from ..models import User, UserRead

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={401: {"description": "Unauthorized"}}
)


@router.get("/me", response_model=UserRead)
async def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user
