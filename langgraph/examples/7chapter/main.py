
from  langchain_openai import  ChatOpenAI

llm = ChatOpenAI(
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1",
    temperature=1,
    max_tokens=10,
    max_retries=10
)

for chunk in llm.stream("你好"):
    print(chunk)


