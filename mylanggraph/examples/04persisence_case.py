from typing import Annotated

from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from typing import Literal
from langgraph.graph import StateGraph,START
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage

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

def should_continue(state:State) -> Literal["action","__end__"]:
    """Return true if we should continue."""
    last_message = state["messages"][-1]
    if not last_message.tool_calls:
        return "__end__"

    return "action"


# 定义一个函数调用模型
def call_model(state:State):
    response = llm.invoke(state["messages"])
    return {"messages":response}


# 定义一个图形工作流
workflow = StateGraph(State)

workflow.add_node("agent",call_model)
workflow.add_node("action",call_model)

workflow.add_edge(START,"agent")

workflow.add_conditional_edges(
    "agent",
    should_continue,
)

workflow.add_edge("action","agent")

# 创建一个MemorySaver实例
memory = MemorySaver()

app = workflow.compile(checkpointer=memory)

graph_png = app.get_graph().draw_mermaid_png()
with open("persistence_case.png","wb") as f:
    f.write(graph_png)


# 设置配置参数
config = {"configurable":{"thread_id":"7943811f-d52f-20ce-7f51-21d263f9f41d"}}

input_message = HumanMessage(content="hi! I'm bob")

for event in app.stream({"messages":[input_message]},config,stream_mode="values"):
    event["messages"][-1].pretty_print()

input_message = HumanMessage(content="what is my name?")

# for event in app.stream({"messages":[input_message]},config,stream_mode="values"):
#     event["messages"][-1].pretty_print()

