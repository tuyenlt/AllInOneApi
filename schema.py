from pydantic import BaseModel,Field
from typing import Optional, Union, Any, List
from typing import Literal

class TodoModel(BaseModel):
    text : str
    done : bool 
    
class LoginModel(BaseModel):
    email : str
    password : str

class RegesterModel(BaseModel):
    email : str
    password : str
    displayName : str

class insertUserListModel(BaseModel):
    id : str
    listName : str
    value : Any

class Users(BaseModel):
    id : str
    email : str 
    password : str
    displayName : str 
    description : str
    avatar: str ## img path
    friendsLists : List[str]
    postsList : List[str]
    todoList : List[TodoModel]
    
    
class Content(BaseModel):
    text: str
    imgPath: Optional[str]  # Equivalent to string | undefined in TypeScript

class React(BaseModel):
    like: int
    dislike: int
    love: int

class Post(BaseModel):
    id: str
    postOwnerId: str
    postOwnerName: str
    avatarSrc: str
    title: str
    type: Literal["post", "comment"]
    content: Content
    react: React
    comment: List[str]

class getPostRequest(BaseModel):
    id : str