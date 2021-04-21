from api import app
from api.models import User
from api.auth import get_current_user
from fastapi import Depends

@app.post('/register', response_model = User.pydantic, tags=['User'])
async def register(user :User.login_pydantic):
    user_obj = await User.create(**user.dict(exclude_unset = True))
    return await User.pydantic.from_tortoise_orm(user_obj)

@app.get('/user/me', response_model = User.pydantic, tags=['User'])
async def current_user(user : User.login_pydantic = Depends(get_current_user)):
    return user
