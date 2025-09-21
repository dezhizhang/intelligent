

from langchain.chains.sequential import SimpleSequentialChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

chain_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一位精通各领域知识的知名教授"),
        ("human","请你尽可能详细解释一下:{knowledge}")
    ]
)

chain = LLMChain(llm = llm,prompt = chain_template,verbose = True)
full_chain = SimpleSequentialChain(
    chains=[chain],
    verbose=True
)

response = full_chain.invoke(input={"input":"什么是langchain"})
print(response)


