from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# local
movies = [
    {
        "id": "99",
        "name": "Vikram",
        "poster": "https://m.media-amazon.com/images/M/MV5BMmJhYTYxMGEtNjQ5NS00MWZiLWEwN2ItYjJmMWE2YTU1YWYxXkEyXkFqcGdeQXVyMTEzNzg0Mjkx._V1_.jpg",
        "rating": 8.4,
        "summary": "Members of a black ops team must track and eliminate a gang of masked murderers.",
        "trailer": "https://www.youtube.com/embed/OKBMCL-frPU",
    },
    {
        "id": "100",
        "name": "RRR",
        "poster": "https://englishtribuneimages.blob.core.windows.net/gallary-content/2021/6/Desk/2021_6$largeimg_977224513.JPG",
        "rating": 8.8,
        "summary": "RRR is an upcoming Indian Telugu-language period action drama film directed by S. S. Rajamouli, and produced by D. V. V. Danayya of DVV Entertainments.",
        "trailer": "https://www.youtube.com/embed/f_vbAtFSEc0",
    },
    {
        "id": "101",
        "name": "Iron man 2",
        "poster": "https://m.media-amazon.com/images/M/MV5BMTM0MDgwNjMyMl5BMl5BanBnXkFtZTcwNTg3NzAzMw@@._V1_FMjpg_UX1000_.jpg",
        "rating": 7,
        "summary": "With the world now aware that he is Iron Man, billionaire inventor Tony Stark (Robert Downey Jr.) faces pressure from all sides to share his technology with the military. He is reluctant to divulge the secrets of his armored suit, fearing the information will fall into the wrong hands. With Pepper Potts (Gwyneth Paltrow) and Rhodes (Don Cheadle) by his side, Tony must forge new alliances and confront a powerful new enemy.",
        "trailer": "https://www.youtube.com/embed/wKtcmiifycU",
    },
    {
        "id": "102",
        "name": "No Country for Old Men",
        "poster": "https://upload.wikimedia.org/wikipedia/en/8/8b/No_Country_for_Old_Men_poster.jpg",
        "rating": 8.1,
        "summary": "A hunter's life takes a drastic turn when he discovers two million dollars while strolling through the aftermath of a drug deal. He is then pursued by a psychopathic killer who wants the money.",
        "trailer": "https://www.youtube.com/embed/38A__WT3-o0",
    },
    {
        "id": "103",
        "name": "Jai Bhim",
        "poster": "https://m.media-amazon.com/images/M/MV5BY2Y5ZWMwZDgtZDQxYy00Mjk0LThhY2YtMmU1MTRmMjVhMjRiXkEyXkFqcGdeQXVyMTI1NDEyNTM5._V1_FMjpg_UX1000_.jpg",
        "summary": "A tribal woman and a righteous lawyer battle in court to unravel the mystery around the disappearance of her husband, who was picked up the police on a false case",
        "rating": 8.8,
        "trailer": "https://www.youtube.com/embed/nnXpbTFrqXA",
    },
    {
        "id": "104",
        "name": "The Avengers",
        "rating": 8,
        "summary": "Marvel's The Avengers (classified under the name Marvel Avengers\n Assemble in the United Kingdom and Ireland), or simply The Avengers, is\n a 2012 American superhero film based on the Marvel Comics superhero team\n of the same name.",
        "poster": "https://terrigen-cdn-dev.marvel.com/content/prod/1x/avengersendgame_lob_crd_05.jpg",
        "trailer": "https://www.youtube.com/embed/eOrNdBpGMv8",
    },
    {
        "id": "105",
        "name": "Interstellar",
        "poster": "https://m.media-amazon.com/images/I/A1JVqNMI7UL._SL1500_.jpg",
        "rating": 8.6,
        "summary": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA\n pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team\n of researchers, to find a new planet for humans.",
        "trailer": "https://www.youtube.com/embed/zSWdZVtXT7E",
    },
    {
        "id": "106",
        "name": "Baahubali",
        "poster": "https://flxt.tmsimg.com/assets/p11546593_p_v10_af.jpg",
        "rating": 8,
        "summary": "In the kingdom of Mahishmati, Shivudu falls in love with a young warrior woman. While trying to woo her, he learns about the conflict-ridden past of his family and his true legacy.",
        "trailer": "https://www.youtube.com/embed/sOEg_YZQsTI",
    },
    {
        "id": "107",
        "name": "Ratatouille",
        "poster": "https://resizing.flixster.com/gL_JpWcD7sNHNYSwI1ff069Yyug=/ems.ZW1zLXByZC1hc3NldHMvbW92aWVzLzc4ZmJhZjZiLTEzNWMtNDIwOC1hYzU1LTgwZjE3ZjQzNTdiNy5qcGc=",
        "rating": 8,
        "summary": "Remy, a rat, aspires to become a renowned French chef. However, he fails to realise that people despise rodents and will never enjoy a meal cooked by him.",
        "trailer": "https://www.youtube.com/embed/NgsQ8mVkN8w",
    },
    {
        "name": "PS2",
        "poster": "https://m.media-amazon.com/images/M/MV5BYjFjMTQzY2EtZjQ5MC00NGUyLWJiYWMtZDI3MTQ1MGU4OGY2XkEyXkFqcGdeQXVyNDExMjcyMzA@._V1_.jpg",
        "summary": "Ponniyin Selvan: I is an upcoming Indian Tamil-language epic period action film directed by Mani Ratnam, who co-wrote it with Elango Kumaravel and B. Jeyamohan",
        "rating": 8,
        "trailer": "https://www.youtube.com/embed/KsH2LA8pCjo",
        "id": "108",
    },
    {
        "name": "Thor: Ragnarok",
        "poster": "https://m.media-amazon.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_.jpg",
        "summary": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA\\n pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team\\n of researchers, to find a new planet for humans.",
        "rating": 8.8,
        "trailer": "https://youtu.be/NgsQ8mVkN8w",
        "id": "109",
    },
]


