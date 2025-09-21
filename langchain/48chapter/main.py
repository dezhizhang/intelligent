from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

def chat_with_model(answer):
    prompt = ChatPromptTemplate.from_messages([
        ("system","你是一个人工智能助手"),
        ("human","{question}")
    ])

    while True:
        chain = prompt | llm
        response = chain.invoke({"question":answer})

        # 输出大模型响应
        print(f"模型回复:{response.content}")

        # 继续获取用户的问题
        user_input = input("你还有其它问题吗?")
        if (user_input == "退出"):
            break

        # 将上这新生成的消息添加到
        prompt.messages.append(AIMessage(content=response.content))
        prompt.messages.append(HumanMessage(content=user_input))

chat_with_model("你好，很高兴认识你")
