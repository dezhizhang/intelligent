from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    """从.env或者环境变量中加载数据"""

    # 项目基础配置
    env:str = "development"
    log_level:str = "INFO"

    #数据库相关配置
    sqlalchemy_database_uri:str = "sqlite:///:memory:"

    # Redis缓存配置
    redis_host:str = "localhost"
    redis_port:int = 6379
    redis_db:int = 0
    redis_password:str | None= ""

    # 使用pydantic_settings设置配置文件
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
@lru_cache()
def get_settings() -> Settings:
    """获取当前项目配置信息并对内容进行缓存"""
    settings = Settings()
    return settings


