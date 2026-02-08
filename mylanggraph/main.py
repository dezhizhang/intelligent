from typing import List,TypedDict,Optional
from langgraph.graph import StateGraph,START,END

class Logs(TypedDict):
    id:str
    question:str
    docs:Optional[List]
    answer:str
    grade:Optional[int]
    grader:Optional[str]
    feedback:Optional[str]


class FailureAnalysisState(TypedDict):
   docs:List[Logs]
   failures:List[Logs]
   fa_summary:str


# 获取失败的日志
def get_failures(state):
    docs = state['docs']
    failures = [doc for doc in docs if 'grade' in doc]
    return {"failures":failures}

# 生成故障分析总结
def generate_summary(state):
    failures = state['failures']
    fa_summary = "Poor quality retrieval of Chroma documentation."
    return {"fa_summary":fa_summary}


fa_builder = StateGraph(FailureAnalysisState)
fa_builder.add_node("get_failures",get_failures)
fa_builder.add_node("generate_summary",generate_summary)
fa_builder.add_edge(START,"get_failures")
fa_builder.add_edge("get_failures","generate_summary")
fa_builder.add_edge("generate_summary",END)









