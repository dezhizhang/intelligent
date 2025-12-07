
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

messages = [
    SystemMessage("你是知识渊博的专家知道很多著名书籍相关知识请简洁的用20个字回答问题"),
    HumanMessage(content="请用一句话解释量子力学")
]

resp = llm.invoke(messages)
print(resp)
