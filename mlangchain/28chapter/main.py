

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个AI助手,你的名字叫{name}"),
        ("human","我的问题是{question}")
    ]
)


prompt = template.invoke({"name":"贵州数擎科技有限公司","question":"1 + 2 * 3 = ?"})
response = llm.invoke(prompt)
print(response)





