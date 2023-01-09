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
    dweets = relationship('Dweet', back_populates="author")
    # profile = relationship('FollowModel', back_populates='follower')
    # following = relationship('FollowModel', back_populates='following')


class FollowModel(Base):
    id = Column(Integer, primary_key=True, index=True)

    follower_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    follower = relationship(User, backref='follower', foreign_keys=[follower_id])

    following_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    following = relationship(User, backref='following', foreign_keys=[following_id])
