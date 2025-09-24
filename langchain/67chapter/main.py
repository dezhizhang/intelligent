# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="glm-4",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     base_url="https://poloai.top/v1"
# )
#
#
# response = llm.invoke("什么是大模型")
# print(response)

from langchain_openai import  ChatOpenAI

llm = ChatOpenAI(
    model="glm-4",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)


response = llm.invoke("什么是大模型")
print(response)


