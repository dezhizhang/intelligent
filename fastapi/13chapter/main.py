import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id:int
    name:str
    price:float
    category:str

@app.get("/item")
async def get_items():
    return [Item(id=i,name=f"apple{i}",price=100*i,category="ipad") for i in range(1,101)]

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)