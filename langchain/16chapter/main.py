from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

messages = [
    SystemMessage(content="你是一个英语学习方向的专家"),
    HumanMessage(content="帮我制定一个英语六级学习的计划")
]

responses = llm.invoke(messages)
print(responses.content)




