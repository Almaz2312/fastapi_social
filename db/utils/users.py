from sqlalchemy.orm import Session

from core.hashing import Hasher
from db.models.users import User, FollowModel
from schemas.users import UserCreate, Follow_Schema, Profile


def create_new_user(user: UserCreate, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    users = db.query(User).all()
    return users


def get_profile(current_user, db: Session):
    profile = db.query(User).get(id=current_user.id)
    return profile


def follow_user(follow: Follow_Schema, user_id: int,db: Session):
    follow_object = FollowModel(user_id=user_id, following_id=follow)
    db.add(follow_object)
    db.commit()
    db.refresh(follow_object)
    return follow_object


def get_following_users(current_user, db: Session):
    following_users = db.query(FollowModel).filter(user_id=current_user)
    return following_users


def get_follow_object(id: int, current_user, db: Session):
    follow_object = db.query(FollowModel).filter(user_id=current_user.id, following_id=id).first()
    return follow_object


def delete_follow_object(id: int, current_user, db: Session):
    follow_object = db.query(FollowModel).filter(user_id=current_user.id, following_id=id)
    if not follow_object:
        return 0
    follow_object.delete(synchronize_session=FollowModel)
    db.commit()
    return 1
