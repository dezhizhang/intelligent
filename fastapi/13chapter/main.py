from fastapi import FastAPI
from openai import BaseModel

app = FastAPI()


@app.get("/item/dict")
async def item_dict():
    return {"name":"tom","age":22,"tags":[1,2,3]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)