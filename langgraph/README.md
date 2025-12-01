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
    print(chunk.content,end="",flush=True)
```
### 第一个智能体
