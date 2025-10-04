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