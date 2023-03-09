from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from ..dependencies import get_current_user, get_session, get_password_hash
from ..models.user_model import User, UserRead, UserReadWithDetails, UserCreate, UserUpdate
from .. import crud

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={401: {"description": "Unauthorized"}}
)


@router.get("/me", response_model=UserRead)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user


@router.patch("/me", response_model=UserRead)
def update_user(
    new_user: UserUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    db_user = crud.update_entity(session, current_user, new_user)
    return db_user


@router.get("/{user_id}", response_model=UserReadWithDetails)
def read_user_details(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, session: Session = Depends(get_session)):
    user.password = get_password_hash(user.password)
    db_user = User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
