import os
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from langchain_community.llms.tongyi import Tongyi
from dotenv import load_dotenv
load_dotenv(verbose=True)

example_template = PromptTemplate.from_template("单词:{world} 反义词:{antonym}")

examples_data = [
    {"world":"大","antonym":"小"},
    {"world":"上","antonym":"下"},
]

few_shot_template = FewShotPromptTemplate(
    example_prompt=example_template,
    examples=examples_data,
    prefix="告知我单词的反义词，我提供如下的示例:",
    suffix="基于前面的示例告知我，{input_word}的反义词是?:",
    input_variables=['input_word'],
)


llm = Tongyi(
    model="qwen-max",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL")
)

prompt = few_shot_template.invoke(input={"input_word":"左"})
resp = llm.invoke(input=prompt)
print(resp)




