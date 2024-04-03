from flask import Blueprint, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from app import db, User, RegistrationForm, LoginForm

users_bp = Blueprint("users_bp", __name__)


@users_bp.route("/register1", methods=["GET", "POST"])
def register_page1():
    form = RegistrationForm()

    # only on POST
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data  # get data from form
        # the first username is the column and the second username is the form data in the following line

        new_user = User(username=username, password=password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return "<h1>Registration successful</h1>"
        except Exception as e:
            db.session.rollback()
            return f"<h1>Error occurred: {str(e)}</h1>", 500

    return render_template("register1.html", form=form)


@users_bp.route("/login1", methods=["GET", "POST"])
def login_page1():
    form = LoginForm()

    # only on POST
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data  # get data from form
        # the first username is the column and the second username is the form data in the following line

        new_user = User(username=username, password=password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return "<h1>Login successful</h1>"
        except Exception as e:
            db.session.rollback()
            return f"<h1>Error occurred: {str(e)}</h1>", 500

    return render_template("login1.html", form=form)
