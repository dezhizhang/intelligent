"""
应用配置管理
"""

from pydantic_settings import BaseSettings
from pydantic import  ConfigDict


class Settings(BaseSettings):
    """应用配置类"""

    app_name: str = "fastapi"
    app_version: str = "0.0.1"
    debug: bool = True
    secret_key: str = "fastapi"

    # 数据库配置
    db_url: str = "sqlite:///./data/test.db"

    model_config = ConfigDict(
        env_file = ".env",
        env_file_encoding="utf-8",
    )


settings = Settings()

if __name__ == "__main__":
    print(settings.app_name)

