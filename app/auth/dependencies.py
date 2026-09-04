from jose import JWTError, jwt

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.auth.security import oauth2_scheme
from app.core.config import settings
from app.repositories.user_repository import UserRepository

ALGORITHM = "HS256"


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:

        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[ALGORITHM],
        )

        username = payload.get("username")

        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = UserRepository(db).get_by_username(username)

    if user is None:
        raise credentials_exception

    return user