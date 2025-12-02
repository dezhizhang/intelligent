from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver  # 检查点管理器
from langchain_core.runnables import RunnableConfig
from typing import Annotated
from typing_extensions import TypedDict
from operator import add


# 创建状态图
class State(TypedDict):
    foo: str
    bar: Annotated[list[str], add]


def node_a(state: State):
    return {"foo": "a", "bar": ["a"]}


def node_b(state: State):
    return {"foo": "b", "bar": ["b"]}

# 构建状态图
workflow = StateGraph(State)
workflow.add_node(node_a)
workflow.add_node(node_b)
workflow.add_edge(START, "node_a")
workflow.add_edge("node_a", "node_b")
workflow.add_edge("node_b",END)

# 检查点管理器
checkpointer = InMemorySaver()

# 配置检查点管理器
config:RunnableConfig ={
    "configurable":{"thread_id":"1"}
}

# 运行
graph = workflow.compile()
# 调用
result = graph.invoke({"foo":""},config)
print(result)

