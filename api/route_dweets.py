from typing import List
from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from schemas.dweets import Dweet_Schema
from schemas.users import Follow_Schema, Profile
from api.route_login import get_current_user_form_token
from db.utils.dweets import list_all_dweets, create_dweet
from db.utils.users import follow_user, get_following_users, get_follow_object, delete_follow_object
from db.models.users import User

router = APIRouter()


@router.get('/dashboard/', response_model=List[Dweet_Schema])
async def get_dweets(db: Session = Depends(get_db)):
    dweets = list_all_dweets(db=db)
    return dweets


@router.post('/dashboard/', response_model=Dweet_Schema)
async def post_dweet(dweet: Dweet_Schema, db: Session = Depends(get_db),
               current_user: User = Depends(get_current_user_form_token)):
    dweet = create_dweet(dweet=dweet, db=db, author_id=current_user)
    return dweet


@router.post('/follow/', response_model=Follow_Schema)
async def follow(follow: Follow_Schema, current_user: User = Depends(get_current_user_form_token),
           db: Session = Depends(get_db)):
    following = follow_user(follow_ing=follow, user_id=current_user, db=db)
    return following


@router.delete('/unfollow/{following_id: id}')
async def unfollow(id: int, current_user: User = Depends(get_current_user_form_token),
             db: Session = Depends(get_db)):
    follow_object = get_follow_object(id=id, current_user=current_user, db=db)
    if not follow_object:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    delete_follow_object(id=id, current_user=current_user, db=db)
    return {'msg': f'You have unfollowed user id {id}'}


@router.get('/follow/', response_model=List[Profile])
async def get_following(current_user: User = Depends(get_current_user_form_token),
                  db: Session = Depends(get_db)):
    following_users = get_following_users(current_user=current_user, db=db)
    return following_users
