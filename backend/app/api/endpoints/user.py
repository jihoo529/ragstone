from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from passlib.context import CryptContext
from jose import JWTError
import jwt
from datetime import datetime, timedelta
from typing import Optional
from datetime import datetime, timezone

router = APIRouter()

# MongoDB connection
client = MongoClient("mongodb://mongodb:27017")
db = client["ragstone"]
users_collection = db["users"]

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT settings
SECRET_KEY = "your-secret-key"  # Change this to a secure secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic models
class UserInDB(BaseModel):
    username: str
    hashed_password: str

class User(BaseModel):
    username: str

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class ChangePassword(BaseModel):
    username: str
    old_password: str
    new_password: str

class LoginData(BaseModel):
    username: str
    password: str

# Helper functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str):
    user = users_collection.find_one({"username": username})
    if user:
        return UserInDB(**user)

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        print("not user")
        return False
    if not verify_password(password, user.hashed_password):
        print("wrong password")
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# API endpoints
@router.post("/login", response_model=Token)
async def login(login_data: LoginData):
    print(f"Login attempt for username: {login_data.username}")  # Debug log
    user = authenticate_user(login_data.username, login_data.password)
    if not user:
        print(f"Authentication failed for username: {login_data.username}")  # Debug log
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    print(f"Login successful for username: {login_data.username}")  # Debug log
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/logout")
async def logout(current_user: User = Depends(get_current_user)):
    # In a real-world scenario, you might want to invalidate the token here
    return {"message": "Successfully logged out"}

@router.post("/change-password")
async def change_password(change_pw: ChangePassword):
    print(f"Change password attempt for username: {change_pw.username}")
    # if change_pw.username != current_user.username:
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN,
    #         detail="Cannot change password for another user",
    #     )
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

# You can add more endpoints for user registration, settings update, etc.