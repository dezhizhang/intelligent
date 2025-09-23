from langchain_community.tools import MoveFileTool
from langchain_core.messages import HumanMessage
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai import  ChatOpenAI


# from langchain_openai from ChatOpenAI

# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     base_url="https://poloai.top/v1"
#
# )

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)


tools = [MoveFileTool()]


functions = [convert_to_openai_function(t) for t in tools]

messages = [HumanMessage(content="将文件a移动到桌面")]

response = llm.invoke(
    input=messages,
    functions = functions
)


print(response)



