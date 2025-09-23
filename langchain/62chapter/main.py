from langchain_core.tools import StructuredTool

# 声明一个函数
def search_google(query:str):
    return "最后查询结果"


# 定义一个工具
search = StructuredTool.from_function(
    func=search_google,
    name="Search",
    description="查询google搜索引擎并将结果返回"
)

print(f"name={search.name}")
print(f"args={search.args}")
print(f"description={search.description}")

search.invoke({"query":"中美ai的发展现状"})
