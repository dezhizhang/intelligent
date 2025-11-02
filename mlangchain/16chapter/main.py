# 关于对话模型中消息的使用
# from langchain_openai import ChatOpenAI
# import os
# import dotenv
#
# dotenv.load_dotenv()
#
# llm = ChatOpenAI(
#     model=os.getenv("OPENAI_BASE_MODEL"),
#     base_url=os.getenv("OPENAI_BASE_URL"),
#     api_key=os.getenv("OPENAI_API_KEY")
# )
#
# response = llm.invoke("什么是大模型")
# print(response)
from pyexpat.errors import messages

# from langchain_openai import ChatOpenAI
# import os
# import dotenv
#
# dotenv.load_dotenv()
#
# llm = ChatOpenAI(
#     model=os.getenv("OPENAI_BASE_MODEL"),
#     base_url=os.getenv("OPENAI_BASE_URL"),
#     api_key=os.getenv("OPENAI_API_KEY")
# )
#
# response = llm.invoke("什么是langchain")
#
# print(response.content)

# from langchain_openai import ChatOpenAI
# import os
# import dotenv
#
# dotenv.load_dotenv()
#
# llm = ChatOpenAI(
#     model=os.getenv("OPENAI_BASE_MODEL"),
#     base_url=os.getenv("OPENAI_BASE_URL"),
#     api_key=os.getenv("OPENAI_API_KEY")
# )
#
# response = llm.invoke("什么是langchain")
# print(response.content)

# from langchain_openai import ChatOpenAI
# from langchain_core.messages import HumanMessage,SystemMessage
#
# messages = [
#     SystemMessage(content="你是人工智能专家"),
#     HumanMessage(content="帮我制定一个AI学习路线")
# ]
#
# print(messages)

from langchain_openai import ChatOpenAI
# from langchain_core.messages import HumanMessage,SystemMessage
#
# messages = [
#     SystemMessage(content="你是人工智能专家"),
#     HumanMessage(content="帮我制定一个AI学习路线s")
# ]
#
# print(messages)

# from langchain_openai import ChatOpenAI
# from langchain_core.messages import HumanMessage,SystemMessage
#
# messages = [
#     SystemMessage(content="你是人工智能专家"),
#     HumanMessage(content="帮我制定一个AI学习路线")
# ]
#
# print(messages)

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(
        content="你是一个英语教学方向的专家",
        addition_kwargs={"tool": "invoke_func1"}
    ),
    HumanMessage(content="帮我制定一个AI学习路线")
]

print(messages)
