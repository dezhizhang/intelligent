from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.chat import  MessagesPlaceholder

chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system","你是一个Ai助手，你的名字叫{name}"),
    MessagesPlaceholder(variable_name="msgs")
])


prompt = chat_prompt_template.invoke({
    "name":"数擎科技",
    "msgs":[HumanMessage(content="我的问题是 1 + 2 * 3 = ?")]
})

print(prompt)




