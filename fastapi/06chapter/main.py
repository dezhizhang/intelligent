
import uvicorn
from  fastapi import  FastAPI

app = FastAPI()

@app.get("/args/{id}")
def get_args(id:int):
    return {"id": id}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)