from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage,AIMessageChunk

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

def parse(ai_message:AIMessage) -> str:
    """Parse the AI message"""
    return ai_message.content.swapcase()

response = llm.invoke("hello")
print(parse(response))







