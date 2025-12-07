from langchain_core.messages import AIMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_ollama import  ChatOllama
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

llm = ChatOllama(
    model="deepseek-r1:7b",
    base_url="http://localhost:11434"
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个助手,擅长能力{ability}。用20个字以内回答"),
        MessagesPlaceholder(variable_name='chat_history'),
        ("human","{input}")
    ]
)

store = {}

def get_session_history(session_id:str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


chain = prompt_template | llm
chain_width_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

r1 = chain_width_history.invoke(
    {"ability":"数学","input":"请问什么是余弦定理?"},
    config={"configurable":{"session_id":"a1"}}
)

print(r1)

print("*" * 20)

r2 = chain_width_history.invoke(
    {"ability":"数学","input":"我刚刚问了些什么?"},
    config={"configurable":{"session_id":"a1"}}
)
print(r2)






