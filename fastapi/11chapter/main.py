import uvicorn
from fastapi import FastAPI,Request

app = FastAPI()


@app.get("/client-info")
def client_info(request: Request):
    return {
        "请求URL":request.url,
        "请求方法":request.method,
        "请求IP":request.client.host,
    }


if __name__ == "__main__":
   uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)
