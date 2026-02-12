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

## 参数获取

### 路径参数获取

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

