from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI(
	title='Fast-api User Auth',
	description= 'Learing how to `OAuth2` in FastAPI',
	version = '1.1.1'
)

register_tortoise(
	app,
	db_url='sqlite://../databse.db',
	modules={"models": ["api.models"]},
	generate_schemas=True,
    add_exception_handlers=True,
)

from api import routes 
