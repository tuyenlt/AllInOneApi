import pymongo
from schema import Users,telReq
sauna_client = pymongo.MongoClient("mongodb+srv://maksauna8668:tuyenlu111@maksauna.cumgjig.mongodb.net/?retryWrites=true&w=majority&appName=Maksauna")

db = sauna_client['Maksauna']
SaunaUsers = db["SaunaUsers"]

def is_exits(curr):
	cnt = 0
	for c in curr:
		cnt = cnt + 1
	if cnt == 0:
		return False
	else:
		return True

def insert_user(user : Users):
	if is_exits(SaunaUsers.find({"tel" : user.tel})):
		return "User Already Exists"
	# tmp = user.dict()
	SaunaUsers.insert_one(user.model_dump())
	return "Insert User Success"

def find_user(tel : telReq):
    return SaunaUsers.find_one({"tel" : tel.tel})
	
def delete_user(tel : telReq):
	if not is_exits(SaunaUsers.find({"tel" : tel.tel})):
		return "User Not Found"
	SaunaUsers.delete_one({"tel" : tel.tel})
	return "deleted"

def get_all_users():
	cursor = SaunaUsers.find({})
	users = []
	for user in cursor:
		del user['_id']
		users.append(user)
	return users
