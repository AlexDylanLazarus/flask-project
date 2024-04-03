import uuid

# absolute or relative import
# from ..extensions import db # .. means one folder back - relative import. . one dot means current folder

# relative import (current folder)
# absolute import (project folder)
from extensions import db

# if flask project is ur start point then u say from models.movie import


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
