# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI  # 如果你用 OpenAI 模型
#
# prompt = ChatPromptTemplate.from_template("介绍一下 {topic}")
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     base_url="https://poloai.top/v1",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM"
# )
#
# chain = prompt | llm  # LCEL 写法
#
# result = chain.invoke({"topic": "人工智能"})
# print(result.content)

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4o-mini",
    base_url="https://poloai.top/v1",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM"
)

prompt = ChatPromptTemplate.from_template("介绍一下{topic}")

chain = prompt | llm
response = chain.invoke({"topic":"人工智能"})
print(response.content)


