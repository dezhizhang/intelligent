# from langchain_core.messages import SystemMessage,HumanMessage
# from langchain_openai import ChatOpenAI
# import os
# import  dotenv
#
# dotenv.load_dotenv()
#
#
#
# messages = [
#     SystemMessage(content="我是一个人工智能助手，我的名字叫晓智"),
#     HumanMessage(content="猫王是一只猫吗?")
# ]
#
# llm = ChatOpenAI(
#     model=os.getenv("OPENAI_BASE_MODEL"),
#     api_key=os.getenv("OPENAI_BASE_URL"),
#     base_url=os.getenv("OPENAI_API_KEY")
# )
#
# response = llm.invoke(messages)
# print(response.content)

# from langchain_core.messages import SystemMessage,HumanMessage
# from langchain_openai import ChatOpenAI
# import os
# import dotenv
# dotenv.load_dotenv()
#
# llm = ChatOpenAI(
#     model=os.getenv("OPENAI_BASE_MODEL"),
#     api_key=os.getenv("OPENAI_BASE_URL"),
#     base_url=os.getenv("OPENAI_API_KEY")
# )
#
#
# message = [
#     SystemMessage(content="我是一个人工智能助手，我的名字叫晓智"),
#     HumanMessage(content="猫王是一只猫吗?")
# ]
#
# response = llm.invoke(message)
# print(response.content)





