# from langchain_core.messages import HumanMessage
# from langchain_ollama import ChatOllama
#
# llm = ChatOllama(
#     model="deepseek-r1:7b"
# )
#
#
#
# messages = [
#     HumanMessage(content="你好，请介绍一下你自已")
# ]
#
# response = llm.invoke(messages)
#
# print(response.content)

from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:7b"
)

messages = [
    HumanMessage(content="介绍一下你自已")
]

response = llm.invoke(messages)

print(response.content)



