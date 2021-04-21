import json
from api import app
from api.models import User 
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

login_schema = OAuth2PasswordBearer(tokenUrl="shild")


async def authnicate_user(username : str, password : str):
    user = await User.get_or_none(name = username)
    if not user :
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail = "User Not Found")

    if not user.password == password:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail = "User Not Found")

    return user

async def get_current_user(token: str = Depends(login_schema)):
    if not token:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail = "Invalid Token")

    payload = json.loads(token)
    user = await authnicate_user(username = payload.get('name'), password = payload.get('password'))
    user_obj = await User.pydantic.from_tortoise_orm(user)
    return user_obj

@app.post('/shild', tags=['Authoncation'])
async def get_shild(form_data : OAuth2PasswordRequestForm = Depends()):
    user = await authnicate_user(form_data.username, form_data.password)
    if user:
        user_obj = await User.login_pydantic.from_tortoise_orm(user)
        token = user_obj.json()
        return {'access_token': token, 'token_type' : 'bearer'}

    raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail = "User Not Found")

