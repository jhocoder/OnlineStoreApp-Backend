from flask import Blueprint, url_for, redirect, render_template, request
from db import queries
from db.mongodb import getDB
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user
from User import User
auth_blueprint = Blueprint("auth",__name__)



@auth_blueprint.route("/")
def home():
    return redirect(url_for("auth.login"))

@auth_blueprint.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST": 
        try:
            email = request.form["email"]
            password =request.form["password"]
            query = queries.login(email, password)
            print(query)
            if query:
                user = User(query)
                login_user(user)
            
                return redirect(url_for("auth.profile"))
        except Exception as e:
            print("error", e)
    return render_template("auth/login.html")


@auth_blueprint.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST": 
        try:
            email = request.form["email"]
            username = request.form["username"]
            password = generate_password_hash(request.form["password"])
            print(email, username, password)
            queries.register(email, username, password)
            
        except Exception as e:
            print("error", e)
    return render_template("auth/register.html")

@auth_blueprint.route("/profile", methods=["POST", "GET"])
@login_required
def profile():
    return render_template("auth/profile.html")
