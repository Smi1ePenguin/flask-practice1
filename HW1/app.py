from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", name="이범준", student_id="22011669")

@app.route("/profile")
def profile():
    hobbies = ["게임 플레이", "노래방", "게임 개발"]
    return render_template("profile.html", hobbies=hobbies)

@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)