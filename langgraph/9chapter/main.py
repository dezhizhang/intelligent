from langchain_core.output_parsers import SimpleJsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel,Field
from  langchain_openai import  ChatOpenAI



llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1",
    temperature=1,
    max_tokens=10,
    max_retries=10
)

class Movie(BaseModel):
    title:str = Field(...,description="电影标题")
    year:int = Field(...,description="电影发行年份")
    director:str = Field(...,description="电影导演")
    rating:float = Field(...,description="电影评份（满分10分）")


prompt = ChatPromptTemplate.from_template(
    "尽你所能回答用户的问题"
    '你必须绍终输入一个包含"title","year","director","rating" 键的JSON对像,其中"title"代表：电影标题,"year"代表：电影发行年份,"director"代表:电影导演,"rating"代表：电影评份"'
    "{question}"
)

chain = prompt | llm | SimpleJsonOutputParser()
resp = chain.invoke({"question":"提供电影 《盗梦空间》的详细信息"})
print(resp)
