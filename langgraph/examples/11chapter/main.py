from langchain.agents import create_agent
from langchain_openai import ChatOpenAI


def send_email(to: str, subject: str, body: str):
    """
    发送邮件工具。
    参数:
        to: 收件人
        subject: 邮件主题
        body: 邮件正文
    """
    return f"发送邮件至:{to}"


llm = ChatOpenAI(
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1",
    model="gpt-4o-mini",
)


agent = create_agent(
    model=llm,
    tools=[send_email],
    system_prompt="你是一个邮件助手，请绐始使用 send_email 工具"
)

result = agent.invoke({"input": "给李雷发一封邮件，主题为问候，内容是你好"})
print(result)
