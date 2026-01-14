from code.config import get_settings
from fastapi import FastAPI
# from app.infrastructure.logging import setup_logging
#


# 1. 加载配置信息
settings = get_settings()
print(settings)

# 2.初始化日志系统
# setup_logging()
# logger = logging.getLogger()
# logger.info("测试")
app = FastAPI()




