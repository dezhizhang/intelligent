"""共享值对像(Value Object)定义模块"""

from dataclasses import dataclass


@dataclass(frozen=True)
class UserId:
    """用户id偱对像"""
    id: int

    def __post_init__(self):
        """初始化检查"""
        if self.id < 0:
            return ValueError("用户ID不能小于0")
