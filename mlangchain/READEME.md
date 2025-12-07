# langchain

## 大模型

### 1. 模型的调用

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

### 2. 对话模型调用

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

### 3. 多轮对话

```python
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

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

## 提示词模板

### 1. 字符串提示词模板

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

prompt_template = PromptTemplate.from_template("给我们讲一个{topic}笑话")
prompt = prompt_template.invoke({"topic": "python"})

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

response = llm.invoke(prompt)
print(response.content)
```

### 2. 会话提示词模板

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt_template = ChatPromptTemplate([
    ("system", "你是一个乐于肋人的助手"),
    ("user", "给我讲一个关于{topic}的笑话")
])

prompt = prompt_template.invoke({"topic": "python"})

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

response = llm.invoke(prompt)
print(response)

```

### 3. 占位符提示词模板

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI

prompt_template = ChatPromptTemplate(
    [
        ("system", "你是一个乐于助人的助手，在回答用户问题时，需要带上用户的名字"),
        ("user", "我是{name}"),
        MessagesPlaceholder("msgs")
    ]
)

prompt = prompt_template.invoke(
    {"msgs": [AIMessage(content="你好，有什么需要咨询的 ?"), HumanMessage(content="三国志的作者是谁？")], "name": "张三"})

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

response = llm.invoke(prompt)
print(response)

```

### 4. 少量样本提示词模板

```python
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

examples = [
    {"input": "北京天气怎么样", "output": "北京市"},
    {"input": "南京属于江苏省", "output": "南京市"},
    {"input": "武汉有什么好玩的地方", "output": "武汉市"}
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="输入：{input}\n输出：{output}",
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="input:{input}\noutput",
    input_variables=["input"]
)

prompt = few_shot_prompt.format(input="烟花三月下场州")

response = llm.invoke(prompt)
print(response.content)
```

### 5. 加载外部提示词模板

```python
from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

prompt_template = load_prompt("08-prompt.json")

prompt = prompt_template.invoke({"name": "小明", "who": "猫"})
response = llm.invoke(prompt)
print(response)

```

### 6. 部份赋值提示词模板

```python

from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("把大像放在冰箱需要三步，第一步:{first},第二步:{second},第三步:{third}")

first_prompt_template = prompt_template.partial(first="打开冰箱")
second_prompt_template = prompt_template.partial(second="把大像放进去")
third_prompt_template = prompt_template.partial(third="关闭冰箱")

print(third_prompt_template)

```

## 选择器类型

### 1. 长度样例选择器

```python

from langchain_core.example_selectors import LengthBasedExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

examples = [
    {"input": "快乐", "output": "悲伤"},
    {"input": "高", "output": "矮"},
    {"input": "精力充沛", "output": "昏昏欲睡"},
    {"input": "阳光", "output": "阴暗"},
    {"input": "喧哗", "output": "安静"},
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="input:{input}\noutput:{output}"
)

example_selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=50,
    get_text_length=lambda x: len(x),
)

dynamic_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    suffix="input:{input}\noutput:",
    input_variables=["input"],
)

short_question = "大"
prompt = dynamic_prompt.format(input=short_question)
print(prompt)

```

### 3. 自定义选择器

```python
from typing import Any, Dict, List
from langchain_core.example_selectors import BaseExampleSelector
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate


class CustomSelector(BaseExampleSelector):
    """医疗示例选择器"""

    def __init__(self, examples: List[dict[str, str]]):
        """
            初始化医疗示例选择器
            :param examples: 医疗相关的示列列表，每个示例是一个字典，包含输入和输出
        """
        self.examples = examples

    def add_example(self, example: dict[str, str]) -> Any:
        """将示例添加到存储中的键"""
        self.examples.append(example)

    def select_examples(self, input_variables: dict[str, str]) -> List[dict[str, str]]:
        """
        根据输入变量选择医疗示例
        :param input_variables: 包含选择条件(如疾病名称、症获等)的字典
        :return:符合条件的示列表
        """

        disease_name = input_variables.get("disease_name", None)
        if disease_name is None:
            return []
        selected_examples = [
            example for example in self.examples
            if disease_name.lower() in example['input'].lower()
        ]
        return selected_examples


# 示例数据,模拟数据库存放时数据

examples = [
    {"input": "流感症状", "output": "发烧、咳嗽、喉咙痛、身体酸痛。"},
    {"input": "糖尿病治疗", "output": "饮食控制、运动、药物"},
    {"input": "新冠肺炎症状", "output": "发烧、咳嗽、疲劳、味觉或嗅觉丧失。"},
    {"input": "糖尿病症状", "output": "口渴、尿频、体重减轻。"}
]

custom_selector = CustomSelector(examples)
selected_examples = custom_selector.select_examples({"disease_name": "糖尿病"})
print(selected_examples)


```

## 输出格式化

### 1. 字符串格式化输出

