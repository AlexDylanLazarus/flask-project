from flask import Blueprint, render_template, jsonify, request, flash
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from models.user import User
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from flask_login import login_user
from models.movie import Movie
from werkzeug.security import generate_password_hash, check_password_hash

users_bp = Blueprint("users_bp", __name__)


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=6)])
    password = PasswordField(
        "Password", validators=[InputRequired(), Length(min=8, max=12)]
    )
    submit = SubmitField("Sign Up")

    # _<columnname>
    # validate is automatically called when form.validate_on_submit()
    def validate_username(self, field):
        # inform WTF that there is an error
        print("validate username ⭐⭐⭐⭐", field.data)
        existing_user = User.query.filter_by(username=field.data).first()
        if existing_user:
            raise ValidationError("Username is taken")


# GET ISSUE TOKEN
# POST VERIFY TOKEN


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=6)])
    password = PasswordField(
        "Password", validators=[InputRequired(), Length(min=8, max=12)]
    )
    submit = SubmitField("Login")

    # _<columnname>
    # validate is automatically called when form.validate_on_submit()
    def validate_username(self, field):
        # inform WTF that there is an error
        print("validate username ⭐⭐⭐⭐", field.data)
        existing_user = User.query.filter_by(username=field.data).first()
        if not existing_user:
            raise ValidationError("Invalid creditenials")

    def validate_password(self, field):
        # inform WTF that there is an error
        print("validate username ⭐⭐⭐⭐", field.data)
        existing_user = User.query.filter_by(username=self.username.data).first()
        if existing_user:
            user_data_db = existing_user.to_dict()
            form_password = field.data
            if not check_password_hash(user_data_db["password"], form_password):
                raise ValidationError("Invalid creditenials")


@users_bp.route("/register1", methods=["GET", "POST"])
def register_page1():
    form = RegistrationForm()

    # only on POST
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data  # get data from form
        password_hash = generate_password_hash(form.password.data)
        # the first username is the column and the second username is the form data in the following line
        print(form.password.data, password_hash)
        new_user = User(
            username=username, password=password_hash
        )  # create hashed password on left side

        try:
            db.session.add(
                new_user
            )  # insert into database. This is where we'll do hashing
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
        user = User.query.filter_by(username=username).first()
        login_user(user)  # token - cookies
        try:
            db.session.add(user)
            db.session.commit()
            flash("You were successfully logged in")
            return "<h1>Login was successful</h1>"
        except Exception as e:
            db.session.rollback()
            return f"<h1>Error occurred: {str(e)}</h1>", 500

    return render_template("login1.html", form=form)
