from datetime import datetime, timedelta
from os import environ
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from ..dependencies import authenticate_user, create_access_token
from ..models.token_model import Token

router = APIRouter(
    tags=["Authentication"]
)


@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    expire = datetime.utcnow() + \
        timedelta(minutes=float(environ["ACCESS_TOKEN_EXPIRE_MINUTES"]))
    access_token = create_access_token(
        data={"sub": user.username, "exp": expire})

    return Token(
        access_token=access_token,
        token_type="bearer",
        expires=expire
    )
