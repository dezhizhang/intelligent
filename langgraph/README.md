# langgraph

## 安装开发包

### 1. 安装langchain

```bash
pip install langchain langchain-community langchain-ollama
```

### 2. 向量库安装

```bash
pip instal chromadb langchain-chroma
```

## 模型调用

### 1. 调用本地deepseek

```python
from langchain.chat_models import init_chat_model

llm = init_chat_model(
    model="ollama:deepseek-r1:7b",
    base_url="http://localhost:11434",
    temperature=0.1,
    max_token=10,
)

for chunk in llm.stream("中国唐诗"):
    print(chunk.content, end='', flush=True)

```

### 2 调用openai

```python
### 老版本
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    base_url="https://poloai.top/v1",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    temperature=0.5,
)

for chunk in llm.stream("来一首唐诗"):
    print(chunk.content, end='', flush=True)

### 新版本v1.0
from langchain.chat_models import init_chat_model

llm = init_chat_model(
    model="gpt-4o-mini",
    base_url="https://poloai.top/v1",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    temperature=0.5,
)

for chunk in llm.stream("你是 请解释一下大模型"):
    print(chunk.content, end="", flush=True)
```

## 创建自能体

### 1. 创建基础自能体

```python
from langchain.agents import create_agent
from dotenv import load_dotenv

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


```
### 2. 创建工具类型自能体
````python
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()


def get_weather(city: str) -> str:
    """获取天气信息"""
    return f"It's always sunny in {city}!"


agent = create_agent(
    model="deepseek:deepseek-chat",
    tools=[get_weather]
)

result = agent.invoke({"messages": [{"role": "user", "content": "What is the weather in SF"}]})
messages = result['messages']

for message in messages:
    print(message)

````
## 
###
```python
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from  dotenv import load_dotenv

load_dotenv()

checkpoint = InMemorySaver()

agent = create_agent(
    model="deepseek:deepseek-chat",
    # 创建记忆功能
    checkpointer=checkpoint,
)

config = {"configurable":{"thread_id":"1"}}

result = agent.invoke(
    {"messages":[{"role":"user","content":"来一首宋词"}]},
    config=config
)

messages = result['messages']
print(f"历史消息:{len(messages)} 条")
for message in messages:
    message.pretty_print()

```
