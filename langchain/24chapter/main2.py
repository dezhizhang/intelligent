# from langchain.prompts import PromptTemplate
#
# template = PromptTemplate.from_template(
#     template = "请评价 {product} 的优点,包括{aspect1}和{aspect2}"
# )
#
# prompt = template.invoke(input={"product":"智能手机","aspect1":"屏幕","aspect2":"拍照"})
#
# print(prompt)


from langchain.prompts import PromptTemplate
from langchain_openai import  ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

template = PromptTemplate.from_template(
    template="请评价 {product} 的优点，包括{aspect1}和{aspect2}"
)

prompt = template.invoke(input={"product": "苹果手机", "aspect1": "屏幕", "aspect2": "拍照"})

response = llm.invoke(prompt)
print(response.content)

