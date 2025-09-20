from langchain_ollama import ChatOllama

# 配置模型和本地 Ollama 服务地址
llm = ChatOllama(
    model="deepseek-r1:7b",
    base_url="http://127.0.0.1:11434",  # Ollama 默认端口
    timeout=60,  # 超时设置
    streaming = False  # 关闭流式
)

# 调用模型
response = llm.invoke("你好")
print(response)