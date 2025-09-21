from langchain_core.example_selectors import LengthBasedExampleSelector
from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate

examples = [
    {"input":"happy","output":"sad"},
    {"input":"tall","output":"short"},
    {"input":"sunny","output":"gloomy"},
    {"input":"高兴","output":"难过"}
]

examples_prompt = PromptTemplate(
    input_variables=["input","output"],
    template="原词: {input}\n反义: {output}"
)

# 构造示例选择器
example_selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=examples_prompt,
    max_length=25
)

dynamic_prompt = FewShotPromptTemplate(
    example_selector = example_selector,
    example_prompt=examples_prompt,
    prefix="给出每个输入词的反义词",
    suffix="原词:{adjective}\n反义",
    input_variables=["adjective"]
)


print(dynamic_prompt.format(adjective="big"))


