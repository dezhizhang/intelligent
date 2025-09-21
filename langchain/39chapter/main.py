from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:7b",
)

response = llm.invoke("你好，请介绍一下你自已")


print(response)
