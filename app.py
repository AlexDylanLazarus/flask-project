import os
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from dotenv import (
    load_dotenv,
)  # to hide connection string, security, flexibility(easy to config changes wihtout code edits. You just modify the url), conevnience
import uuid
from routes.about_bp import about_bp
from extensions import db


# from file name import variable name

load_dotenv()  # loads to os environment variables.

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FORM_SECRET_KEY")  # token

connection_string = os.environ.get("AZURE_DATABASE_URL")
# connection_string = "mssql+pyodbc://<username>:<password>@moviesserversanlam.database.windows.net:1433/moviesdb?driver=ODBC+Driver+17+for+SQL+Server&Encrypt=yes&TrustServerCertificate=no&Connection Timeout=30"
app.config["SQLALCHEMY_DATABASE_URI"] = connection_string
# db = SQLAlchemy(app)
db.init_app(app)

# Driver={ODBC Driver 18 for SQL Server};Server=tcp:
# Driver={ODBC Driver 18 for SQL Server};Server=tcp:alexserver1.database.windows.net,1433;Database=moviesdb;Uid=alexlazarus;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;


# Model(SQLAlchemy) == Schema

try:
    with app.app_context():
        # Use text() to explicitly declare your SQL command
        result = db.session.execute(text("SELECT 1")).fetchall()
        print("Connection successful:", result)
        # db.create_all() #sync tables to db
except Exception as e:
    print("Error connecting to the database:", e)


from routes.movies_bp import movies_bp
from routes.movies_list_bp import movies_list_bp
from routes.users_bp import users_bp
from routes.main_bp import main_bp

app.register_blueprint(about_bp, url_prefix="/about")
app.register_blueprint(movies_bp, url_prefix="/movies")
app.register_blueprint(movies_list_bp, url_prefix="/movie-list")
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(main_bp)


if __name__ == "__main__":
    app.run(debug=True)
