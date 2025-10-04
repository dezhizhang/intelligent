from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
    template="你是一个{role} 你的名字叫{name}",
    input_variables=["role","name"]
)


prompt = prompt_template.format(role="人工智能",name="数擎科技")
print(prompt)





