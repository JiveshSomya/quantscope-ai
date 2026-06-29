from sqlalchemy.orm import Session

from app.auth.security import hash_password
from app.models.user import User

from app.auth.security import (
    verify_password,
    create_access_token,
)

def login_user(
    db: Session,
    email: str,
    password: str,
):

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if user is None:
        raise ValueError("Invalid credentials")

    if not verify_password(
        password,
        user.hashed_password,
    ):
        raise ValueError("Invalid credentials")

    token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    return token


def register_user(
    db: Session,
    username: str,
    email: str,
    password: str,
):
    existing = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if existing:
        raise ValueError("User already exists")

    user = User(
        username=username,
        email=email,
        hashed_password=hash_password(password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user