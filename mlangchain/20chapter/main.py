# from langchain_core.prompts import PromptTemplate
#
# # 创建提示词模板
# prompt_template = PromptTemplate(
#     template="你是一个{role}，你的名字{name}",
#     input_variables=["role","name"]
# )
#
# prompt = prompt_template.format(role="人工智能专家",name="晓智")
#
# print(prompt)

from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
    template="你是一个{role},你的名字叫{name}",
    input_variables=["role","name"]
)

prompt = prompt_template.format(role="人工智能专家",name="晓智")
print(prompt)


