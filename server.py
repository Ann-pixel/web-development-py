from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    # return "<h1>Hello Gauri!</h1>"
    return render_template("./index.html")


@app.route("/blog")
def blog():
    return "<h2>These are my thoughts..</h2>"


@app.route("/blog/<username>")
def blog_user(username="a default value"):
    # return (
    #     "<h1 style='color:red'>I'm not superstitious, but I am a little stitious</h1>"
    # )
    return render_template("./index.html", name=username)


@app.route("/blog/<username>/<int:post_id>")
def blog_fun(username="a default value", post_id=0):
    # return (
    #     "<h1 style='color:red'>I'm not superstitious, but I am a little stitious</h1>"
    # )
    return render_template("./index.html", name=username, id=post_id)
