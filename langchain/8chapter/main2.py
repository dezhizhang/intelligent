from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个起名大师,你的名字叫{name}."),
        ("human","您好{name} 您感觉如何"),
        ("ai","你好！你状态非常好"),
        ("human","你叫什么名字"),
        ("ai","你好，我叫{name}"),
        ("human","user_input")
    ]
)


chats = chat_template.format_messages(name="陈大师",user_input="你的爸爸是谁？")


print(chats)

