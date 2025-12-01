from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

agent = create_agent(
    model="deepseek:deepseek-chat",
)

# 第一轮对话
results = agent.invoke({
    "messages":[{"role":"user","content":"来一首宋词"}]
})

messages = results['messages']
print(f"历史消息:{len(messages)}条")
for message in messages:
    message.pretty_print()

