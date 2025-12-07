from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:7b",
    base_url="http://localhost:11434"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个助手，用20个字以内回答"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human","{input}")
    ]
)

def get_session_history(session_id:str):
    return SQLChatMessageHistory(session_id=session_id,connection="sqlite:///history.db")


chain = prompt | llm
chain_width_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

config = {"configurable":{"session_id":"a1"}}

# r1 = chain_width_history.invoke({"input":"我是数擎，请问中国首都是哪个城市？"},config=config)

r1 = chain_width_history.invoke({"input":"你知道我的名字叫什么吗"},config=config)
print(r1)

