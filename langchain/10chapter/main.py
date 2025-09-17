# from langchain_openai import OpenAI
#
#
# api_key = "sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs"
# base_url = "https://poloai.top/v1"
#
#
# llm = OpenAI(
#     model="gpt-4o-mini",
#     api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
#     base_url="https://poloai.top/v1"
# )
#
# message = llm.invoke("写一首关于春天的诗")
# print(message)

# from langchain_openai import OpenAI
#
# api_key = "sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs"
# base_url = "https://poloai.top/v1"
#
# llm = OpenAI(
#     model="gpt-4o-mini",
#     api_key=api_key,
#     base_url=base_url
# )
#
# message = llm.invoke("写一首关于春天的诗")
# print(message)

from langchain_openai import OpenAI

llm = OpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

msg = llm.invoke("写一首关于春天的诗")
print(msg)



