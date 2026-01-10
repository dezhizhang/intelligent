import uvicorn
from fastapi import FastAPI

app = FastAPI()
@app.get("/query")

async def page_limit(page,limit):
    return {"page": page, "limit": limit}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


