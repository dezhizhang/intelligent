from langchain.chains.llm import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_openai import  ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"

)

prompt_template = PromptTemplate.from_template(
    template="""
        你可以与人类对话
        当前对话:{history}
        人类问题:{question}
        
        回复:
    """
)

# 提供memory实例
memory = ConversationBufferMemory()

# 提供chain
chain = LLMChain(llm = llm,prompt=prompt_template,memory=memory)

# 提供响应
response = chain.invoke({"question":"你好，我的名字叫小明"})
print(response)

