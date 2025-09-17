
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)


# 指定输出模式
output_parser = StrOutputParser();

# 提示词
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","你是世界级的技术文档编写者"),
        ("user","请用JSON格式回答问题。: {input}")
    ]
)

chain = prompt | llm | output_parser

message = chain.invoke({"input":"langchain是什么"})
print(message)
