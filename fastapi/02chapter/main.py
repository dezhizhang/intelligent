from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/items",tags=['item测试接口'])
async def get_items():
    return {"userid": 1001}



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8086,reload=True)
