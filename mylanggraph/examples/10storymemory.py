from typing import Literal

from langchain_deepseek import ChatDeepSeek
from langchain_core.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import MessagesState,StateGraph,START,END
from langgraph.prebuilt import ToolNode

memory = MemorySaver()

@tool
def search(query:str):
    """调用此函数可以浏览网络."""
    return "北京天气睛朗，大约22度，显度30%"

tools = [search]
tool_node = ToolNode(tools)

llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key="sk-df7bba3befa946c283f20c88cc47f9da",
    base_url="https://api.deepseek.com/v1",
)

bound_model = llm.bind_tools(tools)

def should_continue(state:MessagesState):
    """返回下一个执行的节点."""
    last_message = state['messages'][-1]
    if not last_message.tool_calls:
        return END
    return "action"

def call_model(state:MessagesState):
    response = bound_model.invoke(state['messages'])
    return {"messages": response}

workflow = StateGraph(MessagesState)
workflow.add_node("agent",call_model)
workflow.add_node("action",tool_node)


workflow.add_edge(START,"agent")

workflow.add_conditional_edges(
    "agent",
    should_continue,
)
workflow.add_edge("action","agent")

app = workflow.compile(checkpointer=memory)


config = {"configurable":{"thread_id":"1"}}

input_message = {"role":"user","content":"hi 我是tom"}
for chunk in app.stream({"messages":[input_message]},config,stream_mode="values"):
    print(chunk['messages'][-1].pretty_print())


input_message = {"role":"user","content":"我名字叫什么"}
for chunk in app.stream({"messages":[input_message]},config,stream_mode="values"):
    print(chunk['messages'][-1].pretty_print())








