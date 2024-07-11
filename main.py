from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from schema import Users, telReq
from mongo import *

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def home():
    return "this is homepage"

@app.post("/user/warranty_check")
def getWarrantyDate(req : telReq) -> Users:
    try:
       return find_user(req)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail="Database error")
    
@app.post("/user/add")
def addUser(req : Users):
    try:
       return insert_user(req)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail="Database error")
   
@app.delete("/user/delete")
def delUser(req : telReq):
    try:
       delete_user(req)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail="Database error")   
    
@app.get("/user/viewall")
def viewUser():
    try:
       return get_all_users()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail="Database error")   
    
    
