from numpy.distutils.system_info import conda

# fastapi

## 环境搭建

### 1 创建虚拟环境

```bash
conda create -n fastapi_env python=3.12
```

### 2. 激活虚拟环境

```bash
conda activate fastapi_env
```

### 3. 退出虚拟环境

```bash
conda deactivate
```

## 创建应用与启动

### 1. helloworld 应用

```python
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### 2. 启动应用

```bash
uvicorn main:app -reload 
```
### 3. 路径参数
```python
import uvicorn
from  fastapi import  FastAPI

app = FastAPI()


@app.get("/args/{id}")
def path_args1(id:int):
    return {"message": f"{id}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
```

