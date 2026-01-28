from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

@tool(description="获取股价，传入股票名称，返回字符串信息")
def get_price(name:str) -> str:
    return f"股票{name}的价格是20元"

@tool(description="获取上市公司股票信息")
def get_info(name:str) -> str:
    return f"股票{name}，是一家A股上市公司，专注于IT职业教育"

agent = create_agent(
    model = ChatTongyi(
        model="qwen3-max",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url=os.getenv("DASHSCOPE_BASE_URL")
    ),
    tools=[get_price, get_info],
    system_prompt="你是一个智能肋手，可以回答股票相关问题，记住请告诉我思考过程"
)

for chunk in agent.stream(
    {"messages":[{"role":"user","content":"小米股价是多少，并介绍一下"}]},
    stream_mode="values"
):
    print(chunk['messages'][-1])






