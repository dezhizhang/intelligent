from langchain_core.messages import AIMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:7b",
    base_url="http://localhost:11434"
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个乐于助人的助手，尽你所能回答所有问题，回答方式简结，20字左右"),
        MessagesPlaceholder(variable_name="messages"),
        ("user","{question}")
    ]
)

chain = prompt_template | llm
response = chain.invoke({
    "messages":[
        HumanMessage(content="你好,我叫老顾,请请问金庸是谁"),
        AIMessage(content="I love programming"),
    ],
    "question":"你好，你知道我叫什么名字"
})

print(response)

