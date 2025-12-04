# langchain

### 模型的调用

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

response = llm.invoke("写一首关于冬天的诗")
print(response.content)
print(type(response))
```

### 对话模型调用

```python
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

messages = [
    SystemMessage(content="我是人工智能助手,我叫晓智"),
    HumanMessage(content="你好，我是小明，很高兴认识你")
]

response = llm.invoke(messages)
print(response.content)

```
### 多轮对话
```python
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_openai import  ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

messages = [
    SystemMessage(content="你是知识渊博的专家知道很多著名书籍相关知识请简洁的用20个字回答问题"),
    HumanMessage(content="我的身份是学员,名字叫小顾"),
    AIMessage(content="欢迎,有什么需要咨询的?"),
    HumanMessage(content="三国志作者的是谁?"),
    AIMessage(content="《三国志》的作者是三国时期的历史学家陈寿寿。"),
    HumanMessage(content="红楼梦呢?"),
]

response = llm.invoke(messages)
print(response)
```

### 环境变量读取配置文件
```python
from langchain_openai import  ChatOpenAI
import os
import dotenv
dotenv.load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("OPENAI_BASE_MODEL"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)


response = llm.invoke("什么是langchain")
print(response.content)
```

### 流式输出

```python

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1",
    streaming=True
)

message = [
    HumanMessage(content="你好，请介绍一下自已")
]

for chunk in llm.stream(message):
    print(chunk.content, end="", flush=True)

print("\nend")
```

## 提示词

### PromptTemplate 实例化

```python

from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
    template="你是一个{role} 你的名字叫{name}",
    input_variables=["role", "name"]
)

prompt = prompt_template.format(role="人工智能专家", name="数擎科技")
print(prompt)
```

### 提示词结合大模型调用

```python
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

template = PromptTemplate.from_template(
    template="请评价{product}的优点,包括{aspect1}"
)

prompt = template.invoke(input={"product": "智能手机", "aspect1": "拍照质量"})

response = llm.invoke(prompt)

print(response)
```

### from_messages 提示调模板

```python


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个AI助手,你的名字叫{name}"),
        ("human", "我的问题是{question}")
    ]
)

prompt = template.invoke({"name": "贵州数擎科技有限公司", "question": "1 + 2 * 3 = ?"})
response = llm.invoke(prompt)
print(response)

```

### MessagesPlaceholder

```python
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.chat import MessagesPlaceholder

chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个Ai助手，你的名字叫{name}"),
    MessagesPlaceholder(variable_name="msgs")
])

prompt = chat_prompt_template.invoke({
    "name": "数擎科技",
    "msgs": [HumanMessage(content="我的问题是 1 + 2 * 3 = ?")]
})

print(prompt)

```

### StrOutputParser 字符串解析器

```python
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

response = llm.invoke("什么是大模型")
parser = StrOutputParser()

string = parser.invoke(response)

print(string)
```
### JsonOutputParser 解析器
```python
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

parser = JsonOutputParser()

prompt_template = ChatPromptTemplate.from_template(
    template="回答用户的查询\n 满足的格式为{format_instructions}\n 问题为{question}\n",
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt_template | llm | parser

response = chain.invoke(input={"role": "人工智能专家", "question": "人工智能简介"})
print(response)

```

### 本地模型调用
```python
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:7b"
)

messages = [
    HumanMessage(content="介绍一下你自已")
]

response = llm.invoke(messages)

print(response.content)
```

## 链
### 最基础链
```python
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:7b"
)

prompt = PromptTemplate.from_template(
    template="你是一位数学高手,帮我解决如下的数学问题：{question}"
)

chain = LLMChain(llm=llm, prompt=prompt)

response = chain.invoke("1 + 2 * 3 = ？")
print(response)


```

### ChatPromptTemplate
```python
from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:7b"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个数学高手"),
        ("human", "帮我解决如下的数学问题:{question}")
    ]
)

chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

response = chain.invoke(input={"question": "1 + 2 * 3 = ?"})
print(response)


```