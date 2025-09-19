# from langchain_core.prompts import  ChatPromptTemplate
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
#     base_url="https://poloai.top/v1"
# )
#
# chat_prompt_template = ChatPromptTemplate(
#     messages=[
#         ("system","你是一个AI助手,你的名字是{name}"),
#         ("human","我的问题是{question}")
#     ],
#     input_variables=["name","question"]
# )
#
# response = chat_prompt_template.invoke(input={"name":" 晓智","question":"1 + 2 * 3 = ?"})
# message = llm.invoke(response)
# print(message.content)

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

chat_prompt_template = ChatPromptTemplate(
    messages=[
        ("system","你是一个AI助手, 你的名字是{name}"),
        ("human","我的问题是{question}")
    ],
    input_variables=["name","question"]
)

prompt = chat_prompt_template.invoke(input={"name":" 晓智","question":"1 + 2 * 3 = ?"})
message = llm.invoke(prompt)
print(message.content)






