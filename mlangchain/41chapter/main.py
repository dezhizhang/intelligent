from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:7b"
)


prompt = PromptTemplate.from_template(
    template="你是一位数学高手,帮我解决如下的数学问题：{question}"
)

chain = LLMChain(llm=llm,prompt=prompt)

response = chain.invoke("1 + 2 * 3 = ？")
print(response)




