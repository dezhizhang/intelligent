from langchain.prompts import PromptTemplate

template = "你是一位专业的程序员，\n对于信息处{text} 进行简短描述"


prompt = PromptTemplate.from_template(template)

print(prompt.format(text="langchain"))






