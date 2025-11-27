from langchain.agents import create_agent
from openai import api_key, base_url


def send_email(to:str,subject:str,body:str):
    email = {
        "to": to,
        "subject": subject,
        "body": body
    }

    return f"发送邮件至:{to}"


agent = create_agent(
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1",
    model="gpt-4o-mini",
    tools=[send_email],
    system_prompt="你是一个邮件助手，请绐始使用 send_email 工具"
)
