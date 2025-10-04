
#
# from langchain_core.prompts import PromptTemplate
#
# text = """
#     Tell me a joke
# """
#
#
# prompt_template = PromptTemplate.from_template(text)
#
# prompt = prompt_template.format()
#
# print(prompt)


from langchain_core.prompts import PromptTemplate

text = """
    Tell me a joke
"""

prompt_template = PromptTemplate.from_template(text)
prompt = prompt_template.format()

print(prompt)


