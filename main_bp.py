from flask import Blueprint, render_template, request

main_bp = Blueprint("main_bp", __name__)

hobbies = ["gaming", "reading", "soccer", "ballet", "gyming", "yoga"]
name = "Caleb"


@main_bp.route("/profile")
def profile_page():
    return render_template("profile.html", name=name, hobbies=hobbies)


@main_bp.route("/sample")
def sample_page():
    return render_template("sample.html")


@main_bp.route("/dashboard1", methods=["POST"])
def dashboard_page():
    username = request.form.get(
        "username"
    )  # if the method is get then you use args instead of form
    password = request.form.get("password")
    print(username, password)
    return f"<h1> hi {username}</h1>"


@main_bp.route(
    "/"
)  # / is the home page. remember the shortcut we learned in html with / in the anchor tag href.
def hello_world():
    return render_template("base.html")
