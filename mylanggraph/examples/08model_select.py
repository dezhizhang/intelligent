import operator
from typing import Annotated, Sequence
from typing_extensions import TypedDict
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI

from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.runnables.config import RunnableConfig
from langgraph.graph import END, StateGraph, START
from IPython.display import Image,display

deepseekLmm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key="sk-df7bba3befa946c283f20c88cc47f9da",
    base_url="https://api.deepseek.com/v1",
)

openaiLmm = ChatOpenAI(
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1",
    temperature=0,
    streaming=True,
)

# 定义要切换的模型
models = {
    "deepseek": deepseekLmm,
    "openai": openaiLmm
}


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]


def _call_model(state: AgentState, config: RunnableConfig):
    """使用LCEL的配置"""
    model_name = config['configurable'].get('model', 'deepseek')
    model = models[model_name]
    response = model.invoke(state['messages'])
    return {"messages": response['messages']}


builder = StateGraph(AgentState)
builder.add_node("model",_call_model)
builder.add_edge(START,"model")
builder.add_edge("model",END)

graph = builder.compile()
display(Image(graph.get_graph().draw_mermaid_png()))

response = graph.invoke({"messages":[HumanMessage(content="hi 你是难?")]})

print(response)





