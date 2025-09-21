from langchain.chains.llm import LLMChain
from langchain_openai import  ChatOpenAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)


prompt_template = ChatPromptTemplate.from_messages([
    ("system","你是一个数学高手"),
    ("human","帮我解决如下的数学问题:{question}")
])

chain = LLMChain(llm = llm,prompt=prompt_template,verbose=True)

response = chain.invoke(input={"question":"1 + 2 * 3 = ?"})
print(response)

