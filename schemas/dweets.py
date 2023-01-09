from datetime import datetime
from pydantic import BaseModel


class Dweet_Schema(BaseModel):
    body: str
    created_at: datetime = datetime.now().date()

    class Config:
        orm_mode =True
