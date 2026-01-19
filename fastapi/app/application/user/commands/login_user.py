"""用户登录"""

from dataclasses import dataclass

from app.domain.user.repository import UserRepository
from app.application.common.exception import AuthError

@dataclass

class LoginUserCommand:
    """用户登录命令"""
    username:str
    password:str

@dataclass
class LoginUserResult:
    """用户登录结果"""
    user_id:int
    username:str

class LoginUserHandler:
    """用户登录命令处理器"""
    def __init__(self, user_repository:UserRepository):
        self.user_repository = user_repository


    async def handle(self, command:LoginUserCommand) -> LoginUserResult:
        """处理用户登录命令"""
        # 验证输入
        if not command.username or not command.username.strip():
            raise ValueError("用户名不能为空")
        # 验证密码
        if not command.password or not command.password.strip():
            raise ValueError("密码不能为空")


        user = await self.user_repository.find_by_username(command.username)
        if not user:
            raise AuthError("用户名或密码错误")

        if await self.user_repository.verify_password(command.password,user.password):
            raise AuthError("用户名或密码错误")

        return LoginUserResult(
            user_id=user.id if user.id else 0,
            username=user.username,
        )


