from langgraph.graph import START,StateGraph

def my_node(state,config):
    return {"x":state['x'] + 1,"y":state['y'] + 2}


builder = StateGraph(dict)

builder.add_node(my_node)

builder.add_edge(START,"my_node")

graph = builder.compile()

print(graph)

print(graph.invoke({"x":1,"y":2}))



