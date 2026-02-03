import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.interfaces.schemas import Response
from starlette.exceptions import HTTPException

logger = logging.getLogger(__name__)


def register_exception_handlers(app: FastAPI):
    """处理项目中所有的异常并统一处理，涵盖：自定义业务状态异常，HTTP异常，通用异常"""

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, e: HTTPException) -> JSONResponse:
        """处理FastAPI抛出的http异常，将所有状态统一响应为json格式"""
        logger.error(f"HTTPException: {e.detail}")
        return JSONResponse(
            status_code=e.status_code,
            content=Response(
                code=e.status_code,
                msg=e.detail,
                data={}
            )
        )


    @app.exception_handler(Exception)
    async def exception_handler(request: Request, e: Exception) -> JSONResponse:
        """处理项目中抛出的未定义的任意异常，将状态码统一设置为500"""
        logger.error(f"Exception:{str(e)}")

        return JSONResponse(
            status_code=500,
            content=Response(
                code=500,
                msg="服务器出现异常请稍后重试",
                data={}
            ).model_dump()
        )
