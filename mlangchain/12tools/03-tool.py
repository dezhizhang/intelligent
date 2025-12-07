from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field
from typing import Optional


class BankAccountQuery(BaseModel):
    account_id:str = Field(description="用户的银行帐号")

    pass



def query_bank_account(account_id:str,start_date:str,end_date:str,query_type) -> str:
    """查询银行帐户信息"""
    if query_type == "balance":
        return f"帐户{account_id}当前余额为￥1000"
    elif query_type == "account":
      return 'hello world'


StructuredTool.from_function(
    func=query_bank_account,
    name="query_bank_account",
    description="查询银行帐户信息",
    args_schema=BankAccountQuery
)