import uuid
from extensions import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
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
