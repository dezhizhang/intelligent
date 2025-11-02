# from langchain_openai import ChatOpenAI
# from langchain_core.messages import SystemMessage,HumanMessage
#
# llm = ChatOpenAI(
#     model="gpt-4",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     base_url="https://poloai.top/v1"
# )
#
# messages = [
#     SystemMessage(content="我是人工智能助手,我的名字叫数擎Ai"),
#     HumanMessage(content="你好，我是晓智，很高兴认识你")
# ]
#
# response = llm.invoke(messages)
# print(response.content)

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage

llm = ChatOpenAI(
    model="gpt-4",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

messages = [
    SystemMessage(content="我是人工智能助手,我的名字叫数擎Ai"),
    HumanMessage(content="你好，我是晓智，很高兴认识你")
]

response = llm.invoke(messages)
print(response.content)



