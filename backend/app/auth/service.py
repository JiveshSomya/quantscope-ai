from sqlalchemy.orm import Session

from app.auth.security import hash_password
from app.models.user import User


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