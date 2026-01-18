from dataclasses import dataclass
from  ..shared.vo import UserId
from typing import Optional

@dataclass(frozen=True)
class User:
    """用户实体类"""
    id:Optional[UserId]
    username:str
    password:str
    def __post_init__(self):
        if not self.username:
            raise ValueError("用户名不能为空")
        if not self.password:
            raise ValueError("密码不能为空")


    def verify_password(self, password: str) -> bool:
        """验证密码是否正确"""
        return self.password == password
