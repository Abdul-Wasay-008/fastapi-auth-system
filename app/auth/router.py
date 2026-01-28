from fastapi import APIRouter, HTTPException
from app.auth.schemas import UserCreate, Token
from app.auth.service import register_user, authenticate_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def signup(user: UserCreate):
    created = register_user(user.email, user.password)
    if not created:
        raise HTTPException(status_code=400, detail="User already exists")
    return {"msg": "User created successfully"}

@router.post("/login", response_model=Token)
def login(user: UserCreate):
    token = authenticate_user(user.email, user.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token}
