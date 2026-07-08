from fastapi import APIRouter, HTTPException
from backend.user import UserLogin,UserRegister,UserResponse
from backend.security import hash_password,verify_password
from backend.fakedb import fake_users_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserRegister):
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = hash_password(user.password)
    fake_users_db[user.email] = {
        "id": len(fake_users_db) + 1,
        "email": user.email,
        "hashed_password": hashed
    }
    return fake_users_db[user.email]

@router.post("/login")
def login(user: UserLogin):
    db_user = fake_users_db.get(user.email)
    if not db_user or not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "email": user.email}