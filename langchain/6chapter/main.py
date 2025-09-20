# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
#     base_url="https://poloai.top/v1"
# )
#
# question = "langchain是什么"
# response = llm.invoke(question)
#
# print(response.content)
#


from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

question = "langchain是什么"
response = llm.invoke(question)
print(response.content)