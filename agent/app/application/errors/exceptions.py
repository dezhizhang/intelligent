from typing import Any


class AppException(RuntimeError):
    """"基础应用异常类"""

    def __init__(
            self,
            code: int,
            status_code: int,
            msg: str,
            data: Any = None
    ):
        """构造函数，完成错误数据初始化"""
        self.code = code
        self.status_code = status_code
        self.msg = msg
        self.data = data
        super().__init__()


class BadRequestError(AppException):
    """客户端请求错误"""

    def __init__(self, msg: str = "客户端请求错误，请检查后重试"):
        super().__init__(status_code=400, code=400, msg=msg)


class NotFoundError(AppException):
    """资源未找到错误"""

    def __init__(self, msg: str = "资源未找到，请核实后重试"):
        super().__init__(status_code=400, code=404, msg=msg)


class ValidationError(AppException):
    """数据校验错误"""

    def __init__(self, msg: str = "请求参数校验错误，请核实后重试"):
        super().__init__(status_code=422, code=422, msg=msg)


class TooManyRequestsError(AppException):
    """请求过多触发限流"""

    def __init__(self, msg: str = "请求过多，鉵发限流"):
        super().__init__(status_code=429, code=429, msg=msg)
