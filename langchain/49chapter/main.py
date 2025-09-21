from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)
#1. ChatMessageHistory的实例化
history = ChatMessageHistory()


# 添加消息进行存储
history.add_user_message("你好")

history.add_ai_message("很高兴认识你")
history.add_user_message("帮我计算1 + 2 * 3 = ?")

response = llm.invoke(history.messages)
print(response.content)



