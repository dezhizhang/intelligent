from langchain_core.output_parsers import XMLOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import  ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)


actor_query = "生成周星驰的简短电影记录"

parser = XMLOutputParser()

template = PromptTemplate.from_template(template="有户的问题{query}\n使用的格式：{format_instructions}")

prompt = template.partial(format_instructions=parser.get_format_instructions())


response = llm.invoke(prompt.invoke(input={"query":actor_query}))
print(response.content)





