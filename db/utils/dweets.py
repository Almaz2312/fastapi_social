from sqlalchemy.orm import Session

from schemas.dweets import Dweet_Schema
from db.models.dweets import Dweet


async def list_all_dweets(db: Session):
    dweets = db.query(Dweet).all()
    return dweets


async def create_dweet(dweet: Dweet_Schema, db: Session, author_id: int):
    dweet_object = Dweet(**dweet.dict(), author_id=author_id)
    db.add(dweet_object)
    db.commit()
    db.refresh(dweet_object)
    return dweet_object

