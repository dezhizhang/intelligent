from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.graph import MessagesState,START
from langgraph.prebuilt import ToolNode
from langgraph.graph import END,StateGraph
from langgraph.checkpoint.memory import MemorySaver


@tool
def play_song_on_qq(song:str):
    """在qq音乐上播放歌曲"""
    return f"成功在QQ音乐上播放了{song}!"

@tool
def play_song_on_163(song:str):
    """在网易云上播放歌典"""
    return f"成功在网易云上播放了{song}!"

tools = [play_song_on_163,play_song_on_qq]

tool_node = ToolNode(tools)



llm = ChatOpenAI(
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1",
    temperature=0,
    streaming=True,
)

model = llm.bind_tools(tools,parallel_tool_calls=False)

def should_continue(state):
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return "end"
    else:
        return "continue"

def call_model(state):
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages": response}

# 定义一个新图
workflow = StateGraph(MessagesState)

workflow.add_node("agent",call_model)
workflow.add_node("action",tool_node)


workflow.add_edge(START,"agent")

workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue":"action",
        "end":END,
    }
)

workflow.add_edge("action","agent")

# 设置内存
memory = MemorySaver()

app = workflow.compile(checkpointer=memory)








