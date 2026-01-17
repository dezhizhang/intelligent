from fastapi import FastAPI,APIRouter

app = FastAPI()

v1 = APIRouter(prefix="/v1")

user = APIRouter(tags=["user"],prefix="/user")

@user.get("/info")
async def info():
    return {"name":"tom"}


v1.include_router(user)
app.include_router(v1)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



