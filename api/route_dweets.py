from typing import List
from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from schemas.dweets import Dweet_Schema
from schemas.users import Follow_Schema, Profile, ShowFollow
from api.route_login import get_current_user_form_token
from db.utils.dweets import list_all_dweets, create_dweet
from db.utils.users import follow_user, get_following_users, get_follow_object, delete_follow_object
from db.models.users import User

router = APIRouter()


@router.get('/dashboard/', response_model=List[Dweet_Schema])
async def get_dweets(db: Session = Depends(get_db)):
    dweets = await list_all_dweets(db=db)
    return dweets


@router.post('/dashboard/', response_model=Dweet_Schema)
async def post_dweet(dweet: Dweet_Schema, db: Session = Depends(get_db),
               current_user: User = Depends(get_current_user_form_token)):
    dweet = await create_dweet(dweet=dweet, db=db, author_id=current_user.id)
    return dweet


@router.post('/follow/', response_model=Follow_Schema)
async def follow(follow: Follow_Schema, current_user: User = Depends(get_current_user_form_token),
           db: Session = Depends(get_db)):
    following = await follow_user(follow=follow, user_id=current_user.id, db=db)
    if not following:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='')
    return following


@router.delete('/unfollow/{id}')
async def unfollow(id: int, current_user: User = Depends(get_current_user_form_token),
             db: Session = Depends(get_db)):
    follow_object = await get_follow_object(id=id, current_user=current_user, db=db)
    if not follow_object:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if follow_object.follower_id == current_user.id or current_user.is_superuser:
        await delete_follow_object(id=id, current_user=current_user, db=db)
        return {'msg': f'You have unfollowed user id {id}'}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail='You are not permitted!!!')


@router.get('/follow/', response_model=List[ShowFollow])
async def get_following(current_user: User = Depends(get_current_user_form_token),
                  db: Session = Depends(get_db)):
    following_users = await get_following_users(current_user=current_user, db=db)
    return following_users
