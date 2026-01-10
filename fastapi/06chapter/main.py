

# from fastapi import FastAPI,Query
# import uvicorn
#
# app = FastAPI()
# @app.get("/item")
# def read_item(item_id:str=Query(...,min_length=3,max_length=6)):
#     """必传参数"""
#     return {"item_id": item_id}
#
# if __name__ == "__main__":
#     uvicorn.run(app,host="0.0.0.0",port=8000)


from fastapi import FastAPI,Query
import uvicorn

app = FastAPI()
@app.get("/item")
def read_item(item_id:str=Query(...,min_length=1,max_length=100)):
    """必传参数"""
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)




