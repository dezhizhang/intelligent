
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_openai import ChatOpenAI

history = ChatMessageHistory()
history.add_user_message("你好")
history.add_ai_message("很高兴认识你")
history.add_user_message("帮我计算 1 + 2 * 3 = ？")


llm = ChatOpenAI(
    model="gpt-4",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

response = llm.invoke(history.messages)

print(response.content)


