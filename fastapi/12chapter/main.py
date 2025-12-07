from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id:int
    name:str
    tags:list[str] = []

@app.get("/item/dict",response_model=Item,response_model_exclude_none=True)
async def get_item():
    return Item(id=2,name="tom")

if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)