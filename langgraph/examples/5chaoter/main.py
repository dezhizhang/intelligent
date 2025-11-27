from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1",
    model="gpt-4o-mini",
    temperature=0.5,
)

resp = llm.invoke("hello")
print(resp)