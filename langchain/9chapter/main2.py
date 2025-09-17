
from langchain_core.prompts import  ChatPromptTemplate
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system","你是世界级的技术文档编写者"),
        ("user","{input}")
    ]
)

chain = prompt | llm
message = chain.invoke({"input":"大模型中langchain是什么"})
print(message)