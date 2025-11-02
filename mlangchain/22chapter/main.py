
#
# from langchain_core.prompts import PromptTemplate
#
# text = """
#     Tell me a joke
# """



from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(template="你是一个{role} 你的名字叫{name}")

prompt = prompt_template.format(role="人工智能专家",name="晓智")
print(prompt)




