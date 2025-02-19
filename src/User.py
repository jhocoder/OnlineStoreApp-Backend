from flask_login import UserMixin
from db.mongodb import getDB
from bson import ObjectId



class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data["_id"])
        self.email = user_data["email"]
        self.username = user_data["username"]

        
