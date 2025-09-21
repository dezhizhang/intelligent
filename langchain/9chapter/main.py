from langchain_deepseek import ChatDeepSeek
llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key="sk-640be96306a64680985c02c88a4d685b",
    base_url="https://deepseek.com/v1"
)

response = llm.invoke("deepseek 是不是很拉圾")
print(response.content)





