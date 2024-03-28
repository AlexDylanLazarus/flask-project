from flask import Blueprint, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from app import db, User

users_bp = Blueprint("users_bp", __name__)


@users_bp.route("/")
def login_page():
    return render_template("forms.html")


@users_bp.route("/register")  # HOF
def register_page():
    return render_template("register.html")


@users_bp.route("/after_login", methods=["POST"])
def after_login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Query the database to find a user with the provided username
    user = User.query.filter_by(username=username).first()

    if user:
        # If a user with the provided username exists, verify the password
        if user.password == password:
            return "Login successful"
        else:
            return "Invalid password", 401
    else:
        # User not found
        return "User not found", 404


@users_bp.route("/after_register", methods=["POST"])
def after_register():
    username = request.form.get("username")
    password = request.form.get("password")

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return "Username already exists", 400  # Bad Request

    new_user = User(username=username, password=password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return "Registration successful"
    except Exception as e:
        db.session.rollback()
        return f"Error occurred: {str(e)}", 500
