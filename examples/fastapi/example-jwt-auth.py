"""JWT authentication example for AI backends.

Prerequisites: pip install fastapi uvicorn pyjwt python-multipart

Run: uvicorn example-jwt-auth:app --reload
"""

from __future__ import annotations

from datetime import UTC, datetime, timedelta

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI(title="JWT Auth Example")

SECRET_KEY = "change-me-in-production-use-secrets-manager"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

FAKE_USERS = {"engineer@example.com": "hashed-password-placeholder"}


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class User(BaseModel):
    email: str


def create_access_token(subject: str, expires_delta: timedelta | None = None) -> str:
    expire = datetime.now(UTC) + (expires_delta or timedelta(minutes=15))
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    email = decode_token(token)
    return User(email=email)


@app.post("/token", response_model=Token)
async def login(form: OAuth2PasswordRequestForm = Depends()):
    if form.username not in FAKE_USERS:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(
        form.username,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return Token(access_token=token)


@app.get("/v1/me")
async def read_me(user: User = Depends(get_current_user)):
    return {"email": user.email}
