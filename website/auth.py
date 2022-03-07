from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return "Login"

@auth.route("/sign Up")
def sign_up():
    return "sign Up"

@auth.route("/logout")
def logout():
    return "logout"

