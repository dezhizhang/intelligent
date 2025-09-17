# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
#     base_url="https://poloai.top/v1"
# )
#
# response = llm.invoke("贵州数擎科技有限公司")
# print(response.content)
#

# from langchain_openai import ChatOpenAI
#
#
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
#     base_url="https://poloai.top/v1"
# )
#
# response = llm.invoke("贵州数擎科技有限公司")
# print(response.content)

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

response = llm.invoke("贵州数擎科技有限公司")
print(response.content)



