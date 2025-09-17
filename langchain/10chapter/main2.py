# from langchain_openai import ChatOpenAI
# from langchain_core.messages import SystemMessage,HumanMessage
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
#     base_url="https://poloai.top/v1"
# )
#
# message = [
#     SystemMessage(content="我是人工智能助手,我叫晓智"),
#     HumanMessage(content="你好，我是小明，很高兴认识你")
# ]
#
# response = llm.invoke(message)
#
# print(response.content)
#

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

message = [
    SystemMessage(content="我是人工智能助手,我叫晓智"),
    HumanMessage(content="你好，我是小明，很高兴认识你")
]

response = llm.invoke(message)

print(response.content)
