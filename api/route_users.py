from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from api.route_login import get_current_user_form_token
from db.models.users import User
from schemas.users import UserCreate, Profile
from db.utils.users import create_new_user, get_users, get_profile
from db.session import get_db

router = APIRouter()


@router.post("/register/", response_model=Profile)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user


@router.get('/profile_list/', response_model=List[Profile])
async def list_users(db: Session = Depends(get_db)):
    users = get_users(db=db)
    return users


@router.get('/profile', response_model=Profile)
async def profile(current_user: User = Depends(get_current_user_form_token), db: Session = Depends(get_db)):
    profile = get_profile(current_user, db)
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Profile with this user id {current_user.id} was not found')
    return profile
