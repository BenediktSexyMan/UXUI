from MovieInsert import *
from flask import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("forsida.html", movies=movies.values(), enumerate=enumerate)

@app.route("/actors/<movie>")
def actor(movie):
    try:
        movie = movies[movie]
    except KeyError:
        return "<h1 style='text-align: center;'>No movie '" + movie + "' found!</h1>"
    return render_template("leikarar.html", movie=movie, enumerate=enumerate)

app.run("0.0.0.0", 8080)