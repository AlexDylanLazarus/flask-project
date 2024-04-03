from flask import Blueprint, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from models.user import User
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm

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
            if user_data_db["password"] != form_password:
                raise ValidationError("Invalid creditenials")


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
