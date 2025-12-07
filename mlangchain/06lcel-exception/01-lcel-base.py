from langchain_core.prompts import  ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

prompt_template = ChatPromptTemplate.from_template("给我讲一个{topic}的笑话")

chain = prompt_template | llm
response = chain.invoke({"topic":"老王"})
print(response)

