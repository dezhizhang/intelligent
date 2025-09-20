from pydantic import BaseModel, Field
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import HumanMessage

# 初始化 LLM
llm = ChatOpenAI(
    model_name="gpt-4",
    api_key="sk-7b5ca2da2eae420eb985dfd196e3895f",
    base_url="https://deepseek.com/v1"
)

# 工具示例
class Add(BaseModel):
    a: int = Field(..., description="The first integer")
    b: int = Field(..., description="The second integer")

class Multiply(BaseModel):
    a: int = Field(..., description="The first integer")
    b: int = Field(..., description="The second integer")

# 正确调用方式
query = "3加12是多少"
response = llm.invoke([HumanMessage(content=query)])  #
print(response)
