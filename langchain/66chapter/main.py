

from langchain.prompts import  PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate

examples = [
    {"input": "2 + 2", "output": "4", "description": "加法运算"},
    {"input": "5 - 2", "output": "3", "description": "减法运算"}
]

prompt_template = "你是一个数学专家，算式: {input} 值,使用:{description}"

prompt_sample = PromptTemplate.from_template(prompt_template)

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=prompt_sample,
    suffix="你是一个数学专家,算式:{input} 值:{output}",
    input_variables=["input", "output"]
)

message = prompt.format(input="2 * 5",output="10")
print(message)









