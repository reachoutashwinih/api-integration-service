from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.auth.security import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter()

# -----------------------------
# Request Models (PUT HERE)
# -----------------------------
class UserRegister(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


# -----------------------------
# Fake DB (temporary)
# -----------------------------
fake_users_db = {}


# -----------------------------
# Route Handlers
# -----------------------------
@router.post("/login")
def login(user: UserLogin):

    stored_password = fake_users_db.get(user.username)

    if not stored_password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(user.password, stored_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        data={"sub": user.username}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.post("/register")
def register(user: UserRegister):

    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = hash_password(user.password)

    fake_users_db[user.username] = hashed_password

    return {
        "message": "User registered successfully"
    }