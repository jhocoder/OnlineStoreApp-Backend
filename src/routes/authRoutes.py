from flask import Blueprint, url_for, redirect, render_template, request
from db import queries
from db.mongodb import getDB
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user
from User import User
import logging
from senderEmail import sendmail


loggerAuth = logging.getLogger("tienda") 
 
fichero = logging.FileHandler("tienda.log", encoding="utf-8")

fichero.setLevel(logging.DEBUG)

fichero.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

loggerAuth.addHandler(fichero)
loggerAuth.setLevel(logging.DEBUG)

loggerAuth.info("Logger de autenticación inicializado correctamente.")

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/")
def home():
    return redirect(url_for("auth.login"))

@auth_blueprint.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST": 
        try:
            email = request.form["email"]
            password = request.form["password"]
            query = queries.login(email, password)
            loggerAuth.debug(f"Intento de inicio de sesión para {email}")

            if query:
                user = User(query)
                login_user(user)
                loggerAuth.info(f"Usuario {email} ha iniciado sesión correctamente")
                return redirect(url_for("auth.profile"))

        except Exception as e:
            loggerAuth.error(f"Error en login: {e}", exc_info=True)
    
    return render_template("auth/login.html")

@auth_blueprint.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST": 
        try:
            email = request.form["email"]
            username = request.form["username"]
            password = generate_password_hash(request.form["password"])
            queries.register(email, username, password)
            sendmail(email)

            loggerAuth.info(f"Nuevo usuario registrado: {email} - {username}")

        except Exception as e:
            loggerAuth.error(f"Error en registro: {e}", exc_info=True)

    return render_template("auth/register.html")

@auth_blueprint.route("/profile", methods=["POST", "GET"])
@login_required
def profile():
    return render_template("auth/profile.html")
