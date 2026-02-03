import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from core.config import get_settings
from app.infrastructure.logging import setup_logging
from app.interfaces.endpoints.routes import router
from fastapi.middleware.cors import CORSMiddleware
from app.interfaces.errors.exception_handlerss import register_exception_handlers

# 1.加载配置信息
settings = get_settings()

# 2.初始化日志系统
setup_logging()
logger = logging.getLogger()

logger.info("测试")


# 定义FastAPI路由tags标签
openapi_tags = [
    {
        "name":"状态模块",
        "description":"包含 **状态监测**等API接口,用于监测系统的运行状态。",
    }
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    """创建FastAPI应用程序生命周期上下文管理"""
    # 1. 打印日志表过程序开始了
    logger.info("正在初始化")

    try:
        #lifespan分界点
        yield
    finally:
        logger.info("正在关闭")
        pass

# 4. 创建路由实例
app = FastAPI(
    title="通用知能体",
    description="是一个通用的AIAgent系统,可以完全私有部署,使用A2A+MCP连接Agent/Tool,同时支持在沙",
    openapi_tags=openapi_tags,
    lifespan=lifespan,
    version="0.0.1",
)

# 5. 配置CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_origins=["*"],
    allow_credentials=True,
)

# 5. 集成路由
register_exception_handlers(app)

app.include_router(router,prefix="/api")





