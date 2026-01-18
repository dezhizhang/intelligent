
import uvicorn

from  fastapi import FastAPI

app = FastAPI()

@app.get("/args/{id}")
def path_args(id:int):
    return {"message":f"{id}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

