import datetime

from db.base_class import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Dweet(Base):
    id = Column(Integer, primary_key=True, index=True)
    body = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship('User', back_populates='dweets')
    created_at = Column(DateTime, default=datetime.datetime.now().date())


