from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

sy = SystemMessage(
    content="你是一个起名大师",
    additional_kwars={"大师姓名":"陈瞎子"}
)

hu = HumanMessage(
    content="请问大师叫什么"
)

ai = AIMessage(
    content="我叫陈瞎子"
)

prompt = [sy,hu,ai]
print(prompt)

