
from langchain.agents import AgentType,initialize_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults(
    tavily_api_key="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"
)


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION

agent_executor = initialize_agent(
    tools=[search],
    llm=llm,
    agent=agent,
    verbose=True,
)

response = agent_executor.invoke("查询广州今天的天气情况")
print(response)






