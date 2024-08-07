from fastapi import APIRouter, HTTPException, Depends, status
from datetime import timedelta
from ...schemas.user_schemas import Token, User, LoginData, ChangePassword
from ...services.user_service import *

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(login_data: LoginData):
    print(f"Login attempt for username: {login_data.username}")
    user = authenticate_user(login_data.username, login_data.password)
    if not user:
        print(f"Authentication failed for username: {login_data.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    print(f"Login successful for username: {login_data.username}")
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/logout")
async def logout(current_user: User = Depends(get_current_user)):
    return {"message": "Successfully logged out"}

@router.post("/change-password")
async def change_password(change_pw: ChangePassword):
    user = authenticate_user(change_pw.username, change_pw.old_password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or old password",
        )
    hashed_password = get_password_hash(change_pw.new_password)
    users_collection.update_one(
        {"username": user.username},
        {"$set": {"hashed_password": hashed_password}}
    )
    print(f"Password changed successfully for username: {change_pw.username}")
    return {"message": "Password changed successfully"}

@router.get("/user/profile", response_model=User)
async def get_profile(current_user: User = Depends(get_current_user)):
    return current_user