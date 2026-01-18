from typing import Dict
from urllib.parse import  quote_plus


password =  quote_plus("V4Nn9fa#Xf!")


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