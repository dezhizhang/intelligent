from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:7b"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个数学高手"),
        ("human", "帮我解决如下的数学问题:{question}")
    ]
)

chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

response = chain.invoke(input={"question": "1 + 2 * 3 = ?"})
print(response)