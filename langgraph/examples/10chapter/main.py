from  langchain.agents import create_agent
from dotenv import  load_dotenv

load_dotenv()

agent = create_agent(
    model="deepseek:deepseek-chat"
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "hello wold"}]
})

messages = result['messages']

for message in messages:
    print(message)



