from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

# 创建template的实例
example_prompt = PromptTemplate.from_template(
    template="input:{input}\n output:{output}"
)

examples = [
    {"input": "北京天气怎么样", "output": "北京市"},
    {"input": "南京下雨吗", "output": "南京市"},
    {"input": "武汉热吗", "output": "武汉市"}
]

few_shot_template = FewShotPromptTemplate(
    example_prompt=example_prompt,
    suffix="input:{input}\noutput",
    examples=examples,
    input_variables=["input", "output"]
)

few_template = few_shot_template.invoke({"input":"天津会下雪吗?"})

resp = llm.invoke(few_template)
print(resp.content)