```python
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

prompt = "请用一句话解释量子力学"

parser = StrOutputParser()
response = llm.invoke(prompt)
print(response)

```

### 2. json格式化输出

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

template = """
    你是一个助手，需要返回用户信息的JSON格式数据
    {format_instructions}
    请返回一个包含以下字段的JSON对像
    - name：用户性名
    - age: 用户年龄
    - hobbies: 用户爱好
    - favorite_color: 用户最喜欢的颜色
用户信息：{text}
"""

parser = JsonOutputParser()

prompt_template = PromptTemplate(
    template=template,
    input_variables=['text'],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt = prompt_template.format_prompt(text="用户姓名张三，今年25岁，喜欢阅读，游泳和编程，最喜欢的颜色是蓝色")
response = llm.invoke(prompt)

output = parser.invoke(response)

print(output)
```

### 3. Pydantic 解析模板

```python
from typing import List, Optional

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)


class Movie(BaseModel):
    title: str = Field(description="电影标题")
    director: str = Field(description="导演名称")
    year: int = Field(description="上映年份", ge=1900, le=2023)
    genres: List[str] = Field(description="电影类型列表")
    rating: Optional[float] = Field(description="电影评分,0 ~ 10之前", ge=0, le=10)


template = """
你是一个电影信息助手，请从以下文本中提取电影信息，并以JSON格式返回
文本:{text}
{format_instructions}
"""

parser = PydanticOutputParser(pydantic_object=Movie)

prompt_template = PromptTemplate(
    template=template,
    input_variables=['text'],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

movie_text = """
《泰坦尼克号》是一部由詹姆斯·卡梅隆执导的史诗级浪漫?灾难电影。
这部电影于1997年上映讲述了穷画家杰克和贵族女露丝之间的爱情故事。
它被归类为爱情、灾难和剧情片获得了评论界和观众的广泛好评,IMDB评份为8.8分
"""

# 格式化提示
format_prompt = prompt_template.format_prompt(text=movie_text)

response = llm.invoke(format_prompt)
output = parser.invoke(response)
print(output)

```

### 6. 自定义格式化输出

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, AIMessageChunk

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)


def parse(ai_message: AIMessage) -> str:
    """Parse the AI message"""
    return ai_message.content.swapcase()


response = llm.invoke("hello")
print(parse(response))
```

## LCEL 表过式

### 1. 管道符表过式

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

prompt_template = ChatPromptTemplate.from_template("给我讲一个{topic}的笑话")

chain = prompt_template | llm

response = chain.invoke({"topic": "老王"})
print(response)

```

### 2. LCEL 实现的基本原理

```python
class Expression:
    """表过式基类，所有组件都继承自此类"""

    def __init__(self, func):
        self.func = func

    def __call__(self, value):
        return self.func(value)

    def __or__(self, other):
        """重载 | 运算符，返回一个新的串联表达式"""
        return Expression(lambda x: other(self(x)))


def upper(s):
    return s.upper()


def lower(s):
    return s.lower()


def reverse(s):
    return s[::-1]


Upper = Expression(upper)
Lower = Expression(lower)
Reverse = Expression(reverse)

result = Expression(lambda x: x) | Upper | Reverse

print(result("hello world"))

```

### 3. RunnableLambda 对像调用

```python

from langchain_core.runnables import RunnableLambda


def multiply(a: int, b: int) -> int:
    return a * b


def multiply_dict_wrapper(inputs: dict):
    return multiply(inputs['a'], inputs['b'])


runnable_multiply = RunnableLambda(multiply_dict_wrapper)
print(runnable_multiply.invoke({"a": 2, "b": 3}))

```

### 4. Runnable 复杂调用

```python
from typing import AsyncIterator, Iterator
from langchain_core.runnables import Runnable


class TextTransformer(Runnable):
    def __init__(self, prefix: str = "处理后的文本"):
        self.prefix = prefix

    def invoke(self, input: str) -> str:
        """自定义文本处理逻辑"""
        processed_text = input.upper()
        return f"{self.prefix}{processed_text}"

    async def ainvoke(self, input: str) -> str:
        """异步处理实现"""
        return self.invoke(input)

    def stream(self, input: str) -> Iterator[str]:
        processed_text = input.upper()
        for char in processed_text:
            yield f"{self.prefix}{char}"

    async def astream(self, input: str) -> AsyncIterator[str]:
        processed_text = input.upper()
        for char in processed_text:
            yield f"{self.prefix}{char}"

    async def abatch(self, inputs: list[str]) -> list[str]:
        return [await self.ainvoke(input) for input in inputs]


transform = TextTransformer("结果")
result = transform.invoke("hello world")
print(result)
print("*" * 30)

for chunk in transform.stream("hello world"):
    print(chunk)


```

### 5. RunnableSequence 串形调用

```python
from langchain_core.runnables import RunnableLambda, RunnableSequence


def add_one(x: int) -> int:
    return x + 1


def mul_two(x: int) -> int:
    return x * 2


add_one_runnable = RunnableLambda(func=add_one)
mul_two_runnable = RunnableLambda(func=mul_two)

# sequence = RunnableSequence(first=add_one_runnable, last=mul_two_runnable)

sequence = add_one_runnable | mul_two_runnable
print(sequence.get_graph().draw_ascii())
print(sequence.invoke(1))


```

### 6. RunnableParallel 并行调用

```python
from langchain_core.runnables import RunnableLambda, RunnableParallel


def add_one(x: int) -> int:
    return x + 1


def mul_two(x: int) -> int:
    return x * 2


def mul_three(x: int) -> int:
    return x * 3


runnable_1 = RunnableLambda(add_one)
runnable_2 = RunnableLambda(mul_two)
runnable_3 = RunnableLambda(mul_three)

pipeline = runnable_1 | RunnableParallel(
    {"mul_two": runnable_2, "mul_three": runnable_3},
)

print(pipeline.get_graph().draw_ascii())

```

### 3. RunnablePassthrough

```python
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

passthrough = RunnablePassthrough()


def add_extra(input_text):
    return {"name": input_text["name"], "extra": "附加信息"}


add_extra_runnable = RunnablePassthrough(func=add_extra)

chain = passthrough | add_extra_runnable

print(chain.invoke({"name": "张三", "age": 18}))

print("==" * 20)
runnable_1 = passthrough.assign(geeting=lambda x: "hello")

chain = runnable_1 | add_extra_runnable

print(chain.invoke({"name": "张三", "age": 18}))

```

## 记忆功能

### 1. 无记忆功能

```python
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个乐于助人的助手，尽你所能回答所有问题，回答方式简结，20字左右"),
        ("user", "{question}")
    ]
)

