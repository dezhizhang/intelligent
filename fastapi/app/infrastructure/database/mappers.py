"""实体与ORM映射器"""
from app.domain.shared.vo import UserId
from app.infrastructure.database.orm_models import UserORM
from app.domain.user.entity import User

class UserMapper:
    """"用户映射器"""
    @staticmethod
    def to_entity(orm_model:UserORM) -> User:
        """将orm转换成实体对像"""
        return User(
            id=UserId(orm_model.id) if orm_model.id else None,
            username=orm_model.username,
            password=orm_model.password,
        )

    @staticmethod
    def to_orm(user:User) -> UserORM:
        """将实体转换面orm对像"""
        orm_model = UserORM()
        if user.id:
            orm_model.id = user.id.value
        orm_model.username = user.username
        orm_model.password = user.password
        return orm_model


