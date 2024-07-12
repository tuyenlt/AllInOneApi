from pydantic import BaseModel,Field

class Users(BaseModel):
    tel : str = Field(min_length=10)
    name : str 
    address : str 
    done_day : str
    warranty_time : str
    
class telReq(BaseModel):
    tel : str = Field(min_length=10)