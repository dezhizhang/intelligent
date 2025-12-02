from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv

load_dotenv(verbose=True)

checkpoint = InMemorySaver()

agent = create_agent(
    model="deepseek:deepseek-chat",
    checkpointer=checkpoint
)

config = {"configurable":{"thread_id":"1"}}

result = agent.invoke(
    {"messages":[{"role":"user","content":"来一首宋词"}]},
    config=config
)

messages = result['messages']
print(f"历史消息:{len(messages)} 条")
for message in messages:
    message.pretty_print()
