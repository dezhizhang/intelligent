# from langchain_core.tools import tool
#
# @tool("web_search", description="互联网搜索工具，可以搜索所有公开信息", parse_docstring=False)
# def web_search(query: str) -> str:
#     return "search result"

from langchain_core.tools import tool


@tool("web_search", description="互联网搜索工具，可以搜索所有公开信息", parse_docstring=False)
def web_search(query: str) -> str:
    try:
        pass
    except Exception as e:
        print(e)
        return f"error: {e}"
    return "search result"
