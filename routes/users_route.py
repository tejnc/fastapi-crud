from fastapi import APIRouter, Request
from models.users import Users
from json import loads


from functions.add_user import add_user

router = APIRouter()

@router.get("/users/")
async def read_users():
    return [{"username": "Tej"}, {"username": "sagar"}]


@router.get("/users/{username}")
async def read_user(username: str):
    return {"username": username}


@router.post("/add/")
async def add(request: Request):
    body = await request.json()
    user = add_user(body)
    return {"message": "success", "data": loads(user.to_json())}