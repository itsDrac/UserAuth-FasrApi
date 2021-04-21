from tortoise.models import Model
from tortoise.fields import IntField, CharField 
from tortoise.contrib.pydantic import pydantic_model_creator

from api.helper import classproperty

class User(Model):
    id = IntField(pk=True)
    name = CharField(max_length=10)
    password = CharField(max_length=20)

    @classproperty
    def pydantic(cls):
        return pydantic_model_creator(cls, 
            name='User', 
            exclude=['password']
            )

    @classproperty
    def login_pydantic(cls):
        return pydantic_model_creator(cls, 
            name='Login User'
            )


