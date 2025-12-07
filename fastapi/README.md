# fastapi


### 1. 路经参数
```python

import uvicorn
from  fastapi import  FastAPI

app = FastAPI()

@app.get("/args/{id}")
def get_args(id:int):
    return {"id": id}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
```
### 2. 查询参数
```python
from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/query")
def get_query(page:int,size:int):
    return {"page":page,"size":size}


if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)
```
### 3. 请求体参数
```python
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):
    name:str
    description:str | None = None
    price:float



app = FastAPI()
@app.post("/user")
async def create_user(item:Item):
    return item


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
```
### 4. 参数约束
```python
import uvicorn
from typing import Union
from  fastapi import FastAPI

app = FastAPI()
@app.get("/query/{id}")
async def get_query(id:Union[int,str]):
    return {"id":id}

if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)
```
### 5. 获取请求体
```python
import uvicorn
from fastapi import FastAPI,Request

app = FastAPI()


@app.get("/client-info")
def client_info(request: Request):
    return {
        "请求URL":request.url,
        "请求方法":request.method,
        "请求IP":request.client.host,
    }


if __name__ == "__main__":
   uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)
```
### 6. 响应json数据
```python
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    tags: list[str] = []


@app.get("/item/dict", response_model=Item, response_model_exclude_unset=True)
async def get_items_dict():
    return Item(id=2, name="tom")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
```


