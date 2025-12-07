from fastapi import FastAPI
import  uvicorn

app = FastAPI()

@app.get("/get")
def get_test():
    return {"method": "get方法"}

@app.post("/post")
def post_test():
   return {"method": "post方法"}



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)