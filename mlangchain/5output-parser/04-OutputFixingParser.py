from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser, OutputParserException
from langchain_core.output_parsers import OutputFixingParser
from langchain_openai import ChatOpenAI

# 你的 Pydantic 数据模型
class Movie(BaseModel):
    name: str = Field(description="电影名称")
    director: str = Field(description="导演姓名")
    year: int = Field(description="上映年份")

# 基础 Pydantic 解析器
pydantic_parser = PydanticOutputParser(pydantic_object=Movie)

# LLM（修复时会用它补全缺失字段）
llm = ChatOpenAI(model="gpt-4o-mini")

# 包装成可自动修复的 parser
fixing_parser = OutputFixingParser.from_llm(
    llm=llm,
    parser=pydantic_parser
)

# 错误/不完整 JSON
bad_output = '{"name":"卧虎藏龙","director":"李安"}'   # 缺 year

# 自动修复并解析
result = fixing_parser.parse(bad_output)

print(result)
print("修复后对象：", result)
print("year 字段类型：", type(result.year))
