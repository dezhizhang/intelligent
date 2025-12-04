from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI

prompt_template = ChatPromptTemplate(
    [
        ("system", "你是一个乐于助人的助手，在回答用户问题时，需要带上用户的名字"),
        ("user", "我是{name}"),
        MessagesPlaceholder("msgs")
    ]
)

prompt = prompt_template.invoke(
    {"msgs": [AIMessage(content="你好，有什么需要咨询的 ?"), HumanMessage(content="三国志的作者是谁？")], "name": "张三"})

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

response = llm.invoke(prompt)
print(response)

