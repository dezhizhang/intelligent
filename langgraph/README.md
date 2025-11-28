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

### 1. 调用deepseek

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