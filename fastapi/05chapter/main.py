from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post("/items",tags=["item测试接口"],summary="测试接口",description="功能简介")
def post_test():
    return {"message":"测试item接口"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)