from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.schemas import (LoginRequest, TokenResponse,)

from app.auth.service import login_user
from app.auth.schemas import RegisterRequest
from app.auth.service import register_user
from app.database.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):

    try:

        token = login_user(
            db,
            request.email,
            request.password,
        )

        return TokenResponse(
            access_token=token
        )

    except ValueError as e:

        raise HTTPException(
            status_code=401,
            detail=str(e),
        )

@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
):
    try:
        user = register_user(
            db,
            request.username,
            request.email,
            request.password,
        )

        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
        
        
        