from fastapi import FastAPI,Request

app = FastAPI()

@app.get("/client-info")
def client_info(request: Request):
    return {
        "client_name": request.client.host,
        "请求方法":request.method,
        "请求参数":request.query_params,
        "请求files":request.client._fields
    }

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)

