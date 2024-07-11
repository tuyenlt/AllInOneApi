from pydantic import BaseModel

class Users(BaseModel):
    tel : str
    name : str
    address : str
    done_day : str
    warranty_time : str
    
class telReq(BaseModel):
    tel : str