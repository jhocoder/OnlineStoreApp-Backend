from db.mongodb import getDB
from bson import ObjectId
from werkzeug.security import check_password_hash, generate_password_hash


db = getDB()
user_collections = db["usuarios"]



def register(email, username, password):
    searchUser = user_collections.find_one({"email": email})
    
    if searchUser:
        return False
    
    return user_collections.insert_one({'email': email, 'username':username, 'password':password})

def login(email, password):
    searchUser = user_collections.find_one({"email": email})
    
    if searchUser and check_password_hash(searchUser["password"], password):
        return searchUser
    else:
        return False
