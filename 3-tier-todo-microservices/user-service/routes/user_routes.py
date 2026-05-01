from fastapi import APIRouter
from models.user import User

router = APIRouter()
users_db = [{"id": 1, "username": "default_user"}]

@router.get("/")
def list_users():
    return users_db
