from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph,START
from langgraph.graph import END

graph = StateGraph(dict)

# 定义节点
def my_node(state:dict,config:RunnableConfig):
    print("in node",config["configurable"]["user_id"])
    return {"result":f"hello,{state['input']}"}


def my_other_node(state:dict):
    return state

graph.add_node("my_node",my_node)
graph.add_node("other_node",my_other_node)


graph.add_edge(START,"my_node")
graph.add_edge("my_node","other_node")
graph.add_edge("other_node",END)


app = graph.compile()

graph_png = app.get_graph().draw_mermaid_png()
with open("node_case.png","wb") as f:
    f.write(graph_png)



