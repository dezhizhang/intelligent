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