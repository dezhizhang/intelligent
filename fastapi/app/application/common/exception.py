"""通用业务异常"""


from typing import Optional

class DomainException(Exception):
    """业务异常"""
    def __init__(self, message:str,code:Optional[str]=None):
        self.message = message
        self.code = code
        super().__init__(message)

class AuthError(Exception):
    """认证异常"""
    def __init__(self, message:str):
        super().__init__(message,"AuthError")

class DuplicateUserError(Exception):
    """重复数据异常"""
    def __init__(self, message:str):
        super().__init__(message,"DuplicateUserError")

class NotFoundUserError(Exception):
    """未找到数据"""
    def __init__(self, message:str):
        super().__init__(message,"NotFoundUserError")