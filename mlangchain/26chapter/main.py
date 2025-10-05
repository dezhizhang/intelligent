
from langchain_core.prompts import ChatPromptTemplate

chat_prompt_template = ChatPromptTemplate(
    [
        ("system","你是一个AI助手,你的名字叫{name}"),
        ("human","我的问题是{question}")
    ]
)

prompt = chat_prompt_template.format_messages(name="数擎科技",question="1 + 2 * 3 = ?")
print(prompt)






