from langchain_core.output_parsers import JsonOutputParser, XMLOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

actor_query = "生成汤姆 汉克斯的简短电影记录，使用中文回复"

parser = XMLOutputParser()

prompt_template1 = ChatPromptTemplate.from_template(
    template="用户的问题:{query}\n使用的格式{format_instructions}"
)

prompt_template2 = prompt_template1.partial(format_instructions=parser.get_format_instructions())

response = llm.invoke(prompt_template2.invoke(input={"query":actor_query}))

print(parser.invoke(response))




