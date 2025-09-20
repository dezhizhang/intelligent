from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.chat import MessagesPlaceholder

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个AI助手,你的名字叫{name}"),
        MessagesPlaceholder(variable_name="msgs")
    ]
)

prompt = template.invoke({
    "name":"晓智",
    "msgs":[HumanMessage(content="我的问题是:1 + 2 * 3 = ?")]
})

message = llm.invoke(prompt)

print(message.content)

