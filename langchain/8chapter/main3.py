from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

prompt_template = ChatPromptTemplate(
    [
        ("system","你是一个历害的人工智能助手"),
        MessagesPlaceholder(variable_name="msgs"),
    ]
)

result = prompt_template.invoke({"msgs":[HumanMessage(content="hi")]})
print(result)


