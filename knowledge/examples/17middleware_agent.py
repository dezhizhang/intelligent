from langchain.agents import create_agent,AgentState
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool
from langchain.agents.middleware import before_agent,wrap_model_call
from langgraph.runtime import Runtime
from dotenv import load_dotenv
import os
load_dotenv()


@tool(description="查询天气")
def get_weather() -> str:
    return "睛天"

@before_agent
def log_before_agent(state:AgentState,runtime:Runtime) -> None:
    print(f"[before agent] 启动, 并附带{len(state['messages'])}消息")


@wrap_model_call
def model_call_hook(request,handler):
    print("模型调用啦")
    return handler(request)

agent = create_agent(
    model=ChatTongyi(
        model="qwen3-max",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url=os.getenv("DASHSCOPE_BASE_URL")
    ),
    tools=[get_weather],
    middleware=[log_before_agent,model_call_hook],
    system_prompt="""你是严格遵循ReAct框架的智能体,必须按「思考 行动→观察一再思考」的流程解决问题,
    且**每轮仅能思考并调用1个工具**,禁止单次调用多个工具。
    并告知我你的思考过程,工具的调用原因,按思考、行动、观察三个结构告知我"""
)

res = agent.invoke({"message":[{"role":"user","content":"今天天气如何呀"}]})
print("******",res)



