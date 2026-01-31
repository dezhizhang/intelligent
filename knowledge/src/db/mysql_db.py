import os
from typing import AsyncIterator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
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


async def get_db() -> AsyncIterator[AsyncSession, None]:
    try:
        db = await async_session()
        yield db
    except Exception as ex:
        print(f"数据库操作错误:{ex}")
        if db and db.in_transaction():
            await db.rollback()
    finally:
        if db:
            await db.close()
