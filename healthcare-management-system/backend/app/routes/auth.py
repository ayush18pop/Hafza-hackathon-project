from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.firebase_auth import firebase_auth

router = APIRouter()

class UserCredentials(BaseModel):
    email: str
    password: str

@router.post("/signup")
async def signup(user: UserCredentials):
    try:
        user_id = firebase_auth.create_user(user.email, user.password)
        return {"message": "User created successfully", "user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
async def login(user: UserCredentials):
    try:
        token = firebase_auth.login_user(user.email, user.password)
        return {"message": "Login successful", "token": token}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
