import uvicorn
from typing import Union
from  fastapi import FastAPI

app = FastAPI()
@app.get("/query/{id}")
async def get_query(id:Union[int,str]):
    return {"id":id}

if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)