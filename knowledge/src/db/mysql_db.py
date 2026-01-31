import os
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine
from sqlalchemy.orm.session import sessionmaker


def get_db_url() -> str:
    """获取数据连接url"""
    return os.environ["MYSQL_DATABASE_URL"]

engine = create_async_engine(
    get_db_url(),
    pool_size=10,
    pool_recycle=3600,
    max_overflow=2,
    pool_pre_ping=True,
)

async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
