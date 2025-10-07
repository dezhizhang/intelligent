from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

def chat_with_model(answer):
    prompt_template = ChatPromptTemplate.from_messages([
        ("system","你是一个人工智能的助手"),
        ("human","{question}")
    ])

    while True:
        # 获取chain并调用大模型
        chain = prompt_template | llm

        response = chain.invoke({"question":answer})

        # 输出大模型响应
        print(f"模型回复:{response.content}")

        # 继续获取用户的问题
        user_input = input("你还有其它的问题？")
        if(user_input == "退出"):
            break

        # 将上述新生成的消息存放到提示词模板的消息列表
        prompt_template.messages.append(AIMessage(content=response.content))
        prompt_template.messages.append(HumanMessage(content=user_input))

chat_with_model("你好，很高兴认识你")


