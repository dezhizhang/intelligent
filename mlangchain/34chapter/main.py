

# from langchain_core.output_parsers import StrOutputParser
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     base_url="https://poloai.top/v1"
# )
#
# response = llm.invoke("什么是大模型")
# parser = StrOutputParser()
#
# string = parser.invoke(response)
#
# print(string)

# from langchain_core.output_parsers import StrOutputParser
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     base_url="https://poloai.top/v1"
# )
#
# response = llm.invoke("什么是大模型")
# parser = StrOutputParser()
#
# message = parser.invoke(response)
# print(message)

# from langchain_core.output_parsers import StrOutputParser
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     base_url="https://poloai.top/v1"
# )
#
# response = llm.invoke("什么是大模型")
# parser = StrOutputParser()
# message = parser.invoke(response)
# print(message)

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import  StrOutputParser

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

response = llm.invoke("什么是大模型")
parser = StrOutputParser()
message = parser.invoke(response)
print(message)





