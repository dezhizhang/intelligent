from langchain.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)

# 1. 示例消息格式
examples = [
    {"input": "1 + 1 等于几?", "output": "1 + 1 等于2"},
    {"input": " 法图的首都是? ", "output": "巴黎"}
]

# 定义示列消息提示模板格式
msg_example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}")
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=msg_example_prompt,
    examples=examples,
)

print(few_shot_prompt.format())
