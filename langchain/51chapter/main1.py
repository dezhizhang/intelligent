from langchain.chains.llm import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import  ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

# 创建prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个与人类对话的机器人"),
        MessagesPlaceholder(variable_name="history"),
        ("human","问题:{question}")
    ]
)

# 创建memory
memory = ConversationBufferMemory(return_messages=True)

# 创建llmChain
chain = LLMChain(prompt=prompt,llm=llm,memory=memory)

#调用

response = chain.invoke({"question":"中国的首都在啊里"})
print(response,end="\n\n")