chain = prompt_template | llm
response = chain.invoke({"question": "你好,我叫老顾,请请问金庸是谁"})
print(response.content)

response = chain.invoke({"question": "你好,你知道我叫什么名字"})
print(response.content)


```

### 2. MessagesPlaceholder 占位符实现记忆功能

```python
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个乐于助人的助手，尽你所能回答所有问题，回答方式简结，20字左右"),
        MessagesPlaceholder(variable_name="messages"),
        ("user", "{question}")
    ]
)

chain = prompt_template | llm
response = chain.invoke({
    "messages": [
        HumanMessage(content="你好,我叫老顾,请请问金庸是谁"),
        AIMessage(content="I love programming"),
    ],
    "question": "你好，你知道我叫什么名字"
})

print(response)


```

### 3. ChatMessageHistory 实现记忆

```python
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:7b",
    base_url="http://localhost:11434"
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个乐于助人的助手，尽你所能回答所有问题，回答方式简结，20字左右"),
        MessagesPlaceholder(variable_name="messages"),
        ("user", "{question}")
    ]
)

chain = prompt_template | llm
chat_message_history = ChatMessageHistory()
chat_message_history.add_user_message("你好,我叫老顾,请请问金庸是谁")
chat_message_history.add_ai_message("I love programming")

response = chain.invoke(
    {
        "question": "你好，你知道我叫什么名字",
        "messages": chat_message_history.messages,
    }
)

print(response.content)


```

### 5. SQLChatMessageHistory 长期记忆

```python
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:7b",
    base_url="http://localhost:11434"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个助手，用20个字以内回答"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ]
)


def get_session_history(session_id: str):
    return SQLChatMessageHistory(session_id=session_id, connection="sqlite:///history.db")


chain = prompt | llm
chain_width_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

config = {"configurable": {"session_id": "a1"}}

# r1 = chain_width_history.invoke({"input":"我是数擎，请问中国首都是哪个城市？"},config=config)

r1 = chain_width_history.invoke({"input": "你知道我的名字叫什么吗"}, config=config)
print(r1)


```

## 文件加载

### 1. TextLoader 加载text文本

```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader(file_path="./examples.txt", encoding="utf-8")

document = loader.load()
print(document[0].page_content)

```

### 2. PyPDFLoader 加载pdf文件

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path="examples.pdf")

document = loader.load()

for i, doc in enumerate(document):
    print(f"文档片段{i + 1} 内容:{doc}")
```

### 3. Docx2txtLoader 加载doc文档

```python
from langchain_community.document_loaders import Docx2txtLoader

loader = Docx2txtLoader(file_path='examples.docx')

document = loader.load()

for i, doc in enumerate(document):
    print(f'文档片段{i + 1},文档内容:{doc}')

```

## 工具函数

### 1. 装饰器工具函数

```python
from langchain_core.tools import tool
from pydantic import BaseModel, Field


class CityModel(BaseModel):
    city: str = Field(..., description="城市名称")


@tool(description="获取天气信息", args_schema=CityModel)
def get_weather(city: str) -> str:
    """获取城市天气信息"""
    return f"It's sunny in {city}"


print(get_weather.name)
print(get_weather.description)
print(get_weather.args)

```







