from typing import Literal
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END,StateGraph,MessagesState
from langgraph.prebuilt import ToolNode

@tool
def search(query:str):
    """摸拟一个搜索工具"""
    if "上海" in query.lower() or "Shanghai" in query.lower():
        return "现在30度，有雾"
    return "现在35度，阳光明媚"


# 将工具函数放入工具列表
tools = [search]

# 创建工具节点
tool_node = ToolNode(tools)

llm = ChatOpenAI(
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1",
    model="gpt-4o",
    temperature=0
).bind_tools(tools)

# 定义函数，决定是否继续执行
def should_continue(state:MessagesState) -> Literal["tools",END]:
    messages = state["messages"]
    last_message = messages[-1]

    if last_message.tool_calls:
        return "tools"
    return END

# 定义调用模型的函数
def call_model(state:MessagesState):
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages": response}

# 用状态初始化图，定义一个新的状态图
workflow = StateGraph(MessagesState)
workflow.add_node("agent",call_model)
workflow.add_node("tools",tool_node)


workflow.set_entry_point("agent")

workflow.add_conditional_edges(
    "agent",
    should_continue,
)

workflow.add_edge("tools","agent")

# 初始化内存以图运行之间持久化状态
checkpointer = MemorySaver()

# 编译图
app = workflow.compile(checkpointer = checkpointer)

# 执行图，使用可运行对像
final_state = app.invoke(
    {"messages":[HumanMessage(content="上海的天气怎么样")]},
    config={"configurable":{"thread_id":42}}
)

result = final_state["messages"][-1].content


# 将生成的图片保存存到文件
graph_png = app.get_graph().draw_mermaid_png()
with open("langgraph.png","wb") as f:
    f.write(graph_png)











