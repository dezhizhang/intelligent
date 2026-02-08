import os
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker


def get_db_url() -> str:
    """
    你的环境变量必须是 async 驱动，例如：

    mysql+aiomysql://user:password@127.0.0.1:3306/dbname
    或
    mysql+asyncmy://user:password@127.0.0.1:3306/dbname
    """
    return os.environ["MYSQL_DATABASE_URL"]


# 创建异步引擎
engine = create_async_engine(
    get_db_url(),
    pool_size=10,
    max_overflow=20,
    pool_recycle=1800,
    pool_pre_ping=True,
    echo=False,  # 生产环境建议关闭 SQL 日志
)


# 创建 Session 工厂
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# FastAPI 依赖注入使用
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
