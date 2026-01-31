# 定义state
from langchain_core.messages import AnyMessage,HumanMessage
from typing_extensions import TypedDict
from langgraph.graph import StateGraph
from IPython.display import display,Image
# 定义节点间通讯的消息格式
class State(TypedDict):
    message: list[AnyMessage]
    extra_field:int

# 创建节点
def node(state: State):
    message=state["messages"]
    new_message = AnyMessage("你好！我是节点1")

    return {
        "message": message + [new_message],
        "extra_field": 1,
    }

# 创建图
graph = StateGraph(State)
graph.add_node(node)
graph.set_entry_point("node")
graph_builder=graph.compile()


# 查看节点图与结构
display(Image(graph_builder.get_graph().draw_mermaid_png()))


result = graph_builder.invoke({
    "messages":[HumanMessage("您好阿！我是tom")]
})

print(result)










