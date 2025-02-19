from flask import Flask
from routes.authRoutes import auth_blueprint
from db.mongodb import getDB
from flask_login import LoginManager
from bson import ObjectId
from User import User



app = Flask(__name__)
app.secret_key = "pepito"
loginmanager = LoginManager()
loginmanager.init_app(app)
loginmanager.login_view = "auth.login"


db = getDB()
user_collections = db["usuarios"]


@loginmanager.user_loader
def load_user(user_id):
    searchUser = user_collections.find_one({"_id":ObjectId(user_id)})
    if searchUser:
        return User(searchUser)


app.register_blueprint(auth_blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=3030, host="localhost")