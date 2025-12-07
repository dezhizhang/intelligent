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


