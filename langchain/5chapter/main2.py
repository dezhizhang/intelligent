
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=['text'],
    template = '你是一位专业的程序员，对于信息{text} 进行简短描述'
)

print(prompt.format(text = "langchain"))

