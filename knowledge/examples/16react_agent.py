from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv
import os
load_dotenv(verbose=True)

@tool(description="获取体重，返回值是整数，单位是千克")
def get_weight() -> int:
    return 90

@tool(description="获取身高，返回是整数，单位是厘米")
def get_height() -> int:
    return 172


agent = create_agent(
    model=ChatTongyi(
        model="qwen3-max",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url=os.getenv("DASHSCOPE_BASE_URL")
    ),
    tools=[get_weight,get_height],
    system_prompt="""你是严格遵循ReAct框架的智能体,必须按「思考 行动→观察一再思考」的流程解决问题,
    且**每轮仅能思考并调用1个工具**,禁止单次调用多个工具。
    并告知我你的思考过程,工具的调用原因,按思考、行动、观察三个结构告知我"""
)

for chunk in agent.stream(
        {"message":[{"role":"user","content":"计算我的BMI"}]},
         stream_mode="values",
):
    print(chunk['messages'][-1])