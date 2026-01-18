"""用户仓储接口"""

from abc import ABC, abstractmethod
from .entity import User
from ..shared.vo import UserId
from typing import Optional

class UserRepository(ABC):

    @abstractmethod
    async def add(self, user: User) -> User:
        """保存用户"""
        pass
    @abstractmethod
    async def find_by_id(self, id: UserId) -> User:
        """通过id查户用户"""
        pass
    @abstractmethod
    async def find_by_username(self, username: str) -> Optional[User]:
        """通过用户名查找用户"""
        pass
    @abstractmethod
    async def exists_by_username(self, username: str) -> bool:
        """检查用户名是否存在"""
        pass

    @abstractmethod
    async def delete(self,user_id: UserId) -> Optional[User]:
        """删除用户"""
        pass
    @abstractmethod
    async def find_all(self) -> None:
        """删除所有用户"""
        pass





