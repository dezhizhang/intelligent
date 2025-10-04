
from langchain_core.messages import HumanMessage
from langchain_openai import  ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1",
    streaming=True
)

message = [
    HumanMessage(content="你好，请介绍一下自已")
]

for chunk in llm.stream(message):
    print(chunk.content,end="",flush=True)

print("\nend")




