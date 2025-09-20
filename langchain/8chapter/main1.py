# from langchain_core.prompts import PromptTemplate
#
# prompt = PromptTemplate.from_template("请评价 {product} 的优点,包括{aspect1}和{aspect2}")
# template = prompt.format(product="手机",aspect1="屏幕",aspect2="拍照")
#
# print(template)
#

# from langchain_core.prompts import PromptTemplate
#
# template = PromptTemplate.from_template("请您评价{product} 的优点，包括{aspect1}和{aspect2}")
#
# prompt = template.format(product="手机",aspect1="屏幕",aspect2="拍照")
#
# print(prompt)

from langchain_core.prompts import  PromptTemplate
template = PromptTemplate.from_template("请评价{product}的优点,包括{aspect1}和{aspect2}")
prompt = template.format(product="手机",aspect1="屏幕",aspect2="拍照")

print(prompt)


