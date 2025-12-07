from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

examples = [
    {"input": "北京天气怎么样", "output": "北京市"},
    {"input": "南京属于江苏省", "output": "南京市"},
    {"input": "武汉有什么好玩的地方", "output": "武汉市"}
]

example_prompt = PromptTemplate(
    input_variables=["input","output"],
    template="输入:{input}\n输出:{output}",

)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="input:{input}\n output",
    input_variables=["input"]
)

prompt = few_shot_prompt.format(input="烟花三月下场州")

print(prompt)
response = llm.invoke(prompt)
print(response.content)


