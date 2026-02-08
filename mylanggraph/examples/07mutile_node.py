import operator
from typing import Any,Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph,START,END
from IPython.display import Image,display

class State(TypedDict):
    aggregate:Annotated[list,operator.add]

def a(state:State):
    print(f"添加A到{state['aggregate']}")
    return {"aggregate":['A']}

def b(state:State):
    print(f"添加B到{state['aggregate']}")
    return {"aggregate":['B']}

def c(state:State):
    print(f"添加C到{state['aggregate']}")
    return {"aggregate":['C']}

def d(state:State):
    print(f"添加C到{state['aggregate']}")
    return {"aggregate":['D']}


builder = StateGraph(State)
builder.add_node(a)
builder.add_node(b)
builder.add_node(c)
builder.add_node(d)

builder.add_edge(START,'a')
builder.add_edge('a','b')
builder.add_edge('a','c')
builder.add_edge('b','d')
builder.add_edge('d',END)
graph = builder.compile()




display(Image(graph.get_graph().draw_mermaid_png()))


result = graph.invoke({"aggregate":[]},{"configurable":{"thread_id":"foo"}})
print(result)





