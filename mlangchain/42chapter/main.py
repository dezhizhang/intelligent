from langchain.chains.sequential import SimpleSequentialChain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.llm import LLMChain
from langchain_ollama import  ChatOllama

llm = ChatOllama(
    model="deepseek-r1:7b"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","你是一位精通和领域知识的知名教授"),
        ("human","请你尽可能详细解释一下:{knowledge}")
    ]
)

chain = LLMChain(llm = llm,prompt=prompt,verbose = True)



simple_chain = SimpleSequentialChain(chains=[chain],verbose = True)

print(simple_chain)




