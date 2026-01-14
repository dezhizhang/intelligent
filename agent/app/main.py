from code.config import get_settings
from fastapi import FastAPI


# 加载配置信息
settings = get_settings()
print(settings)

app = FastAPI()




