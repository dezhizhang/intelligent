from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key="sk-ad2baecfde824382bbd93423a405e0df",
    base_url="https://api.deepseek.com"
)

response = llm.invoke("介绍一下自已")
print(response.usage_metadata)

