from typing import Dict
from fastapi import FastAPI
from sqlalchemy.orm import defer
from  tortoise.contrib.fastapi import register_tortoise
from urllib.parse import quote_plus

app = FastAPI()

password = quote_plus("V4Nn9fa#Xf!")


#Tortoise-ORM配置
TORTOISE_ORM: Dict = {
    "connections":{
        "default":f"mysql://root:{password}@localhost:3306/ihome",
    },
    "apps": {
        "models":{
            "models": ["model"],
            "default_connection": "default"
        }
    },
    "use_tz":False,
    "timezone":"UTC", #默认时区
    "db_pool":{
        "max_size":10, # 最大连接数
        "min_size": 1,
        "idle_timeout": 30 #空闲连接超时(秒)
    }
}


register_tortoise(app=app,config=TORTOISE_ORM,generate_schemas=True,add_exception_handlers=True)

from service import create_student

@app.get("/create")
async def create():
   stu = await create_student("tom",22,"15992478448@163.com")
   return stu

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)