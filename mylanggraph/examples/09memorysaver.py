from langchain_deepseek import ChatDeepSeek
from langgraph.graph import StateGraph,MessagesState,START
from langgraph.checkpoint.memory import MemorySaver

llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key="sk-df7bba3befa946c283f20c88cc47f9da",
    base_url="https://api.deepseek.com/v1",
)

def call_model(state:MessagesState):
    response = llm.invoke(state['messages'])
    return {"messages":response}

builder = StateGraph(MessagesState)
builder.add_node("call_model",call_model)
builder.add_edge(START,"call_model")


# 激活持久化层

memory = MemorySaver()
graph = builder.compile(checkpointer=memory)

config = {"configurable":{"thread_id":"1"}}

input_message = {"role":"user","content":"hi 我是tom"}
for chunk in graph.stream({"messages":[input_message]},config,stream_mode="values"):
    print(chunk['messages'][-1].pretty_print())


input_message = {"role":"user","content":"我名字叫什么"}
for chunk in graph.stream({"messages":[input_message]},config,stream_mode="values"):
    print(chunk['messages'][-1].pretty_print())








