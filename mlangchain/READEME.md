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





