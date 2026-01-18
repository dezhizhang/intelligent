import uvicorn
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

from typing import Dict
from urllib.parse import  quote_plus
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

password =  quote_plus("V4Nn9fa#Xf!")

v1 = APIRouter(prefix="/api/v1")
user = APIRouter(tags=['user'], prefix='/user')


class UserSchema(BaseModel):
    name: str
    email: str
    age: int

from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64)
    email = fields.CharField(max_length=64)
    created_at = fields.DatetimeField(auto_now_add=True)





@user.post("/create")
async def create_user(user: UserSchema):
    await User.create(**user.model_dump())


@user.get("/info")
async def get_user():
    user = await User.first()
    user_schema = UserSchema.model_validate(user.__dict__)
    return user_schema


TORTOISE_ORM:Dict = {
    "connections":{
        "default":f"mysql://root:{password}@localhost:3306/ihome"
    },
    "apps":{
        "models":{
            "models":["main"],
            "default_connection": "default"
        }
    },
    "use_tz": False,
    "timezone": "UTC",  # 默认时区
    "db_pool": {
        "max_size": 10,  # 最大连接数
        "min_size": 1,
        "idle_timeout": 30  # 空闲连接超时(秒)
    }
}

register_tortoise(app,config=TORTOISE_ORM,generate_schemas=True,add_exception_handlers=True)


v1.include_router(user)
app.include_router(v1)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
