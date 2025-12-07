from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_openai import  ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

messages = [
    SystemMessage(content="你是知识渊博的专家知道很多著名书籍相关知识请简洁的用20个字回答问题"),
    HumanMessage(content="我的身份是学员,名字叫小顾"),
    AIMessage(content="欢迎,有什么需要咨询的?"),
    HumanMessage(content="三国志作者的是谁?"),
    AIMessage(content="《三国志》的作者是三国时期的历史学家陈寿寿。"),
    HumanMessage(content="红楼梦呢?"),
]

resp = llm.invoke(messages)
print(resp)




