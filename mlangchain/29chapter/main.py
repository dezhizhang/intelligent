#
#
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# import os
# import dotenv
#
# dotenv.load_dotenv()
#
# llm = ChatOpenAI(
#     model=os.getenv("OPENAI_BASE_MODEL"),
#     base_url=os.getenv("OPENAI_BASE_URL"),
#     api_key=os.getenv("OPENAI_API_KEY"),
# )
#
# # 创建提示词
# template = ChatPromptTemplate.from_messages([
#     ("system","你是一个AI助手你的名字叫{name}"),
#     ("human","我的问题是{question}")
# ])
#
#
# prompt = template.invoke({"name":"晓智","question":"1 + 2 * 3=?"})
#
# response = llm.invoke(prompt)
# print(response)
#
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os
import dotenv

dotenv.load_dotenv()

print(os.getenv("OPENAI_BASE_URL"))

llm = ChatOpenAI(
    model=os.getenv("OPENAI_BASE_MODEL"),
    api_key=os.getenv("OPENAI_BASE_URL"),
    base_url=os.getenv("OPENAI_API_KEY")
)

template = ChatPromptTemplate.from_messages([
    ("system","你是一个AI助手,你的名字叫{name}"),
    MessagesPlaceholder(variable_name="msgs")
])

prompt = template.invoke({
    "name":"晓智",
    "msgs":[HumanMessage(content="我的问题是1 + 2 * 3 = ?")]
})

print(prompt)


response = llm.invoke(prompt)
print(response)




