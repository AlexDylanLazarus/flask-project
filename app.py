from flask import Flask

app = Flask(__name__)


@app.route(
    "/"
)  # / is the home page. remember the shortcut we learned in html with / in the anchor tag href.
def hello_world():
    return "<p>Super, cool</p>"


# decorators are high order functions
@app.route("/about")
def about_page():
    return "<h1>ABOUT PAGE</h1>"


if __name__ == "__main__":
    app.run(debug=True)
