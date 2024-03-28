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

try:
    with app.app_context():
        # Use text() to explicitly declare your SQL command
        result = db.session.execute(text("SELECT 1")).fetchall()
        print("Connection successful:", result)
except Exception as e:
    print("Error connecting to the database:", e)

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
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    # JSON
    def to_dict(self):
        return {
            "id": self.id,  # this is for the front end people. They can have any key so it can support older and newer versions of the app.  So if you want to maintain a project then you dont have to change the column name in the database
            "username": self.username,
            "password": self.password,
        }


@app.route(
    "/"
)  # / is the home page. remember the shortcut we learned in html with / in the anchor tag href.
def hello_world():
    return render_template("base.html")


from movies_bp import movies_bp
from movies_list_bp import movies_list_bp
from users import users_bp

app.register_blueprint(about_bp, url_prefix="/about")
app.register_blueprint(movies_bp, url_prefix="/movies")
app.register_blueprint(movies_list_bp, url_prefix="/movie-list")
app.register_blueprint(users_bp, url_prefix="/users")

hobbies = ["gaming", "reading", "soccer", "ballet", "gyming", "yoga"]
name = "Caleb"


@app.route("/profile")
def profile_page():
    return render_template("profile.html", name=name, hobbies=hobbies)


@app.route("/sample")
def sample_page():
    return render_template("sample.html")


@app.route("/dashboard1", methods=["POST"])
def dashboard_page():
    username = request.form.get(
        "username"
    )  # if the method is get then you use args instead of form
    password = request.form.get("password")
    print(username, password)
    return f"<h1> hi {username}</h1>"


from wtforms.validators import InputRequired, Length
from wtforms import StringField, PasswordField, SubmitField


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=6)])
    password = PasswordField(
        "Password", validators=[InputRequired(), Length(min=8, max=12)]
    )
    submit = SubmitField("Sign Up")


@app.route("/register1", methods=["GET", "POST"])
def register_page1():
    form = RegistrationForm()

    # only on POST
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data  # get data from form
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

    return render_template("register1.html", form=form)


# GET ISSUE TOKEN
# POST VERIFY TOKEN

if __name__ == "__main__":
    app.run(debug=True)
