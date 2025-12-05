from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

template = """
    你是一个助手，需要返回用户信息的JSON格式数据
    {format_instructions}
    请返回一个包含以下字段的JSON对像
    - name：用户性名
    - age: 用户年龄
    - hobbies: 用户爱好
    - favorite_color: 用户最喜欢的颜色
用户信息：{text}
"""

parser = JsonOutputParser()
prompt_template = PromptTemplate(
    template=template,
    input_variables=['text'],
    partial_variables={"format_instructions":parser.get_format_instructions()}
)

prompt = prompt_template.format_prompt(text="用户姓名张三，今年25岁，喜欢阅读，游泳和编程，最喜欢的颜色是蓝色")
response = llm.invoke(prompt)
output = parser.invoke(response)
print(output)







