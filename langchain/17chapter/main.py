# from langchain_openai import ChatOpenAI
# from langchain_core.messages import SystemMessage,HumanMessage
#
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
#     base_url="https://poloai.top/v1"
# )
#
#
# messages = [
#     SystemMessage(content="我是一个人工智能的助手,我的名字叫晓智"),
#     HumanMessage(content="猫王是一只狗吗")
# ]
#
# resp =llm.invoke(messages)
# print(resp.content)
#
# resp1 = llm.invoke("你叫什么名字")
# print(resp1.content)

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

messages = [
    SystemMessage("我是一个人工智能助手，名字叫晓智"),
    HumanMessage("猫王是一只狗吗"),
    HumanMessage("你叫什么名字")
]

resp = llm.invoke(messages)

print(resp.content)
