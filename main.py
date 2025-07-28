from fastapi import FastAPI,Body
from typing import Optional
app =FastAPI()

@app.get("/")
async def hello_world():
    return {
        "msg" : "Hello world"
    }   

@app.get("/greet/{username}")
async def greet(username,q:Optional[str]=None,data=Body()):
    print(data)
    print(q)
    print(data['Hello'])
    return {
        "msg" : f"Good Morning {username}"
    }

