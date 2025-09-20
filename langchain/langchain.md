# langchain

## 提示词

### 使用构造方法获取实例PromptTemplate

```python

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

# 创建input
prompt_template = PromptTemplate(
    template="你是一个{role},你的名字叫{name}",
    input_variables=["role", "name"]
)
prompt = prompt_template.format(role="人工智能专家", name="晓智")

resp = llm.invoke(prompt)
print(resp.content)


```
### 调用大模型
```python


from langchain_openai import  ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 创建大模型
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

# 创建提示词
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个AI助手,你的名字叫{name}"),
        ("human","我的问题是{question}")
    ]
)

prompt = prompt_template.invoke({"name":"晓智","question":"1 + 2 * 3 = ?"})
response = llm.invoke(prompt)

print(response.content)

```
### 插入提示词模板
```python
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.chat import MessagesPlaceholder

template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个AI助手,你的名字叫{name}"),
        MessagesPlaceholder(variable_name="msgs"),
    ]
)

prompt = template.invoke({
    "name": "晓智",
    "msgs": [HumanMessage(content="我的问题是:1 + 2 * 3 = ?")]
})

print(prompt)

```
### 简短提示词模板
```python
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
```
