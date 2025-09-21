from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import  PromptTemplate


llm  = ChatOpenAI(
    model="gpt-3.5-turbo-0613",
    temperature=0.9,
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

parser = JsonOutputParser()
prompt_template = PromptTemplate.from_template(
    template="回答用户的查询\n 满足的格式为{form_instructions}\n 问题为{question}",
    partial_variables={"form_instructions": parser.get_format_instructions()}
)


joke_query = "告诉我一个笑话"

chain = prompt_template | llm | parser
json_result = chain.invoke(input={"question":joke_query})
print(json_result)

