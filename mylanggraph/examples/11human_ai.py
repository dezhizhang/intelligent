from typing_extensions import TypedDict
from langgraph.graph import StateGraph,START,END
from langgraph.types import Command,interrupt
from langgraph.checkpoint.memory import MemorySaver
from IPython.display import  Image,display


class State(TypedDict):
    input:str
    user_feedback:str

def step_1(state):
    print("--step1--")
    pass

def human_feedback(state):
    print("--human_feedback--")
    feedback = interrupt("place provide feedback")
    return {"user_feedback":feedback}

def step_3(state):
    print("--step_3--")
    pass

builder = StateGraph(State)
builder.add_node("step_1",step_1)
builder.add_node("human_feedback",human_feedback)
builder.add_node("step_3",step_3)
builder.add_edge(START,"step_1")
builder.add_edge("step_1","human_feedback")
builder.add_edge("human_feedback","step_3")
builder.add_edge("step_3",END)

memory = MemorySaver()
graph = builder.compile(checkpointer=memory)
# display(Image(graph.get_graph().draw_mermaid_png()))


graph_png = graph.get_graph().draw_mermaid_png()
with open("node_case.png","wb") as f:
    f.write(graph_png)


