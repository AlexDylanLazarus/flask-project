from flask import Blueprint, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models.movie import Movie
from extensions import db


movies_bp = Blueprint("movies_bp", __name__)


# route created for add movie.html
@movies_bp.route("/add", methods=["GET"])
def add_movie():
    return render_template("add_movie.html")


# get all movies
@movies_bp.get("/")
def get_movies():
    movie_list = Movie.query.all()  # Select * from movies
    data = [movie.to_dict() for movie in movie_list]  # list of dictionaries
    return jsonify(data)


# get movie by id
@movies_bp.get("/<id>")
def get_movie_by_id(id):
    movie = Movie.query.get(id)
    if movie:
        data = movie.to_dict()
        return jsonify(data)
    else:
        return jsonify({"message": "movie not found"}), 404


# create movie
@movies_bp.post("/")
def post_movies():
    data = request.json()
    new_movie = Movie(**data)
    try:
        db.session.add(new_movie)
        db.session.commit()
        result = {"message": "Added Successfully", "data": new_movie.to_dict()}
        return jsonify(result), 201
    except Exception as e:
        db.session.rollback()  # undo the change
        return jsonify({"message": str(e)}), 500


# delete by id
@movies_bp.delete("/<id>")
def delete_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        return jsonify({"message": "Movie not found"}), 404
    try:
        data = movie.to_dict()
        db.session.delete(movie)  # Changed 'data' to 'movie'
        db.session.commit()  # this makes the change permanant
        return jsonify({"message": "DELETED MOVIE SUCCESSFULLY", "data": data})
    except Exception as e:
        db.session.rollback()  # undo the change
        return jsonify({"message": str(e)}), 500


# update movie
@movies_bp.put("/<id>")
def update_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        return jsonify({"message": "Movie not found"}), 404
    body = request.json
    try:
        for key, value in body.items():
            if hasattr(
                movie, key
            ):  # checking if it has the column in table.  if you receive a json then it wont only match the keys. We also dont want to add columns that dont exist
                setattr(movie, key, value)
        db.session.commit()
        return jsonify(
            {"message": "Movie updated successfully!", "data": movie.to_dict()}
        )
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500


@movies_bp.route("/add/added", methods=["POST"], endpoint="post_movie")
def post_movie():
    name = request.form.get("name")
    poster = request.form.get("poster")
    rating = request.form.get("rating")
    summary = request.form.get("summary")
    trailer = request.form.get("trailer")
    new_movie = (
        Movie(  # if you wanna do unpacking method then it needs to be the same name
            name=name, poster=poster, rating=rating, summary=summary, trailer=trailer
        )
    )
    try:
        db.session.add(new_movie)
        db.session.commit()
        data = new_movie.to_dict()
        return f"<h1>{data['name']} added successfully"
    except Exception as e:
        db.session.rollback()  # undo the change
        return jsonify({"message": str(e)}), 500


@movies_bp.route("/delete", methods=["POST"])
def delete_movie_by_id():
    print(request.form.get("movie_id"))
    id = request.form.get("movie_id")
    filtered_movie = Movie.query.get(id)
    if not filtered_movie:
        return "<h1>Movie not found</h1>", 404
    try:
        data = filtered_movie.to_dict()
        db.session.delete(filtered_movie)
        db.session.commit()  # Making the change (update/delete/create) permanent
        return f"<h1>{data['name']} Movie deleted Successfully</h1>"
    except Exception as e:
        db.session.rollback()  # Undo the change
        return f"<h1>Error happened {str(e)}</h1>", 500
