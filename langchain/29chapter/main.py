

from langchain_openai import  ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 创建大模型
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

# 创建提示词
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个AI助手,你的名字叫{name}"),
        ("human","我的问题是{question}")
    ]
)

prompt = prompt_template.invoke({"name":"晓智","question":"1 + 2 * 3 = ?"})
response = llm.invoke(prompt)

print(response.content)



