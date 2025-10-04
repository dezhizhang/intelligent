# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     base_url="https://poloai.top/v1"
# )
#
# response = llm.invoke("帮我解释一下什么是大模型langchain")
# print(response.content)
# print(type(response))

# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     base_url="https://poloai.top/v1",
# )
#
# response = llm.invoke("帮我解释一下什么是大模型langchain")
# print(response.content)
# print(type(response))


from langchain_openai import  ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

response = llm.invoke("帮我解释一下什么是大模型langchain")
print(response.content)
print(type(response))





