import logging

from fastapi import APIRouter

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/app-config", tags=["设置模块"])

@router.get(
    path="/llm",
    response_model=None,
    summary="获取LLM配置信息",
    description="包含LLM提供商的base_url,temperature,model_name,max_tokens",
)

async def get_llm_config():
    """获取LLM配置信息"""
    pass

@router.post(
    path="/llm",
    response_model=None,
    summary="更新LLM配置信息",
    description="更新LLM配置信息,当api_key为空的时候表示不更新该字段",
)

async def update_llm_config():
    """更新LLM配置信息"""
    pass




