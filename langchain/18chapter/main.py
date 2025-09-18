from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1",
    streaming=True
)

message = [HumanMessage("你好，请介绍一下自已")]

for chunk in llm.stream(message):
    print(chunk.content,end="",flush=True)

