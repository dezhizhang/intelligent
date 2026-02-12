from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login")
async def login(username: Annotated[str, Form()]):
    return {"username": username}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8082)

