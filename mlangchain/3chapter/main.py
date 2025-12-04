# from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
# prompt_template = PromptTemplate.from_template("给我们讲一个{topic}笑话")
# prompt = prompt_template.invoke({"topic":"猫"})
#
#
# llm = ChatOpenAI(
#     model="gpt-4",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     base_url="https://poloai.top/v1"
# )
#
#
# response = llm.invoke(prompt)
# print(response.content)

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

prompt_template = PromptTemplate.from_template("给我们讲一个{topic}笑话")
prompt = prompt_template.invoke({"topic":"python"})

llm = ChatOpenAI(
     model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

response = llm.invoke(prompt)
print(response.content)
