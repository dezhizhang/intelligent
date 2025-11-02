

from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    template="请评价{product}的产品质量，包括{aspect1}和{aspect2}"
)

prompt = template.partial(aspect1="电池续般",aspect2="拍照质量").format(product="智能手机")
print(prompt)






