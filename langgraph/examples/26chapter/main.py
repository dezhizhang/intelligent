# from langchain.chat_models import init_chat_model
#
# llm = init_chat_model(
#     model="gpt-4o-mini",
#     base_url="https://poloai.top/v1",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM"
# )
#
# resp = llm.invoke("你好，你是谁...")
# print(resp)
#
#


# from langchain.chat_models import init_chat_model
# from langchain.agents import create_agent
# llm = init_chat_model(
#     model="gpt-4o-mini",
#     base_url="https://poloai.top/v1",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM"
# )
#
# agent = create_agent(
#     model=llm,
#     tools=[],
#     system_prompt="You are a helpful assistant"
# )
#
# results = agent.invoke({"messages":[{"role":"user","content":"你是谁，你能帮我解决什么问题"}]})
# print(results)

from langgraph.prebuilt import  create_react_agent
from langchain.chat_models import init_chat_model

llm = init_chat_model(
    model="gpt-4o-mini",
    base_url="https://poloai.top/v1",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM"
)

agent = create_react_agent(
    model=llm,
    base_url="https://poloai.top/v1",

)







