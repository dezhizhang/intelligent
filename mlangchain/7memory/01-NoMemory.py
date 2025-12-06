from langchain_core.messages import AIMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="deepseek-r1:7b",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个乐于助人的助手，尽你所能回答所有问题，回答方式简结，20字左右"),
        ("user","{question}")
    ]
)

chain = prompt_template | llm
response = chain.invoke({"question":"你好,我叫老顾,请请问金庸是谁"})
print(response.content)

response = chain.invoke({"question":"你好,你知道我叫什么名字"})
print(response.content)






