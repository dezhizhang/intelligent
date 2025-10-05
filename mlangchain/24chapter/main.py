

from langchain.prompts import  PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

template = PromptTemplate.from_template(
    template="请评价{product}的优点,包括{aspect1}"
)

prompt = template.invoke(input={"product":"智能手机","aspect1":"拍照质量"})

response = llm.invoke(prompt)
print(response)











