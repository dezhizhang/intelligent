from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import  StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


llm = ChatOpenAI(
    temperature=0.8,
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

prompt = ChatPromptTemplate.from_template("讲一个关于{topic}的笑话，不要有任何解释")

chain = prompt | llm | StrOutputParser()
response = chain.invoke({"topic":"狗"})
print(response)

