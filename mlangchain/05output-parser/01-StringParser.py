from langchain_openai import  ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

prompt = "请用一句话解释量子力学"

parser = StrOutputParser()
response = llm.invoke(prompt)
print(response)


