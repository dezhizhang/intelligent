from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

messages1 = [
    SystemMessage(content="你是一位乐于助人的智能小助手"),
    HumanMessage(content="请帮我介绍一下什么是机器学习")
]

messages2 = [
    SystemMessage(content="你是一位乐于助人的智能小助手"),
    HumanMessage(content="请帮我介绍一下什么是AIGC")
]

messages = [messages1,messages2]

resp = llm.batch(messages)

print(resp)