import os
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from dotenv import (
    load_dotenv,
)  # to hide connection string, security, flexibility(easy to config changes wihtout code edits. You just modify the url), conevnience
import uuid
from about_bp import about_bp
from flask_wtf import FlaskForm


# from file name import variable name

load_dotenv()  # loads to os environment variables.

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FORM_SECRET_KEY")  # token

connection_string = os.environ.get("AZURE_DATABASE_URL")
# connection_string = "mssql+pyodbc://<username>:<password>@moviesserversanlam.database.windows.net:1433/moviesdb?driver=ODBC+Driver+17+for+SQL+Server&Encrypt=yes&TrustServerCertificate=no&Connection Timeout=30"
app.config["SQLALCHEMY_DATABASE_URI"] = connection_string
db = SQLAlchemy(app)


# Driver={ODBC Driver 18 for SQL Server};Server=tcp:
# Driver={ODBC Driver 18 for SQL Server};Server=tcp:alexserver1.database.windows.net,1433;Database=moviesdb;Uid=alexlazarus;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;


# Model(SQLAlchemy) == Schema


class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(
        db.String(50), primary_key=True, default=lambda: str(uuid.uuid4())
    )  # you dont wanna auto increment in the python world. If you want to merge tables together this make sure that the primary keys are unique. Security as well.
    name = db.Column(db.String(100))
    poster = db.Column(db.String(255))
    rating = db.Column(db.Float)
    summary = db.Column(db.String(500))
    trailer = db.Column(db.String(255))

    # JSON
    def to_dict(self):
        return {
            "id": self.id,  # this is for the front end people. They can have any key so it can support older and newer versions of the app.  So if you want to maintain a project then you dont have to change the column name in the database
            "name": self.name,
            "poster": self.poster,
            "rating": self.rating,
            "summary": self.summary,
            "trailer": self.trailer,
        }


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(
        db.String(50), primary_key=True, default=lambda: str(uuid.uuid4())
    )  # you dont wanna auto increment in the python world. If you want to merge tables together this make sure that the primary keys are unique. Security as well.
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50))

    # JSON
    def to_dict(self):
        return {
            "id": self.id,  # this is for the front end people. They can have any key so it can support older and newer versions of the app.  So if you want to maintain a project then you dont have to change the column name in the database
            "username": self.username,
            "password": self.password,
        }


from wtforms.validators import InputRequired, Length, ValidationError
from wtforms import StringField, PasswordField, SubmitField


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


try:
    with app.app_context():
        # Use text() to explicitly declare your SQL command
        result = db.session.execute(text("SELECT 1")).fetchall()
        print("Connection successful:", result)
        # db.create_all() #sync tables to db
except Exception as e:
    print("Error connecting to the database:", e)


from movies_bp import movies_bp
from movies_list_bp import movies_list_bp
from users_bp import users_bp
from main_bp import main_bp

app.register_blueprint(about_bp, url_prefix="/about")
app.register_blueprint(movies_bp, url_prefix="/movies")
app.register_blueprint(movies_list_bp, url_prefix="/movie-list")
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(main_bp)


if __name__ == "__main__":
    app.run(debug=True)
