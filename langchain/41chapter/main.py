# from langchain.chains.llm import LLMChain
# from langchain_core.prompts import PromptTemplate
# from langchain_openai import  ChatOpenAI
#
#
# llm = ChatOpenAI(

# )
#
# prompt = PromptTemplate.from_template(
#     template="你是一个数字高手,帮我解决如下数学问题:{question}"
# )
#
#
# chain = LLMChain(llm=llm,prompt = prompt)
# response = chain.invoke(input={"question":"1 + 2 * 3 = ?"})
# print(response)

from langchain_openai import  ChatOpenAI
from langchain_core.prompts import  PromptTemplate
from langchain.chains.llm import LLMChain


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

prompt = PromptTemplate.from_template(
    template="你是一个数字高手,帮我解决如下数学问题:{question}"
)

chain = LLMChain(llm = llm,prompt = prompt)
response = chain.invoke(input={"question":"1 + 2 * 3 = ?"})

print(response)




