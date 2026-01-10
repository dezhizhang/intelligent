from fastapi import FastAPI,Form

app = FastAPI()

@app.post("/login")
def login(username:str=Form(...), password:str=Form(...)):
    return {"username": username, "password": password}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)