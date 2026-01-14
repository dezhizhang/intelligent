import logging

from code.config import get_settings
from fastapi import FastAPI
# from app.infrastructure.logging import setup_logging
#
from contextlib import asynccontextmanager


# 1. 加载配置信息
settings = get_settings()
print(settings)

# 2.初始化日志系统
# setup_logging()
# logger = logging.getLogger()
# logger.info("测试")


# 3. 定义fastapi路由tag标签
openai_tags = [
    {
        "name":"状态模块",
        "description":"包含 **状态监控** 等API 接口，用于监测系统的运行状态。",
    }
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    """创建fastapi应用程序生命周斯上下文管理"""
    logging.info("正在初始化")

    try:
        yield
    finally:
        pass
app = FastAPI(
    title="通用智能体",
    lifespan=None,
    description="agent系统，可以私有化部署",
    openapi_tags=openai_tags,
    version="0.1.0",
)




