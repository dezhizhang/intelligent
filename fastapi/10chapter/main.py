from  fastapi import FastAPI,Query
import uvicorn

app = FastAPI()
@app.get("item")
def query_item(item_id:str = Query(...)):
    """...是必须传递"""
    return {"item_id":item_id}


if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)