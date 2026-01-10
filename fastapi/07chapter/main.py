import uvicorn
from fastapi import FastAPI,Path

app = FastAPI()

@app.get("/item/{item_id}")
def read_item(item_id:str | int):
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)


