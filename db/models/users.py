from db.base_class import Base
from sqlalchemy import Boolean, Column, Integer, ForeignKey
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    jobs = relationship("Job", back_populates="owner")
    dweets = relationship('Dweet', back_populates="author")
    profile = relationship('FollowModel', back_populates='user')
    following = relationship('FollowModel', back_populates='following')


class FollowModel(Base):
    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship('User', back_populates='profile')

    following_id = Column(Integer, ForeignKey('User', ondelete='CASCADE'))
    following = relationship('User', back_populates='following')
