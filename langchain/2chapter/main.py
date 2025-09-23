from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import  ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","你是世界级的技术文档编写者"),
        ("user","{input}")
    ]
)

# 使用输出解析器
parser = JsonOutputParser()

# 生成链
chain = prompt | llm | parser

response = chain.invoke({"input":"langchain是什么，问题question 回签用answer 用json格式回复"})
print(response)


