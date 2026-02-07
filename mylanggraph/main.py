from typing import Annotated

from math import trunc
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI

class State(TypedDict):
    message:Annotated[list,add_messages]


@tool
def search(query:str):
    """call to surf the web."""
    return ["The answer to your question lies within."]


tools = [search]

tool_node = ToolNode(tools)

llm = ChatOpenAI(
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1",
    temperature=0,
    streaming=True,
)

bound_model = llm.bind_tools(tools)




