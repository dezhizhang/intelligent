


# from langchain.prompts import PromptTemplate
#
# template = PromptTemplate.from_template(
#     template="请评价{product}的优点，包括{aspect1}",
#     partial_variables={"aspect1":"电池续航"}
# )
#
# prompt_1 = template.format(product="智能手机",aspect1="拍照质量")
# print(prompt_1)

from langchain.prompts import PromptTemplate

template = PromptTemplate.from_template(
    template="请评价{product}的优点,包括{aspect1}",
    partial_variables={"aspect1":"电池续航"}
)

prompt = template.format(product="智能手机",aspect1="拍照质量")
print(prompt)




