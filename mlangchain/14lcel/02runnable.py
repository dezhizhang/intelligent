from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel



llm = ChatOpenAI(
    temperature=0.8,
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

joke_chain = ChatPromptTemplate.from_template("给我讲一个关于{topic}的笑话") | llm
poem_chain = ChatPromptTemplate.from_template("给我写一首关于{topic}的绝句") | llm

map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)

response = map_chain.invoke({"topic":"程序员"})
print(response)

