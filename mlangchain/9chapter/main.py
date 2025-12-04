# from  langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
#
# llm = ChatOpenAI(
#     model="gpt-4",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     base_url="https://poloai.top/v1"
# )
#
# prompt = ChatPromptTemplate.from_messages([
#     ("system","你是世界级的技术文档编写者"),
#     ("user","{input}")
# ])
#
# chain = prompt | llm
#
# message = chain.invoke({"input":"大模型中langchain是什么"})
# print(message)
# from  langchain_openai import ChatOpenAI
# from langchain_core.output_parsers import JsonOutputParser
#
# from  langchain_core.prompts import ChatPromptTemplate
#
# llm = ChatOpenAI(
#     model="gpt-4",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     base_url="https://poloai.top/v1"
# )
#
# prompt = ChatPromptTemplate.from_messages([
#     ("system","你是世界级的技术文档编写者"),
#     ("user","{input}")
# ])
#
# output_parser = JsonOutputParser()
#
# chain = prompt | llm | output_parser
# response = chain.invoke({"input":"langchain是什么? 用json格式回复"})
# print(response)







