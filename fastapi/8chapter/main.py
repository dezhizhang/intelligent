from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):
    name:str
    description:str | None = None
    price:float

app = FastAPI()
@app.get("/user")
async def create_user(item:Item):
    return item


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)