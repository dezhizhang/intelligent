from langchain_core.output_parsers import XMLOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)


actor_query = "周星驰的简短电影记录,使用中文回复"

parser = XMLOutputParser()

# 生成提示词模板
prompt_template = PromptTemplate.from_template(
    template="用户的问题:{query}\n便用的格式:{format_instructions}",
    partial_variables={"query": actor_query}
)

prompt = prompt_template.partial(format_instructions=parser.get_format_instructions())


response = llm.invoke(prompt.invoke(input={"query":actor_query}))

xml_result = parser.invoke(response)


print(xml_result)

