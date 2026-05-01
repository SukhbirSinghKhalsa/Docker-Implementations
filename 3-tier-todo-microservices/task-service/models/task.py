from sqlalchemy import Column, Integer, String, Boolean
from pydantic import BaseModel
from database import Base

class TaskDB(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    completed = Column(Boolean, default=False)

class TaskCreate(BaseModel):
    title: str
    completed: bool = False

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool
    class Config:
        from_attributes = True
