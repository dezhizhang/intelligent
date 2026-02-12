# fastapi 入门到精通文档

## 项目初始化与环境配置

### 1. 项目初始化

```bash
uv init my_project
```

### 2. 初始化虚拟环境并激活

```bash
uv .vene
source .venv/bin/activate # mac
venv\Scripts\activate # win
```

## 包安装和hello world

### 1. 安装fastapi和uvicorn

```bash
uv add fastapi uvicorn
```

### 2. 创建hello world

```python

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8082)
```

### 3. 应用并启动hello world

```bash
uvicorn main:app --reload --port 8082
http://localhost:8082
```

## 请求参数获取

### 1. 路径参数获取

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8082)
# 输入http://localhost:8082/items/1
```

### 2. 查询参数

```python
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]


@app.get("/items")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip + limit]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8082)
# http://127.0.0.1:8000/items?skip=0&limit=10
```

### 3. body请求参数

```python
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/item")
async def create_item(item: Item):
    return item
```

## 响应参数

### 1. form响应参数
```python
from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login")
async def login(username: Annotated[str, Form()]):
    return {"username": username}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8082)


```

