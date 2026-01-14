from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    """配置信息，从.env或者环境变量中加载数据"""

    env: str = "development"
    log_level: str = "INFO"

    # 数据库配置
    sqlalchemy_database_uri: str = "sqlite:///:memory:"

    # Redis缓存配置
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


@lru_cache()
def get_settings() -> Settings:
    """获取配置信息并对内容进行缓存，避免重复读取"""
    return Settings()
