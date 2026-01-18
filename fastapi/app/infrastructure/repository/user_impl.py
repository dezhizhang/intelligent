from typing import Optional

from app.domain.user.repository import UserRepository
from app.domain.user.entity import User
from app.domain.shared.vo import UserId
from app.infrastructure.database.mappers import UserMapper
from app.infrastructure.database.orm_models import UserORM


class UserRepositoryImpl(UserRepository):
    """基于ORM的用户仓储实现"""
    async def save(self, user: User) -> User:
        user_orm = UserMapper.to_orm(user)
        await user_orm.save()
        return UserMapper.to_entity(user_orm)


    async def find_by_id(self, user_id: UserId) -> User:
        """用通id查找用户"""
        orm_model = await UserORM.get_or_none(id=user_id.value)
        if orm_model:
            return UserMapper.to_entity(orm_model)
        return None

    async def find_by_username(self, username: str) -> User:
        """通过用户名查找用户"""
        orm_model = await UserORM.get_or_none(username=username)
        if orm_model:
            return UserMapper.to_entity(orm_model)
        return None

    async def exists_by_username(self, username: str) -> bool:
        """检查用户名是否存在"""
        return await UserORM.get_or_none(username=username) is not None

    async def delete(self,user_id: UserId) -> bool:
        """删除用户"""
        orm_model = await UserORM.get_or_none(id=user_id.value)
        if orm_model:
            await orm_model.delete()
            return True
        return False

    async def find_all(self) -> list[User]:
        """查找所有用户"""
        orm_models = await UserORM.all()
        return [UserMapper.to_entity(orm_model) for orm_model in orm_models]








