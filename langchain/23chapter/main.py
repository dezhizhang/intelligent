# from langchain.prompts import PromptTemplate
#
# template = PromptTemplate(
#     template="请评价{product}的优点,包括{aspect1}和{aspect2}",
#     input_variables=["product","aspect1","aspect2"]
# )
#
# # partial() 调用完以后，不会对调用者这个模板产生影响，而其返回的是一个新的模板
# temp = template.partial(product="手机",aspect1="屏幕",aspect2="拍照")
#
# prompt = temp.format(product="手机")
#
# print(prompt)

from langchain.prompts import PromptTemplate

template = PromptTemplate(
    template="请评价{product}的优点，包括{aspect1}和{aspect2}",
    input_variables=["product","aspect1","aspect2"]
)

temp = template.partial(product="手机",aspect1="屏幕",aspect2="拍照")
prompt = temp.format(product="手机")
print(prompt)



