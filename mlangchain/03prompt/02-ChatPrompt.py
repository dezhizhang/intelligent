from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import  ChatOpenAI
prompt_template = ChatPromptTemplate([
    ("system", "你是一个乐于肋人的助手"),
    ("user", "给我讲一个关于{topic}的笑话")
])

prompt = prompt_template.invoke({"topic":"python"})

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)


response = llm.invoke(prompt)
print(response)


