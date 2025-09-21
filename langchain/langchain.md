# langchain

## 模型调用

### invoke 函数的调用

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

question = "langchain是什么"
response = llm.invoke(question)

print(response.content)
```

### stream 流式输出

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

question = "langchain是什么"
for chunk in llm.stream(question):
    print(chunk.content)

```

### 批处理

```python

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

response = llm.batch(["langchain作者是谁", "langchain的竟品有那些"])
print(response)
```

### 异步处理

```python


import asyncio
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)
question = "介绍一下langchain"


async def main():
    async for event in llm.astream_events(question, version="v2"):
        print(event)


if __name__ == "__main__":
    asyncio.run(main())
```

### with_structured_output

```python
from langchain_openai import ChatOpenAI
from typing import Optional, Union
from typing_extensions import Annotated, TypedDict

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)


class Joke(TypedDict):
    """Joke to tell user."""
    setup: Annotated[str, ..., "The setup of the joke."]
    punchline: Annotated[str, ..., "The punchline of the joke."]
    rating: Annotated[Optional[Union[int, float]], "The rating of the joke."]


structured_llm = llm.with_structured_output(Joke)
for chunk in structured_llm.stream("给我讲一个关于程序员的笑话"):
    print(chunk)


```

### deepseek 调用

```python
from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
    temperature=0,
    model="deepseek-chat",
    api_key="sk-7b5ca2da2eae420eb985dfd196e3895f",
    base_url="https://deepseek.com/v1"
)

resp = llm.invoke("介绍下自已")
print(resp.content)

```

## 提示词

### 字符串模板PromptTemplate

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("请评价 {product} 的优点,包括{aspect1}和{aspect2}")
template = prompt.format(product="手机", aspect1="屏幕", aspect2="拍照")

print(template)

```

### 聊天模板ChatPromptTemplate

```python
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个起名大师,你的名字叫{name}."),
        ("human", "您好{name} 您感觉如何"),
        ("ai", "你好！你状态非常好"),
        ("human", "你叫什么名字"),
        ("ai", "你好，我叫{name}"),
        ("human", "user_input")
    ]
)

chats = chat_template.format_messages(name="陈大师", user_input="你的爸爸是谁？")

print(chats)


```

### MessagesPlaceholder 消息占位符

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

prompt_template = ChatPromptTemplate(
    [
        ("system", "你是一个历害的人工智能助手"),
        MessagesPlaceholder(variable_name="msgs"),
    ]
)

result = prompt_template.invoke({"msgs": [HumanMessage(content="hi!")]})
print(result)

```

### 模板组合

```python
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

sy = SystemMessage(
    content="你是一个起名大师",
    additional_kwars={"大师姓名": "陈瞎子"}
)

hu = HumanMessage(
    content="请问大师叫什么"
)

ai = AIMessage(
    content="我叫陈瞎子"
)

prompt = [sy, hu, ai]
print(prompt)

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

## 解析器

### 字符串解析器StrOutputParser

```python
from langchain_core.output_parsers import StrOutputParser
# 字符串输出解析器
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-3.5-turbo-0125",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

response = llm.invoke("什么是大语言模型?")

parser = StrOutputParser()
content = parser.invoke(response)
print(content)
```

### json解析器JsonOutputParser

```python
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-3.5-turbo-0613",
    temperature=0.9,
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个靠谱的{role}"),
        ("human", "{question}")
    ]
)

prompt = chat_prompt_template.invoke(input={
    "role": "人工智能专家",
    "question": "人工智能用英文怎么说,问题用q表示，答案用a表示，返回一个json数据",
})

response = llm.invoke(prompt)

parser = JsonOutputParser()
json = parser.invoke(response)
print(json)
```

### json路径解析器get_format_instructions

```python
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 初始化语言模型
llm = ChatOpenAI(
    model="gpt-3.5-turbo-0613",
    temperature=0.9,
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

parser = JsonOutputParser()
prompt_template = PromptTemplate.from_template(
    template="回答用户的查询\n 满足的格式为{form_instructions}\n 问题为{question}\n",
    partial_variables={"form_instructions": parser.get_format_instructions()}
)

joke_query = "告诉我一个笑话"

prompt = prompt_template.invoke(input={"question": joke_query})
response = llm.invoke(prompt)

json_result = parser.invoke(response)

print(json_result)

```

### 管道解析器

```python
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(
    model="gpt-3.5-turbo-0613",
    temperature=0.9,
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

parser = JsonOutputParser()
prompt_template = PromptTemplate.from_template(
    template="回答用户的查询\n 满足的格式为{form_instructions}\n 问题为{question}",
    partial_variables={"form_instructions": parser.get_format_instructions()}
)

joke_query = "告诉我一个笑话"

chain = prompt_template | llm | parser
json_result = chain.invoke(input={"question": joke_query})
print(json_result)

```

### XMLOutputParser 解析器

```python
from langchain_core.output_parsers import XMLOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

actor_query = "周星驰的简短电影记录,使用中文回复"

parser = XMLOutputParser()

# 生成提示词模板
prompt_template = PromptTemplate.from_template(
    template="用户的问题:{query}\n便用的格式:{format_instructions}",
    partial_variables={"query": actor_query}
)

prompt = prompt_template.partial(format_instructions=parser.get_format_instructions())

response = llm.invoke(prompt.invoke(input={"query": actor_query}))

xml_result = parser.invoke(response)

print(xml_result)


```
## 链
### LLMChain 链调用
```python
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

prompt = PromptTemplate.from_template(
    template="你是一个数字高手,帮我解决如下数学问题:{question}"
)

chain = LLMChain(llm=llm, prompt=prompt)
response = chain.invoke(input={"question": "1 + 2 * 3 = ?"})
print(response)

```
