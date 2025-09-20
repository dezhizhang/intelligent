# from langchain_deepseek import ChatDeepSeek
#
# llm = ChatDeepSeek(
#     temperature=0,
#     model="deepseek-chat",
#     api_key="sk-7b5ca2da2eae420eb985dfd196e3895f",
#     base_url="https://deepseek.com/v1"
# )
#
# resp = llm.invoke("介绍下自已")
# print(resp.content)


from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
    temperature=0,
    model="deepseek-chat",
    api_key="sk-7b5ca2da2eae420eb985dfd196e3895f",
    base_url="https://deepseek.com/v1"
)

resp = llm.invoke("介绍下自已")
print(resp.content)