@app.route(
    "/"
)  # / is the home page. remember the shortcut we learned in html with / in the anchor tag href.
def hello_world():
    return render_template("base.html")


users = [
    {
        "name": "John",
        "pic": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTF3FUIWqvlCTuJzEb3juBvSd54uz1gn1SY8_RBJFUJBg&s",
        "pro": True,
    },
    {
        "name": "Carl",
        "pic": "data:image/jpeg;base64,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",
        "pro": False,
    },
    {
        "name": "Sarah",
        "pic": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxQcpt-l3VPFa-mO-9DWhGNYUw5gHDjQ0klT0D-YJEkw&s",
        "pro": False,
    },
]


# decorators are high order functions
@app.route("/about")
def about_page():
    return render_template("about.html", users=users)


hobbies = ["gaming", "reading", "soccer", "ballet", "gyming", "yoga"]
name = "Caleb"


@app.route("/profile")
def profile_page():
    return render_template("profile.html", name=name, hobbies=hobbies)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", movies=movies)


if __name__ == "__main__":
    app.run(debug=True)


# /movies -> JSON data

# your flask server always has to be running for postman to make a request
# remember when you give the app to customer, dont run in debug
# You can't directly change the methods with chrome. Theres no provision for testing purposes. If you know js, you can do it
# with postman, you're just testing you api


@app.get("/movies")
def get_movies():
    return jsonify(movies)


# @app.post("/movies")
# def post_movies():
#     new_movie = request.json
# movies.append(new_movie)
# result = {"message": "Added Successfully"}
# return jsonify(result)


# this is only temporarily stored
@app.post("/movies")
def post_movies():
    new_movie = request.json()
    movie_ids = [int(movie["id"]) for movie in movies]
    max_id = max(movie_ids) if movie_ids else 0
    new_movie["id"] = str(max_id + 1)
    movies.append(new_movie)
    result = {"message": "Added Successfully"}
    return jsonify(result), 201


@app.get("/movies/<id>")
def get_movie_by_id(id):
    # Code here to match the movie with id
    # Generator expression to get the first match
    # Generators dont create a new memory location, operates on same memory
    # it automatically converts to iter

    # find an item list | next(expression,default value)
    # Advantage: Loop will stop as soon as match is found

    filtered_movie = next((movie for movie in movies if movie["id"] == id), None)
    if filtered_movie:
        return jsonify(filtered_movie)
    else:
        return jsonify({"message": "movie not found"}), 404


# create a delete api for movies
@app.delete("/movies/<id>")
def delete_movie(id):
    id_for_deletion = next((movie for movie in movies if movie["id"] == id), None)
    if id_for_deletion:
        print(movies.remove(id_for_deletion))
        return jsonify({"message": "deleted successfully", "data": id_for_deletion})
    else:
        return jsonify({"message": "movie not found"}), 404


# update movie
@app.put("/movies/<id>")
def update_movie(id):
    update_movie = request.json
    id_for_updating = next((movie for movie in movies if movie["id"] == id), None)
    if id_for_updating:
        # What does update do? Pass a dictionary in it. it is a method for dictionaries.
        # other way y = {**id_for_updating, "name": "blah"}
        id_for_updating.update(update_movie)  # mutable | same memory
        return jsonify(
            {"message": "movie updated successfully", "data": id_for_updating}
        )
    else:
        return jsonify({"message": "movie not found"}), 404


# @app.put("/movies/<id>")
# def update_movie_by_id(id):
#     movie_idx = next((idx for idx, movie in enumerate(movies) if movie["id"] == id), None) # same memory
#     body = request.json
#     movies[movie_idx] = {**movies[movie_idx], **body}
