from langchain_core.messages import AnyMessage
from typing_extensions import  TypedDict
from langchain_core.messages import AIMessage



class State(TypedDict):
    messages:list[AnyMessage]
    extra_field:int


def node(state:State):
    messages = state["messages"]
    new_message = AIMessage("你好！我是节点1")

    return {
        "messages": messages + [new_message],
        "extra_field": 1
    }

# 创建图使用state通信
from langgraph.graph import  StateGraph
graph = StateGraph(State)
graph.add_node(node)
graph.set_entry_point("node")
graph_builder = graph.compile()


# 查看节点与图关系
from IPython.display import Image,display
display(Image(graph_builder.get_graph().draw_mermaid_png()))



from langchain_core.messages import HumanMessage

result = graph_builder.invoke({
    "messages":[HumanMessage("你好，我是tom")],
})

from langchain_core.messages import HumanMessage
result = graph_builder.invoke({
    "messages": [HumanMessage("你好，我是tom")],
})

for message in result["messages"]:
    print(message.pretty_print())










