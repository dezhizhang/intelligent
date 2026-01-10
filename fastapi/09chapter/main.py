
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

class User(BaseModel):
    name: str = Field(default="tom")
    age: int = Field(default=18)

@app.post("/users")
def read_users(user:User):
    return {"users": user}

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)




