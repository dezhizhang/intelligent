
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("把大像放在冰箱需要三步，第一步:{first},第二步:{second},第三步:{third}")

first_prompt_template = prompt_template.partial(first="打开冰箱")
second_prompt_template = prompt_template.partial(second="把大像放进去")
third_prompt_template = prompt_template.partial(third="关闭冰箱")

print(third_prompt_template)

