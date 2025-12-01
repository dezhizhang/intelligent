from langchain.agents import create_agent
from  dotenv import  load_dotenv

load_dotenv()

def get_weather(city:str) -> str:
    """获取天气信息"""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="deepseek:deepseek-chat",
    tools=[get_weather]
)

result = agent.invoke({"messages":[{"role":"user","content":"What is ther weather in SF"}]})
messages = result['messages']

for message in messages:
    print(message)

