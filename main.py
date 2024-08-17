from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schema import *
import pymongo


client = pymongo.MongoClient("mongodb+srv://keplerlu:tuyenlu111@allinoneusers.qtic57s.mongodb.net/?retryWrites=true&w=majority&appName=AllInOneUsers")
db = client.get_database("AllInOneUsers")
usersCollection = db.get_collection("users")
postsCollection = db.get_collection("posts")


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def convert_objectid_to_str(user):
    """Convert MongoDB ObjectId to string in the user document."""
    if user and "_id" in user:
        user["_id"] = str(user["_id"])
    return user

@app.get("/")
def home():
    return "this is homepage"

@app.post("/loginAuth")
def loginAuth(request: LoginModel):
    user = usersCollection.find_one({"email": request.email})
    if user is None:
        raise HTTPException(status_code=201, detail="User name does not exist")
    if user["password"] != request.password:
        raise HTTPException(status_code=202, detail="Wrong password")
    return convert_objectid_to_str(user)


@app.post("/userRegester")
def userRegester(request : RegesterModel):
    exitedUser = usersCollection.find_one({"email" : request.email})
    if exitedUser != None:
        raise HTTPException(status_code=201,detail="user name already exits")
    newUser = Users(
        id="tuyenlt",
        email= request.email,
        displayName= request.displayName,
        password=request.password,
        friendsLists=[],
        postsList=[],
        todoList=[]
    )
    
    usersCollection.insert_one(newUser.model_dump())
    return newUser
    
@app.post("/insertUserList")
def updateuser(request : insertUserListModel):
    print(request)
    user = usersCollection.find_one({"id" : request.id})
    if user == None:
        raise HTTPException(status_code=400,detail="user is not exits")
    usersCollection.update_one({"id" : request.id}, {"$set" : {request.listName : request.value}})
        
@app.post("/create-post")
def createPost(request : Post):
    try:
        postsCollection.insert_one(request.model_dump())
    except Exception as e:
        print(e)
        
        
@app.get("/get-post")
def getPost(req : getPostRequest):
    try:
        post = postsCollection.find_one({"id" : req.id})
        if post == None:
            return "post not exits"
        return convert_objectid_to_str(post)
    except Exception as e:
        print(e)